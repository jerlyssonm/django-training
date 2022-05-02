from rest_framework import serializers


class CommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField()
    content = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)