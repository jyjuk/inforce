from django.urls import path
from . import views

urlpatterns = [
    path("", views.RestaurantCreateView.as_view(), name="restaurant-create"),
    path("menu/", views.MenuUploadView.as_view(), name="menu-upload"),
    path("menu/today/", views.TodayMenuListView.as_view(), name="menu-today"),
]
