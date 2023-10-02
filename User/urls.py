from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="UserHome"),
    path('userlogin/', views.userlogin, name="UserLogin"),
    path('userhome/', views.userhome, name="UserHome"),
    path('accesshealthdata/', views.accesshealthdata, name="AccessHealthData"),
    path('healthdata/', views.healthdata, name="HealthData"),
    path('editvitalsings/', views.editvitalsings, name="EditHealthData"),
    path('editeatinghabits/', views.editeatinghabits, name="EditEatingHabits"),
    path('edithealthsuccess/', views.edithealthsuccess, name="EditHealthSuccess"),
    path('addcredentials/', views.addcredentials, name="AddCredentials"),
    path('connectsmartphone/', views.connectsmartphone, name="ConnectSmartPhone"),
    path('diabetesprediction/', views.diabetesprediction, name="DiabetesPrediction"),
    path('hearthealthprediction/', views.hearthealthprediction, name="HeartHealthPrediction"),
    path('successconnect/', views.successconnect, name="SuccessConnect"),
    path('userlogout/', views.userlogout, name="LogoutUser"),
    path('userprofile', views.userprofile, name="UserProfile"),
    path('edituserprofile', views.edituserprofile, name="EditUserProfile"),
    path('edithealthconditions', views.edithealthconditions, name="EditHealthConditions"),
    path('editfeeltoday', views.editfeeltoday, name="EditFeelToday"),
    path('editregularmedications', views.editregularmedications, name="EditRegularMedications"),
    path('editexercisedata', views.editexercisedata, name="EditExcerciseData"),
    path('editeatinghabitsother', views.editeatinghabitsother, name="EditEatingHabitsOther"),
    path('uploadprescription', views.uploadprescription, name="UploadPrescription"),
    path('viewprescription', views.viewprescription, name="ViewPrescription"),
    path('iglu', views.iglu, name="iGLU"),
    path('igluaccessdata', views.igluaccessdata, name="iGLUAccessData"),
    path('iframe2d', views.iframe2d, name="IFrame2D")
    # path('iframe3d', views.iframe3d, name="IFrame2D")
]