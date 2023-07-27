from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import MyModel


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def my_models_index(request):
    my_models = MyModel.objects.all()
    return render(request, 'my_models/index.html',{
        'my_models' : my_models
    })

def my_models_detail(request, my_model_id):
    my_model=MyModel.objects.get(id=my_model_id)
    return render(request, 'my_models/detail.html',{
        'my_model' : my_model
    })

class MyModelCreate(CreateView):
    model = MyModel
    fields = '__all__'

class MyModelUpdate(UpdateView):
    model = MyModel
    fields = ['brand', 'line']

class MyModelDelete(DeleteView):
    model = MyModel
    success_url = '/my_models'