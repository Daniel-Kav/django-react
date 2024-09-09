from django.urls import path
from . import views

urlpatterns = [
    path('/', views.index, name='index'),
    path('/likepost', views.likepost, name='likepost'),
]