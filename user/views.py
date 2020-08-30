from django.shortcuts import render
from django.views.generic import ListView

from services.profile_logic import get_my_profile
from services.main_logic import user_is_anonymous


class MyProfileView(ListView):
    template_name = 'profile/my_profile.html'
    context_object_name = 'my_profile'

    def get_queryset(self):
        return user_is_anonymous(obj=get_my_profile(self))
