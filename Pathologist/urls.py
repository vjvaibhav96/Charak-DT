from django.urls import path
from . import views

urlpatterns = [
    path('pathologin/', views.pathologin, name="PathoLogin"),
    path('pathohomepage', views.pathohomepage, name="PathoHomePage"),
    path('pathodashboard', views.pathodashboard, name="PathoDashboard"),
    path('pathoprofile', views.pathoprofile, name="PathoProfile"),
    path('pathouserlogin', views.pathouserlogin, name="PathoUserLogin"),
    path('pathouserotp', views.pathouserotp, name="PathoUserOtp"),
    path('pathoaccess/', views.pathoaccess, name="PathoAccess"),
    path('pathouserdata', views.pathouserdata, name="PathoUserData"),
    path('pathoedit', views.pathoedit, name="PathoEdit"),
    path('pathoeditsuccess', views.pathoeditsuccess, name="PathoEditSuccess"),
    path('pathsingup/', views.pathosingup, name="PathoSingup"),
    path('pathesiofy/', views.pathoesiofy, name="PathoEsiofy"),
    path('pathologout/', views.pathologout, name="PathoLogout"),
    # path('pathotodoctorpres', views.pathotodoctorpres, name="PathoToDoctorPres"),
    # path('pathotodocsuccess', views.pathotodocsuccess, name="PathoToDocSuccess"),
]