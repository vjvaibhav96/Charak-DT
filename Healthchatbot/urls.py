from django.urls import path
from . import views

urlpatterns = [
    path('', views.healthchatbot, name="HealthChatBot"),
]