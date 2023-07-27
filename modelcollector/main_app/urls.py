from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('my_models/', views.my_models_index, name='index'),
    path('my_models/<int:my_model_id>', views.my_models_detail, name='detail'),
    path('my_models/create/', views.MyModelCreate.as_view(), name='my_models_create'),
    path('my_models/<int:pk>/update/', views.MyModelUpdate.as_view(), name='mymodel_update'),
    path('my_models/<int:pk>/delete/', views.MyModelDelete.as_view(), name='mymodel_delete'),
]