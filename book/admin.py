from django.contrib import admin
from django.utils.html import format_html
from .models import Book

# Đăng ký model với admin
admin.site.register(Book)
