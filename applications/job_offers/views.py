from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Job


class Index(TemplateView):
    template_name = "index.html"


class Results(ListView):
    template_name = 'results.html'
    model = Job

class EmployeesByKword(ListView):
    """  lista empelado por palabra clave """
    template_name = 'results.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        print('********************')
        palabra_clave = self.request.GET.get("kword", '')
        sort_qery = self.request.GET.get("sort", '')
        salary_qery = self.request.GET.get("salary", '')

        if sort_qery == "date":
            lista = Job.objects.filter(
                Q(title__icontains=palabra_clave) | Q(description__icontains=palabra_clave)
            ).order_by("date_publish")
            return lista
        if salary_qery == "salary":
            lista = Job.objects.filter(
                Q(title__icontains=palabra_clave) | Q(description__icontains=palabra_clave)
            ).order_by("salary")
            return lista
        else:

            lista = Job.objects.filter(
                Q(title__icontains=palabra_clave)| Q(description__icontains=palabra_clave)
            )
            return lista

# Create your views here.

class DetailJob(DetailView):
    template_name = 'detail.html'
    context_object_name = 'detail'
    model = Job
