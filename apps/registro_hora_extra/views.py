from django.shortcuts import render
from .models import RegistroHoraExtra
# Create your views here.
from django.views.generic import CreateView, ListView


class HoraExtraList(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)
