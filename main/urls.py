from django.urls import path

from main import views

urlpatterns = [
    path('', views.PurchaseList.as_view(), name='purchase_list'),
]