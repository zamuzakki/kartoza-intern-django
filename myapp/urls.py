from django.urls import path
from  . import views


app_name = 'myapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:staff_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create')
]