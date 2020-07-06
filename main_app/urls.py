from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clothings/', views.clothings_index, name='index'),
    path('myclothings/', views.myclothings_index, name='myindex'),
    path('clothings/<int:clothing_id>/', views.clothings_detail, name='detail'),
    path('accounts/signup/', views.signup, name='signup'),
    path('clothings/create/', views.ClothingCreate.as_view(), name='clothings_create'),
]