from django.urls import include, path
from linebotapp import views

urlpatterns = [
    path("callback", views.callback),
]