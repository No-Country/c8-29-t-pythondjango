from django.db import models


class FavoritesManager(models.Manager):

    def jobs_user(self, usuario):
        return self.filter(
            user=usuario
        ).order_by('-created')

