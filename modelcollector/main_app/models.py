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
    
    def has_pilot(self):
        return self.pilot_set.exists()

class Pilot(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    home = models.CharField(max_length=100)
    my_model=models.ForeignKey(
        MyModel,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.get_pilot_display()} is ready for action"
    
    class Meta:
        ordering = ['-age']