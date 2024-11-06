"""
URL configuration for charity_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    # path('header/',views.header),
    path('home/',views.home),
    path('base/',views.base),
    path('index/',views.index),
    path('who_are_we/',views.who_are_we),
    path('what_we_do/',views.what_we_do),
############################################
    path('register/',views.registration),
    path('register/<did>/',views.registration_ngo),
############################################
    path('login/',views.ulogin),
    path('logout/',views.ulogout),
    path('fpass/',views.fpass),
    
    path('user_profile/',views.user_profile),
    path('update_pass/',views.update_pass),
    path('ngo_login/',views.nlogin),
    path('ngo_logout/',views.nlogout),
    path('contact/',views.contact),
    path('admin_pannel/',views.admin_pannel),
    path('dashboard_ngo/',views.dashboard_ngo),
    path('dashboard_user/',views.dashboard_user),

###########################################################
    path('make_donations/',views.make_donations),
    path('donate/<nid>/',views.donate),
    path('donations_made/',views.donations_made),
    # path('dashboard_user/<sid>/',views.dashboard_user_show),
    # path('dashboard_user/<mid>/',views.dashboard_user_make),
####################################################################
    path('initiate-payment/<nid>/', views.initiate_payment, name='initiate_payment'),
    path('verify-payment/', views.verify_payment, name='verify_payment'),
    # path('money_donate/<uid>/',views.money_donate_upi),
    # path('money_donate/<cid>/',views.money_donate_card),
    # path('money_donate/<qid>/',views.money_donate_qr),
####################################################################
    path('daily_donate/<nid>/',views.daily_donate),
    path('food_donate/<nid>/',views.food_donate),
    # path('daily_donate/<cid>/',views.daily_donate_cloths),
    # path('daily_donate/<bid>/',views.daily_donate_blanket),
    # path('daily_donate/<fid>/',views.daily_donate_blanket),
    # path('daily_donate/<pid>/',views.daily_donate_blanket),
####################################################################
    
    # path('food_donate/<aid>/',views.food_donate_pickup),
#####################################################################
    # path('money_show/',views.money_show),
    # path('daily_show/',views.daily_show),
    # path('food_show/',views.food_show),
#####################################################################
    path('ngo_login/',views.ngo_login),
    path('ngo_profile/',views.ngo_profile),
    path('new_ngo/',views.new_ngo),
    path('ngos_connected/',views.ngos_connected),
    path('ngo_detail/<nid>/',views.ngo_detail),
    path('ngo_connect/<nid>/',views.ngo_connect),
#####################################################################
###    NGO paths
    # path('ngo_donations/',views.ngo_donation), #Total Donations Made
    path('donor_connected/',views.donor_connected),
    
    path('to_be_received/',views.to_be_received),
    path('to_be_received_Ufood/<did>/',views.to_be_received_food),
    path('to_be_received_Udaily/<did>/',views.to_be_received_daily),
    
    path('donation_request/',views.donation_request),
    path('donation_request_Ufood/<did>/',views.donation_request_update_food),
    path('donation_request_Udaily/<did>/',views.donation_request_update_daily),
    
    path('donation_received/',views.donations_received),
    path('rejected/',views.donations_rejected),
    path('work_done/',views.work_done),
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)