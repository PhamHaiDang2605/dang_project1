from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)  # Thêm trường description
    photo = models.ImageField(upload_to='book_photos/', null=True, blank=True)

    def is_available(self):
        return self.stock > 0

    def __str__(self):
        return self.title
