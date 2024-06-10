from rest_framework import serializers
from .models import Player, GameScore

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ["id",'name', 'email', 'phone', 'profile_pic_id']


class GameScoreSerializer(serializers.ModelSerializer):
    player = serializers.PrimaryKeyRelatedField(queryset=Player.objects.all())

    class Meta:
        model = GameScore
        fields = ['player', 'score', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class LeaderboardSerializer(serializers.ModelSerializer):
    player = PlayerSerializer()

    class Meta:
        model = GameScore
        fields = ['player', 'score',]