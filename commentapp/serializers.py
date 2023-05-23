from rest_framework import serializers
from .models import CommentApp

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentApp
        # fields = ['id', 'title', 'author', 'isbn', 'publisher']
        fields='__all__'
