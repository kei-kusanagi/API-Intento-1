from rest_framework import viewsets

from watchlist_app.api import serializers
from watchlist_app.models import StreamPlataform

class StreamPlataformVS(viewsets.ModelViewSet):

    queryset = StreamPlataform.objects.all()
    serializer_class = serializers.StreamPlataformSerializer
    