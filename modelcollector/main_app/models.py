from django.db import models
from django.urls import reverse
# Create your models here.
class MyModel(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    line = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={"my_model_id": self.id})
