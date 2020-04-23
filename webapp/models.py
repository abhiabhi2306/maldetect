from django.db import models



class MalUrl(models.Model):
    url = models.CharField(max_length=120)
   
