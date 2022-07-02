from django.urls import path

from service_app import views


urlpatterns = [
    path('', views.home_view, name=''), 
    path('into_audio', views.into_audio, name='into_audio'),
]