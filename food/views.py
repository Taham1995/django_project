from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Food
# Create your views here.


class FoodPage(ListView):
    model = Food
    template_name = "index.html"
    context_object_name = "foods"


class FoodDetail(DetailView):
    model = Food
    template_name = "about.html"
    context_object_name = "detail"
