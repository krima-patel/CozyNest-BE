"""View module for handling requests about routines"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from cozynestapi.models import Piece, PieceStyle, User

class PieceStyleView(ViewSet):
    """CozyNest Piece Style View"""

    def retrieve(self, request, pk):
        """Handle GET requests for single piece style

        Returns:
            Response -- JSON serialized piece style
        """
        piece_style = PieceStyle.objects.get(pk=pk)
        serializer = PieceStyleSerializer(piece_style)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all piece styles

        Returns:
            Response -- JSON serialized list of piece styles
        """
        piece_styles = PieceStyle.objects.all()
        serializer = PieceStyleSerializer(piece_styles, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Creating styles for pieces - multi-select"""
        user = User.objects.get(pk=request.data["user"])

        piece_styles=PieceStyle.objects.create(
            piece=Piece.objects.get(pk=request.data["piece_id"]),
            style=request.data["style"]
        )
        serializer = PieceStyleSerializer(piece_styles)
        return Response(serializer.data)

    def destroy(self, request, pk):
        """Deleting a style(s) for a piece"""
        piece_style=PieceStyle.objects.get(pk=pk)
        piece_style.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class PieceStyleSerializer(serializers.ModelSerializer):
    """JSON serializer for piece styles
    """
    class Meta:
        model = PieceStyle
        fields = ('id', 'piece', 'style')
        depth = 1
