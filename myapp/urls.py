from django.urls import path
from  . import views


app_name = 'myapp'
urlpatterns = [
    # path('', views.index, name='index'),
    # path('staff/<int:staff_id>/', views.detail, name='detail'),
    # path('staff/create/', views.create, name='create'),
    path('', views.IndexView.as_view(), name='index'),
    path('staff/<int:pk>/update/', views.UpdateView.as_view(), name='update'),
    path('staff/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('staff/create/', views.CreateView.as_view(), name='create'),
]