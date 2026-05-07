from rest_framework import generics, permissions
from .models import Restaurant
from .serializers import RestaurantSerializer, MenuSerializer
from . import services


class RestaurantCreateView(generics.CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = (permissions.IsAdminUser,)


class MenuUploadView(generics.CreateAPIView):
    serializer_class = MenuSerializer
    permission_classes = (permissions.IsAdminUser,)


class TodayMenuListView(generics.ListAPIView):
    serializer_class = MenuSerializer

    def get_queryset(self):
        return services.get_today_menus()