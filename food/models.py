from django.db import models
from django.utils.html import format_html
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Food(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    published = models.DateTimeField(default=timezone.now)
    photo = models.ImageField(upload_to="food", null=True, blank=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    def photo_tag(self):
        return format_html(f"<img src='{self.photo.url}' width=100px height=100px")
