from tabnanny import verbose
from unicodedata import name
from django.db import models

class City(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        ordering = ['name']

    def __str__(self):
        return self.name