from django.shortcuts import render
#
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
#
from django.views.generic import (
    View,
    ListView,
    DeleteView
)

from applications.job_offers.models import Job

#
from .models import Favorites


class UserPageView(LoginRequiredMixin, ListView):
    template_name = "favoritos/perfil_new.html"
    context_object_name = 'entradas_user'
    login_url = reverse_lazy('users_app:user-login')

    def get_queryset(self):
        return Favorites.objects.jobs_user(self.request.user)


class AddFavoritosView(LoginRequiredMixin, View):
    login_url = reverse_lazy('users_app:user-login')

    def post(self, request, *args, **kwargs):
        # recuperar el usuario
        usuario = self.request.user
        job = Job.objects.get(id=self.kwargs['pk'])
        # registramos favorito
        try:
            Favorites.objects.create(
                user=usuario,
                job=job,
            )
        except:
            pass

        return HttpResponseRedirect(
            reverse(
                'favoritos_app:perfil',
            )
        )



class FavoritesDeleteView(DeleteView):
    model = Favorites
    success_url = reverse_lazy('favoritos_app:perfil')