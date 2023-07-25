from django.shortcuts import render

my_models = [
{
'brand': 'Bandai',
'line' : ' HG Gunpla',
'name' : 'Heavyarms',
},

{
'brand' : 'Bandai',
'line' : 'Spirits',
'name' : 'Mandalorian Razor Crest',
},
{
'brand' : 'Aoshima',
'line' : 'Initial D',
'name' : "Takumi Fujiwara's AE86 Trueno",
},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def my_models_index(request):
    return render(request, 'my_models/index.html',{
        'my_models' : my_models
    })