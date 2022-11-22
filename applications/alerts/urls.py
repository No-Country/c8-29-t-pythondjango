from django.urls import path
from . import views

app_name = "alerts_app"

urlpatterns = [
    path(
        'add-alert/<pk>/',
        views.AddAlertView.as_view(),
        name='add-alert',
    )
]
