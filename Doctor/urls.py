from django.urls import path
from . import views

urlpatterns = [
    path('doctorlogin/', views.doctorlogin, name="DoctorLogin"),
    path('doctorsingup/', views.doctorsingup, name="DoctorSingup"),
    path('doctordashboard/', views.doctordashboard, name="DoctorDashboard"),
    path('doctorprofile/', views.doctorprofile, name="DoctorProfile"),
    path('doctoruserlogin/', views.doctoruserlogin, name="DoctorUserLogin"),
    path('userotpverification/', views.userotpverification, name="UserOtpVerification"),
    path('doctormainpage/', views.doctormainpage, name="DoctorMainPage"),
    path('doctoraccessdata/', views.doctoraccessdata, name="DoctorAccessData"),
    path('duserhealthdata/', views.duserhealthdata, name="DUserHealthData"),
    path('dedituserdata', views.dedituserdata, name="DEditUserData"),
    path('deditsuccess/', views.deditsuccess, name="DEditSuccess"), 
    path('dprescription', views.dprescription, name="DPrescription"),
    path('dprescriptionsuccess', views.dprescriptionsuccess, name="DPrescriptionSuccess"),
    path('ddiagnostic/', views.ddiagnostic, name="DDiagnostic"),
    path('doctorlogout/', views.doctorlogout, name="DLogout"),
    path('doctorctscan2d/', views.doctorctscan2d, name="DCTScan2D"),
    path('doctorctscan3d/', views.doctorctscan3d, name="DCTScan3D")
]