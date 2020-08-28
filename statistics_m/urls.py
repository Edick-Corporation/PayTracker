from django.urls import path

from statistics_m import views

urlpatterns = [
    path('', views.StatisticsListAndAdd.as_view(), name='statistics'),
]