from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('home/',views.home),
    path('index/',views.index),
    path('add/<int:a>/<int:b>',views.add),
    path('College_list/',views.College_list)
]
