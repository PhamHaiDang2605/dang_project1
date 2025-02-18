"""
URL configuration for dang_project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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


from .views import home
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import custom_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Trang chủ
    path('', include('customer.urls')),  # Đưa đường dẫn customer vào project
    path('',include('book.urls')),
    path('', include('cart.urls')),
    path('books/', include('book.urls')),
    path('customers/', include('customer.urls')),
    path('', home, name='home'),
    path('login/', custom_login, name='login'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)