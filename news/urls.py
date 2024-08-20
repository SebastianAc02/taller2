from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name='news'),
    # Add other URL patterns here
]