from rest_framework.generics import ListAPIView
from backend.demo.models import Demo
from .serializers import DemoSerializer


class DemoListView(ListAPIView):
    queryset = Demo.objects.all()
    serializer_class = DemoSerializer
