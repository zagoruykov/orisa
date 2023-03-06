from rest_framework import viewsets
from .serializers import SightSerializer
from .models import Sight
from rest_framework import viewsets

from .models import Sight
from .serializers import SightSerializer


class SightsViewSet(viewsets.ModelViewSet):
    serializer_class = SightSerializer
    queryset = Sight.objects.all()
