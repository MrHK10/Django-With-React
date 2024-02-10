from django.contrib import admin
from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_language/', views.add_language, name='add_language'),
    path('add_question_answer/', views.add_question_answer, name='add_question_answer'),
]
