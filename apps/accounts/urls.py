from django.urls import path

from apps.accounts import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/sign_in/', views.sign_in, name='sign_in'),
    path('accounts/sign_out/', views.sign_out, name='sign_out'),
    path('accounts/sign_up/', views.sign_up, name='sign_up'),
    path('accounts/reset/', views.reset, name='reset'),
    path('accounts/forgot/', views.forgot, name='forgot'),
]