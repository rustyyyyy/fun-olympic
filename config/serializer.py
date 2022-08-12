from rest_framework import serializers


class StaticImageSerializer(serializers.Serializer):
    image = serializers.ImageField()
