from django.http import HttpResponseRedirect
from django.template.loader import get_template
from django.urls import reverse
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Alert
from applications.job_offers.models import Job
# Create your views here.


class AddAlertView(LoginRequiredMixin,View):
    def post(self, request, *args, **kwargs):
        # recuperar el usuario
        usuario = self.request.user
        print(self.kwargs['pk'])
        alert_text = Job.objects.get(id=self.kwargs['pk'])

        print(alert_text)
        # registramos favorito
        Alert.objects.create(
            user=usuario,
            alert_text=alert_text.title,
            periodicity="Diario"
        )

        return HttpResponseRedirect(
            reverse(
                'favoritos_app:perfil',
            )
        )


def send_user_mail(user,name):
    import smtplib
    email_address = 'aliria.gutierrez@yahoo.com'  # add email address here
    Subject = 'Subject: Bievenido...\n\n'
    content = f' Dear {name}, \n This is a test message.\n\n '
    footer = '- Test'  # add test footer
    passcode = 'paondxrldheavnlz'  # add passcode here
    conn = smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465)
    conn.ehlo()
    conn.login(email_address, passcode)
    conn.sendmail(email_address,
                  user,
                  Subject + content + footer)
    conn.quit()