from django.urls import path
from . import views

urlpatterns = [ # Default home page
    path('', views.user_list, name='user_list'),
    path('', views.home, name='home'),  # New page for 42 users
]
