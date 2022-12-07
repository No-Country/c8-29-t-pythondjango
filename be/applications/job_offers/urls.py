from django.urls import path
from .views import Index, Results, EmployeesByKword, DetailJob, Contact, About, Blog

app_name = "job_app"

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('contact', Contact.as_view(), name='about'),
    path('about', About.as_view(), name='contact'),
    path('blog', Blog.as_view(), name='blog'),
    path('results', EmployeesByKword.as_view(), name='results'),
    path('results/detail/<int:pk>', DetailJob.as_view(), name='detail'),

]
