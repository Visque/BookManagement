from django.urls import path
from books import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create', views.create, name="create"),
    path('display', views.display, name="display"),
]
