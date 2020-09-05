from django.urls import path

from user import views

urlpatterns = [
    path('', views.MyProfileView.as_view(), name='my_profile'),
    path('all/', views.ProfilesListView.as_view(), name='profile_list'),
    path('<profile_slug>/', views.ProfileDetailView.as_view(), name='profile_detail')
]