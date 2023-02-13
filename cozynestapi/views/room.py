"""View module for handling requests about rooms"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from cozynestapi.models import Room, User

class RoomView(ViewSet):
    """CozyNest Rooms View"""

    def retrieve(self, request, pk):
        """Handle GET requests for a single room

        Returns:
            Response -- JSON serialized room
        """
        # room = Room.objects.get(pk=pk)
        # serializer = RoomSerializer(room)
        # return Response(serializer.data)
        try:
            room = Room.objects.get(pk=pk)
            serializer = RoomSerializer(room)
            return Response(serializer.data)
        except Room.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all rooms

        Returns:
            Response -- JSON serialized list of rooms
        """
        rooms = Room.objects.all()

        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized room instance
        """
        user = User.objects.get(pk=request.data["user"])

        room = Room.objects.create(
            name=request.data["name"],
            purpose=request.data["purpose"],
            theme=request.data["theme"],
            mood=request.data["mood"],
            deadline=request.data["deadline"],
            user=user
        )
        serializer = RoomSerializer(room)
        return Response(serializer.data)

class RoomSerializer(serializers.ModelSerializer):
    """JSON serializer for rooms"""
    class Meta:
        model = Room
        fields = ('id', 'name', 'purpose', 'theme', 'mood', 'deadline', 'user')
        depth = 1
