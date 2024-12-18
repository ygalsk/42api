from django.core.management.base import BaseCommand
import os
import requests
import json

UID = os.getenv("SOCIAL_AUTH_42_KEY")
SECRET = os.getenv("SOCIAL_AUTH_42_SECRET")

def post42(url, payload):
    url = "https://api.intra.42.fr" + url
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post(url, headers=headers, data=payload)
    return response.json()

def get42(url, payload):
    url = "https://api.intra.42.fr" + url
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.get(url, headers=headers, data=payload)
    return response.json()

class Command(BaseCommand):
    help = "Fetch user data from 42 API"

    def handle(self, *args, **kwargs):
        # Authenticate and get the token
        wtoken = post42("/oauth/token", {
            "grant_type": "client_credentials",
            "client_id": UID,
            "client_secret": SECRET
        })

        # Get user data
        campus_users = []
        temp = []

        campus_users_general = '/v2/campus/39'
        campus_users_total = get42(campus_users_general, {"access_token": wtoken["access_token"]})
        total_users = campus_users_total["users_count"]
        total_pages = (total_users // 100 + 1) + 1

        print(f"Total users: {total_users} Total pages: {total_pages}")
        print("Fetching data from the API...")

        for i in range(1, total_pages):  
            campus_users += get42(f"/v2/campus/39/users?page[number]={i}&page[size]=100", {
                "access_token": wtoken["access_token"]
            })

        for user in campus_users:
            temp.append({
                "login": user.get("login"),
                "correction_point":  user.get("correction_point"),
                "pool_year": user.get("pool_year"),
                "location": user.get("location"),
                "updated_at": user.get("updated_at").split("T")[1].split(".")[0],
                "wallet": user.get("wallet")
            })

        for entry in temp:
            if entry["location"] is not None and entry["pool_year"] == '2022':
                print(f"\033[91m{entry['login']:<10}\033[0m Updated: {entry['updated_at']:<8} Eval Points: {str(entry['correction_point']):<5} Location: {str(entry['location']):<10} Wallet: {str(entry['wallet']):<10}")
            elif entry["location"] is not None and entry["pool_year"] == '2023':
                print(f"\033[92m{entry['login']:<10}\033[0m Updated: {entry['updated_at']:<8} Eval Points: {str(entry['correction_point']):<5} Location: {str(entry['location']):<10} Wallet: {str(entry['wallet']):<10}")
