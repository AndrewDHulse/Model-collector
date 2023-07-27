from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import MyModel
from .forms import PilotForm

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
    pilot_form = PilotForm()
    return render(request, 'my_models/detail.html',{
        'my_model' : my_model,
        'pilot_form' : pilot_form
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

def add_pilot(request, my_model_id):
    form=PilotForm(request.POST)
    if form.is_valid():
        new_pilot = form.save(commit=False)
        new_pilot.my_model_id = my_model_id
        new_pilot.save()
    return redirect('detail', my_model_id=my_model_id)