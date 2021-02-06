from . import views
from django.urls import path

app_name = 'todoapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/', views.detail, name='detail'),
    path('remove/<int:item_id>/', views.remove, name='remove')
]