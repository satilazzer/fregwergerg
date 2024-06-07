from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('checkout/<int:car_id>', views.checkout, name = "checkout"),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('details/<int:car_id>', views.details, name = 'details'),
    path('high_low/', views.high_low, name = 'high_low'),
    path('low_high/', views.low_high, name='low_high')
]
