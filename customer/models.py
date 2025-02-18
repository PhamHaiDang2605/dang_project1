from django.db import models
from django.contrib.auth.models import AbstractUser

class Customer(AbstractUser):  # Kế thừa AbstractUser để dùng hệ thống auth của Django
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.username  # username là mặc định trong AbstractUser
