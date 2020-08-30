from django.urls import path

from user import views

urlpatterns = [
    path('', views.MyProfileView.as_view(), name='profile_detail'),
]