from django.urls import path

from main import views

urlpatterns = [
    path('', views.PurchaseListAndAdd.as_view(), name='purchase_list'),
    # path('add/', views.PurchaseAdd.as_view(), name='purchase_add'),
]