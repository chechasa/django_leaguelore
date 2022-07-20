from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.Index.as_view(), name="index_page"),
    path('<slug:slug>/', views.ChampionDetails.as_view(), name="champion-details")
]