from django.urls import path
from . import views

urlpatterns = [
    path('', views.doctorlogin, name='DoctorLogin'),
    path('doctorsingup/', views.doctorsingup, name="DoctorSingup"),
    path('doctoruserlogin/', views.doctoruserlogin, name="DoctorUserLogin"),
    path('userotpverification/', views.userotpverification, name="UserOtpVerification"),
    path('doctormainpage/', views.doctormainpage, name="DoctorMainPage"),
    path('doctoraccessdata/', views.doctoraccessdata, name="DoctorAccessData"),
    path('duserhealthdata/', views.duserhealthdata, name="DUserHealthData"),
    path('dedituserdata', views.dedituserdata, name="DEditUserData"),
    path('deditsuccess/', views.deditsuccess, name="DEditSuccess"), 
    path('dprescription', views.dprescription, name="DPrescription"),
    path('dprescriptionsuccess', views.dprescriptionsuccess, name="DPrescriptionSuccess"),
    path('ddiagnostic/', views.ddiagnostic, name="DDiagnostic")
]