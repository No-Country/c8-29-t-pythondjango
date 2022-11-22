from django.db import models
from django.conf import settings

# Create your models here.


class Alert(models.Model):
    PERIODICITY_OPTIONS = [("Diario", "Diario"),
            ("Semanal", "Semanal"),]
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='user_alert',
        on_delete=models.CASCADE,
    )
    alert_text = models.CharField('Alerta', max_length=100)
    periodicity = models.CharField(
        max_length=10,
        choices=PERIODICITY_OPTIONS,
        blank=True
    )

