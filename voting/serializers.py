from rest_framework import serializers


class VoteInputSerializer(serializers.Serializer):
    menu_id = serializers.IntegerField()


class MenuResultSerializer(serializers.Serializer):
    restaurant = serializers.CharField(source="restaurant.name")
    menu_id = serializers.IntegerField(source="id")
    votes = serializers.IntegerField(source="vote_count")
