from django.urls import path
from .api import JobApiView

urlpatterns = [
    path('add-job', JobApiView.as_view(), name='add-job'),
]
