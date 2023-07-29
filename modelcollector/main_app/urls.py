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
    path('my_models/<int:my_model_id>/add_pilot/', views.add_pilot, name='add_pilot'),

    path('my_models/<int:my_model_id>/assoc_accessory/<int:accessory_id>/', views.assoc_accessory, name='assoc_accessory'),
    path('my_models/<int:my_model_id>/unassoc_accessory/<int:accessory_id>/', views.unassoc_accessory, name='unassoc_accessory'),
    
    path('accessories/', views.AccessoryList.as_view(), name='accessories_index'),
    path('accessories/<int:pk>/', views.AccessoryDetail.as_view(), name='accessories_detail'),
    path('accessories/create/', views.AccessoryCreate.as_view(), name='accessories_create'),
    path('accessories/<int:pk>/update/', views.AccessoryUpdate.as_view(), name='accessories_update'),
    path('accessories/<int:pk>/delete/', views.AccessoryDelete.as_view(), name='accessories_delete'),
]