from django.contrib.auth import views as auth_view
from django.urls import path
from . import views 
from .forms import SignupFrom
app_name = 'mainapp'
urlpatterns = [
    path('', views.index name = 'index '),
]
