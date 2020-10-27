from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from user import views

urlpatterns = [
    path('', views.MyProfileView.as_view(), name='my_profile'),
    path('edit/', views.MyProfileEdit.as_view(), name='my_profile_edit'),
    path('all/', views.profile_list_view, name='profile_list'),
    path('<profile_slug>/', views.ProfileDetailView.as_view(), name='profile_detail')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
