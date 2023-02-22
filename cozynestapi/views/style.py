"""View module for handling requests about interior design styles"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from cozynestapi.models import Style

class StyleView(ViewSet):
    """CozyNest Style View"""

    def retrieve(self, request, pk):
        """Handle GET requests for single interior design style

        Returns:
            Response -- JSON serialized style
        """
        style = Style.objects.get(pk=pk)
        serializer = StyleSerializer(style)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all hair types

        Returns:
            Response -- JSON serialized list of hair types
        """
        styles = Style.objects.all()
        serializer = StyleSerializer(styles, many=True)
        styles_serialized = serializer.data
        for style in styles_serialized:
            style['value'] = style.pop('id')
            style['label'] = style.pop('style')
        return Response(serializer.data)

class StyleSerializer(serializers.ModelSerializer):
    """JSON serializer for style
    """
    class Meta:
        model = Style
        fields = ('id', 'style')
