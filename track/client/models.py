from django.db import models

class Post(models.Model):
    titel=models.CharField(max_length=200)
    desc=models.CharField(max_length=500)
