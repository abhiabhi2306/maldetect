from django.urls import path

from . import views


handler500 = 'webapp.views.handler500'


urlpatterns = [
    path('', views.malurl_form, name='index'),
]
