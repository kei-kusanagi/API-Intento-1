from rest_framework import serializers
from watchlist_app.models import StreamPlataform

class StreamPlataformSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamPlataform
        fields = "__all__"