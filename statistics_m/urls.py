from django.urls import path

from statistics_m import views

urlpatterns = [
    path('', views.PieChartAndPurchases.as_view(), name='pie-chart'),
    path('detail/', views.StatisticsListAndAdd.as_view(), name='statistics'),

]