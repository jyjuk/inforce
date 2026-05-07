from rest_framework import serializers
from .models import Restaurant, Menu, MenuItem


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ("id", "name", "description", "price")


class MenuSerializer(serializers.ModelSerializer):
    items = MenuItemSerializer(many=True)

    class Meta:
        model = Menu
        fields = ("id", "restaurant", "date", "items")

    def create(self, validated_data):
        items_data = validated_data.pop("items")
        menu = Menu.objects.create(**validated_data)
        for item in items_data:
            MenuItem.objects.create(menu=menu, **item)
        return menu


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ("id", "name", "created_at")
        read_only_fields = ("created_at",)