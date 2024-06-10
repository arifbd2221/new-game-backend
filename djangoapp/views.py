# views.py
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import GameScore
from .serializers import PlayerSerializer, GameScoreSerializer, LeaderboardSerializer

class PlayerCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GameScoreCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = GameScoreSerializer(data=request.data)
        if serializer.is_valid():
            player = serializer.validated_data['player']
            incoming_score = serializer.validated_data['score']
            
            # Check if the GameScore already exists for the player
            try:
                game_score = GameScore.objects.get(player=player)
                if incoming_score > game_score.score:
                    game_score.score = incoming_score
                    game_score.save()
                    return Response({'message': 'GameScore updated successfully', 'score': game_score.score}, status=status.HTTP_200_OK)
                else:
                    return Response({'message': 'Incoming score is not higher than existing score', 'score': game_score.score}, status=status.HTTP_200_OK)
            except GameScore.DoesNotExist:
                # Create new GameScore if it does not exist
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
                
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GameScoreListView(generics.ListAPIView):
    queryset = GameScore.objects.all().order_by("-score", 'updated_at')
    serializer_class = LeaderboardSerializer