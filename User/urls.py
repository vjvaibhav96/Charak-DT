from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="UserHome"),
    path('userlogin/', views.userlogin, name="UserLogin"),
    path('userhome/', views.userhome, name="UserHome"),
    path('accesshealthdata/', views.accesshealthdata, name="AccessHealthData"),
    path('healthdata/', views.healthdata, name="HealthData"),
    path('edithealthdata/', views.edithealthdata, name="EditHealthData"),
    path('edithealthsuccess/', views.edithealthsuccess, name="EditHealthSuccess"),
    path('connectsmartphone/', views.connectsmartphone, name="ConnectSmartPhone"),
    path('diagnostictool/', views.diagnostictool, name="DiagnosticTool"),
    path('successconnect/', views.successconnect, name="SuccessConnect"),
    path('userlogout/', views.userlogout, name="LogoutUser"),
    path('userprofile', views.userprofile, name="UserProfile"),
    path('edituserprofile', views.edituserprofile, name="EditUserProfile")
]