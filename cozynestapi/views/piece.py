"""View module for handling requests about pieces/items"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from cozynestapi.models import Piece

class PieceView(ViewSet):
    """CozyNest Pieces View"""

    def retrieve(self, request, pk):
        """Handle GET requests for single piece

        Returns:
            Response -- JSON serialized piece
        """

        # piece = Piece.objects.get(pk=pk)
        # serializer = PieceSerializer(piece)
        # return Response(serializer.data)

        try:
            piece = Piece.objects.get(pk=pk)
            serializer = PieceSerializer(piece)
            return Response(serializer.data)
        except Piece.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all pieces

        Returns:
            Response -- JSON serialized list of pieces
        """
        pieces = Piece.objects.all()
        serializer = PieceSerializer(pieces, many=True)
        return Response(serializer.data)

class PieceSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Piece
        fields = ('id', 'room', 'piece_type', 'image_url', 'source', 'condition', 'user')
        depth = 1
