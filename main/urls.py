from django.urls import path

from main import views

urlpatterns = [
    path('', views.PurchaseListAndAdd.as_view(), name='purchase_list'),
    # path('', views.PurchaseList.as_view(), name='purchase_list'),
    path('types/', views.TypeList.as_view(), name='type_list'),
    path('<type_slug>/', views.PurchasesByTypeList.as_view(), name='type_detail'),
    # path('add/', views.PurchaseAdd.as_view(), name='purchase_add'),
]