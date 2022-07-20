from django.urls import path
from . import views
urlpatterns = [
    path('profiles', views.index.as_view()),
]