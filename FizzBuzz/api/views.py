from rest_framework import viewsets
from .serializers import FizzSerializer
from .models import FizzModel

class FizzViewSet(viewsets.ModelViewSet):
    queryset = FizzModel.objects.all()
    serializer_class = FizzSerializer
    
    def perform_create(self, serializer):
        serializer.save(useragent = self.request.META['HTTP_USER_AGENT'])