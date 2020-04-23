from django.urls import path

from . import views

urlpatterns = [
    path('', views.malurl_form, name='index'),
]
