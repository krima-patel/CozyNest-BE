"""View module for handling requests about pieces/items"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from cozynestapi.models import Room, Piece, User, PieceStyle, Style
from .piece_style import PieceStyleSerializer

class PieceView(ViewSet):
    """CozyNest Pieces View"""

    def retrieve(self, request, pk):
        """Handle GET requests for single piece

        Returns:
            Response -- JSON serialized piece
        """
        piece = Piece.objects.get(pk=pk)
        designs = PieceStyle.objects.filter(piece=pk)
        designs_serialized = PieceStyleSerializer(designs, many=True)
        piece.designs = designs_serialized.data
        serializer = PieceSerializer(piece)
        return Response(serializer.data)

        # piece = Piece.objects.get(pk=pk)
        # serializer = PieceSerializer(piece)
        # return Response(serializer.data)

        # try:
        #     piece = Piece.objects.get(pk=pk)
        #     serializer = PieceSerializer(piece)
        #     return Response(serializer.data)
        # except Piece.DoesNotExist as ex:
        #     return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all pieces

        Returns:
            Response -- JSON serialized list of pieces
        """
        # pieces = Piece.objects.all()
        # serializer = PieceSerializer(pieces, many=True)
        # return Response(serializer.data)

        room_id = request.GET.get("room")

        if room_id:
            pieces = Piece.objects.filter(room_id=room_id)
            for piece in pieces:
                designs = PieceStyle.objects.filter(piece=piece.id)
                designs_serialized = PieceStyleSerializer(designs, many=True)
                piece.designs = designs_serialized.data
                serializer = PieceSerializer(pieces, many=True)
            return Response(serializer.data)
        else:
            pieces = Piece.objects.all()
            for piece in pieces:
                designs = PieceStyle.objects.filter(piece=piece.id)
                designs_serialized = PieceStyleSerializer(designs, many=True)
                piece.designs = designs_serialized.data
                serializer = PieceSerializer(pieces, many=True)
            return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized piece instance
        """
        styles=request.data["designs"]
        user = User.objects.get(pk=request.data["user"])

        piece = Piece.objects.create(
            room=Room.objects.get(pk=request.data["room_id"]),
            piece_type=request.data["piece_type"],
            image_url=request.data["image_url"],
            source=request.data["source"],
            condition=request.data["condition"],
            user=user
        )
        for style in styles:
            print(style)
            PieceStyle.objects.create(piece=piece, style=Style.objects.get(pk=style))
            serializer = PieceSerializer(piece)
        return Response(serializer.data)

class PieceSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Piece
        fields = ('id', 'room', 'piece_type', 'image_url', 'source', 'condition', 'user', 'designs')
        depth = 1
