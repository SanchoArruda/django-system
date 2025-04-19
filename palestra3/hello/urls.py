from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("sancho", views.sancho, name="sancho"),
    path("<str:name>", views.saudacao, name = "saudacao" )
]