# myapp/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'myapp/home.html')  # Render the home template
