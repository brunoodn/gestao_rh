from django.urls import path
from .views import HoraExtraList

urlpatterns = [
    path('novo/',HoraExtraList.as_view() , name='list_hora_extra')
]