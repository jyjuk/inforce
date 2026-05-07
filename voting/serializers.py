from rest_framework import serializers


class MenuResultSerializer(serializers.Serializer):
    restaurant = serializers.CharField(source="restaurant.name")
    menu_id = serializers.IntegerField(source="id")
    votes = serializers.IntegerField(source="vote_count")
