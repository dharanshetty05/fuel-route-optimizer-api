from rest_framework import serializers


class RouteRequestSerializer(serializers.Serializer):
    start_lat = serializers.FloatField()
    start_lng = serializers.FloatField()
    end_lat = serializers.FloatField()
    end_lng = serializers.FloatField()