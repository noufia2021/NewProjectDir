from django.db import models


# Create your models here.
class links(models.Model):
    address_link = models.CharField(max_length=500, null=True, blank=True)
    name_link = models.CharField(max_length=500, null=True, blank=True)
    def __str__(self):
        return self.name_link


