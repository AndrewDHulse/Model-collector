from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import MyModel, Accessory
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
    id_list= my_model.accessories.all().values_list('id')
    accessories_my_model_doesnt_have=Accessory.objects.exclude(id__in=id_list)
    pilot_form = PilotForm()
    return render(request, 'my_models/detail.html',{
        'my_model' : my_model,
        'pilot_form' : pilot_form,
        'accessories' : accessories_my_model_doesnt_have
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

class AccessoryList(ListView):
    model = Accessory

class AccessoryDetail(DetailView):
    model = Accessory

class AccessoryCreate(CreateView):
    model = Accessory
    fields = '__all__'

class AccessoryUpdate(UpdateView):
    model = Accessory
    fields = ['name']

class AccessoryDelete(DeleteView):
    model = Accessory
    success_url = '/accessories'

def assoc_accessory(request, my_model_id, accessory_id):
    MyModel.objects.get(id=my_model_id).accessories.add(accessory_id)
    return redirect('detail', my_model_id=my_model_id)

def unassoc_accessory(request, my_model_id, accessory_id):
    MyModel.objects.get(id=my_model_id).accessories.remove(accessory_id)
    return redirect('detail', my_model_id=my_model_id)