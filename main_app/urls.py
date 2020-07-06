from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clothing/', views.clothings_index, name='index'),
    path('myclothing/', views.myclothings_index, name='myindex'),
    path('accounts/signup/', views.signup, name='signup'),
]