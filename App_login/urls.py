from django.urls import path
from App_login import views

app_name = 'App_login'


urlpatterns = [
    path('signup/', views.registrations_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_views, name='logout'),
    path('my-profile/', views.my_profile, name='my-profile'),
    path('profile-settings/', views.profile_settings, name='profile-settings'),
    path('contact/', views.contact_sys, name='contact'),
    path('about/', views.about_views, name='about'),
    path('my_chats/', views.my_chats, name='my_chats'),
]

