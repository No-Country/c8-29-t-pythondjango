from django.db import models

# Create your models here.


class Job(models.Model):
    TYPE = [("Presencial", "Presencial"),
           ("Hibrido", "Hibrido"),
           ("Remoto", "Remoto")]
    title = models.CharField("titulo", max_length=200)
    date_publish = models.DateField()
    subtitulo = models.CharField(max_length=100)
    sub_subtitulo = models.CharField(max_length=100)
    salary = models.CharField("Salario", max_length=50)
    description = models.CharField("Descripcion", max_length=10000)
    company = models.CharField("Empresa", max_length=50, default="")
    type = models.CharField("Tipo", max_length=50, choices=TYPE)
    url_postulation = models.URLField(max_length=5000)
    location = models.CharField("Ubacion", max_length=100, default="")

    def __str__(self):
        return self.title
