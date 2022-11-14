from django.db import models

# Create your models here.


class Job(models.Model):
    SEX = [("Presencial", "Presencial"),
           ("Hibrido", "Hibrido"),
           ("Remoto", "Remoto")]
    title = models.CharField("titulo", max_length=200)
    date_publish = models.DateField()
    salary = models.CharField("Salario", max_length=50)
    description = models.CharField("Descripcion", max_length=900)
    company = models.CharField("Empresa", max_length=50, default="")
    type = models.CharField("Tipo", max_length=50)
    url_postulation = models.URLField()
    location = models.CharField("Ubacion", max_length=100, default="")

    def __str__(self):
        return self.title
