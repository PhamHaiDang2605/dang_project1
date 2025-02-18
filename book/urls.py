from django.urls import path
from .views import book_list,book_detail
from . import views
urlpatterns = [
    path('books/', book_list, name='book_list'),
    path('books/<int:book_id>/', book_detail, name='book_detail'),
    path('', views.book_list, name='book_list'),
    path('<int:book_id>/', views.book_detail, name='book_detail'),  # URL cho chi tiết sách
]
