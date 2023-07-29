from django.contrib import admin
from.models import MyModel, Pilot, Accessory

# Register your models here.
admin.site.register(MyModel)
admin.site.register(Pilot)
admin.site.register(Accessory)