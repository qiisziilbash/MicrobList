from django.urls import path

from apps.accounts import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/sign_in/', views.sign_in, name='login'),
    path('accounts/sign_out/', views.sign_out, name='logout'),
    path('accounts/sign_up/', views.sign_up, name='forgot'),
    path('accounts/reset/', views.reset, name='reset'),
    path('accounts/forgot/', views.forgot, name='reset'),
]