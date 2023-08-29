from django.urls import path
from . import views

urlpatterns = [
    path("", views.FoodPage.as_view(), name="home_page"),
    path("<int:pk>/", views.FoodDetail.as_view(), name="detail_page"),
]
