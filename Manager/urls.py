from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name="ManagerHome"),
    path('signup/', views.signup, name="ManagerSignup"),
    path('managerlogin/', views.managerlogin, name="ManagerLogin"),
    path('attributes/', views.attributes, name="ManagerAttributes"),
    path('prediction/', views.prediction, name="ManagerPrediction"),
    path('managerhome/', views.manager_home, name="ManagerHome"),
    path('managerlogout/', views.logout, name="ManagerLogout"),
    path('managersingupsuccess/', views.managersingupsuccess, name="ManagerSingupSuccess")
]