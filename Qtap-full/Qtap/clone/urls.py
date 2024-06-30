
from django.urls import path
from . import views

urlpatterns = [
    path('',views.register, name='register'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('edit-profile/<str:nickname>/', views.user_profile, name='edit_profile'),
    path('profile/<str:nickname>/', views.profile_view, name='profile_view'),
    path('generate-qr-code/<str:nickname>/', views.generate_qr_code_view, name='generate_qr_code'),
]

