from rest_framework import serializers


class AlbumSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    #musician = MusicianSerializer(read_only=True)

class MusicianSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    instrument = serializers.CharField()
    albums = AlbumSerializer(many=True, read_only=True)

    #poderia ser no albumserializer com o campo de musician