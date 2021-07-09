from django.urls import path
from books import views

urlpatterns = [
    path('', views.index, name="index"),                # index page URL
    path('create', views.create, name="create"),        # Create page URL
    path('display', views.display, name="display"),     # Display page URL
]
