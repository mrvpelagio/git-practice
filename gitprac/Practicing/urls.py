from django.urls import path
from .views import index
from .views import task_list

urlpatterns = [
    path('', index, name ='index'),
    path('list', task_list, name = 'task-list'),
]

app_name = "Practicing"