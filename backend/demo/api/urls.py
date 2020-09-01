from django.urls import path
from .views import DemoListView

urlpatterns = [path('', DemoListView.as_view())]
