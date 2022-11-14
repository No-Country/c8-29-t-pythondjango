from django.urls import path
from .views import Index, Results, EmployeesByKword, DetailJob



urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('results', EmployeesByKword.as_view(), name='results'),
    path('results/detail/<int:pk>', DetailJob.as_view(), name='detail'),

]
