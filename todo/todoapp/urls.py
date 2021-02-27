from . import views
from django.urls import path

app_name = 'todoapp'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('remove/<int:task_id>/', views.remove, name='remove'),
    path('detail/<int:task_id>/', views.detail, name='detail')
]