from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Job


class Index(TemplateView):
    template_name = "index_new.html"

class About(TemplateView):
    template_name = "home/about.html"

class Contact(TemplateView):
    template_name = "home/contact.html"

class Blog(TemplateView):
    template_name = "home/blog.html"


class Results(ListView):
    template_name = 'results_new.html'
    model = Job

class EmployeesByKword(ListView):
    """  lista empelado por palabra clave """
    template_name = 'results_new.html'
    context_object_name = 'empleados'
    paginate_by = 10

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        sort_qery = self.request.GET.get("sort", '')
        type_qery = self.request.GET.get("type", '')
        location_qery = self.request.GET.get("location", '')
        print(type_qery)
        print(palabra_clave)
        print(location_qery)
        print(sort_qery)


        if type_qery == "Todos" and sort_qery == "relevance":
            lista = Job.objects.filter(
                title__icontains=palabra_clave, location__icontains=location_qery)
            print("relevance todos")

            return lista

        if type_qery == "Todos" and sort_qery == "date":
            lista = Job.objects.filter(
                title__icontains=palabra_clave, location__icontains=location_qery).order_by("date_publish")
            print("date todos")

            return lista

        if type_qery == "Todos" and sort_qery == "salary":
            lista = Job.objects.filter(
                title__icontains=palabra_clave, location__icontains=location_qery).order_by("salary")
            print("salary todos")

            return lista

        if type_qery == "Presencial" and sort_qery == "relevance":
            lista = Job.objects.filter(
                title__icontains=palabra_clave, type__exact="Presencial", location__icontains=location_qery)
            print("presencial relevance")

            return lista

        if type_qery == "Presencial" and sort_qery == "date":
            lista = Job.objects.filter(
                title__icontains=palabra_clave, type__exact="Presencial", location__icontains=location_qery).order_by("date_publish")
            print("presencial date")

            return lista

        if type_qery == "Presencial" and sort_qery == "salary":
            lista = Job.objects.filter(
                title__icontains=palabra_clave, type__exact="Presencial", location__icontains=location_qery).order_by("salary")
            print("salary presencial")

            return lista

        if type_qery == "Remoto" and sort_qery == "relevance":
            lista = Job.objects.filter(
                title__icontains=palabra_clave, type__exact="Remoto", location__icontains=location_qery)
            print("Remoto relevance")

            return lista

        if type_qery == "Remoto" and sort_qery == "date":
            lista = Job.objects.filter(
                title__icontains=palabra_clave, type__exact="Remoto", location__icontains=location_qery).order_by(
                "date_publish")
            print("Remoto date")

            return lista

        if type_qery == "Remoto" and sort_qery == "salary":
            lista = Job.objects.filter(
                title__icontains=palabra_clave, type__exact="Remoto", location__icontains=location_qery).order_by(
                "salary")
            print("salary Remoto")

            return lista

        return Job.objects.all()






# Create your views here.

class DetailJob(DetailView):
    template_name = 'detail_new.html'
    context_object_name = 'detail'
    model = Job
