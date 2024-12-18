# myapp/views.py
from django.shortcuts import render
from .api_service import fetch_users, get42, post42 # Import the fetch_users function

def user_list(request):
    users = fetch_users()  # Fetch the users using the API
    return render(request, 'myapp/user_list.html', {'users': users})
def home(request):
    return render(request, 'myapp/home.html')  # Render the home template
