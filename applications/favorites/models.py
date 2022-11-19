from django.db import models
from django.conf import settings

# apps de terceros
from model_utils.models import TimeStampedModel

#
from applications.job_offers.models import Job

#
from .managers import FavoritesManager


class Favorites(TimeStampedModel):
    """ Modelo para favotios """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='user_favorites',
        on_delete=models.CASCADE,
    )
    job = models.ForeignKey(
        Job,
        related_name='jobs_favorites',
        on_delete=models.CASCADE
    )

    objects = FavoritesManager()

    class Meta:
        unique_together = ('user', 'job')
        verbose_name = 'Trabajo Favorito'
        verbose_name_plural = 'Trabajos Favoritos'

    def __str__(self):
        return self.job.title