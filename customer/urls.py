from django.urls import path
from .views import customer_list
from .views import register, user_login, user_logout
urlpatterns = [
    path('customers/', customer_list, name='customer_list'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
