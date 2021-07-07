from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_html, name='post_html'),
    path('FarRock', views.FarRock, name='FarRock'),
]
