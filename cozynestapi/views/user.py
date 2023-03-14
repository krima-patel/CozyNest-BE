"""View module for handling requests for users"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from cozynestapi.models import User


class UserView(ViewSet):
    """CozyNest Users View"""

    def retrieve(self, request, pk):
        """Handle GET requests for a single user

        Returns:
            Response -- JSON serialized user
        """

        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all users
        Returns:
          Response -- JSON serialized list of users
        """

        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for users"""
    class Meta:
        model = User
        fields = ('id', 'uid', 'name', 'bio', 'image')
