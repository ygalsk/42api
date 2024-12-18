from django.conf import settings
import requests

def post42(url, payload):
    url = "https://api.intra.42.fr" + url
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.post(url, headers=headers, data=payload)
    return response.json()

def get42(url, payload):
    url = "https://api.intra.42.fr" + url
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.get(url, headers=headers, data=payload)
    return response.json()

def fetch_users():
    wtoken = post42("/oauth/token", {
        "grant_type": "client_credentials", 
        "client_id": settings.SOCIAL_AUTH_42_KEY, 
        "client_secret": settings.SOCIAL_AUTH_42_SECRET
    })
    
    campus_users = []
    campus_users_total = get42('/v2/campus/1', {"access_token": wtoken["access_token"]})
    total_users = campus_users_total.get("users_count", 0)
    total_pages = (total_users // 100 + 1) + 1

    for i in range(1, total_pages):  
        campus_users += get42(f"/v2/campus/1/users?page[number]={i}&page[size]=100", {"access_token": wtoken["access_token"]})

    users = []
    for user in campus_users:
        users.append({
            "login": user.get("login"),
            "correction_point": user.get("correction_point"),
            "pool_year": user.get("pool_year"),
            "location": user.get("location"),
            "updated_at": user.get("updated_at").split("T")[1].split(".")[0],
            "wallet": user.get("wallet")
        })
    return users