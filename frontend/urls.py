from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('execute-command/', views.execute_command, name='execute_command'),
]
