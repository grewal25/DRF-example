from rest_framework import serializers

class PostSerializers(serializers.Serializer):
    topic = serializers.CharField(max_length = 40)
    author = serializers.CharField(max_length = 40)
    body = serializers.CharField()
