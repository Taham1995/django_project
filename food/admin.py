from django.contrib import admin
from .models import Food
# Register your models here.


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ["photo_tag", "name", "price"]
    list_editable = ["price",]
    list_filter = ["name", "price"]
