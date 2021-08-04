from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=120)
    qiantity = models.PositiveSmallIntegerField(default=12)

