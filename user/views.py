from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, View
from services.profile_logic import get_my_profile, all_profiles, get_profile, get_form_for_editing_my_profile,\
    edit_my_profile
from services.main_logic import user_is_anonymous
from user.utils import MyProfileEditMixin, MyProfileMixin


class MyProfileView(MyProfileMixin, View):
    """Отображение своего Профиля"""

    template_name = 'profile/my_profile.html'
    context_object_name = 'my_profile'
    queryset = get_my_profile


class MyProfileEdit(MyProfileEditMixin, View):
    """Редактирование своего Профиля"""

    queryset = get_form_for_editing_my_profile
    form = edit_my_profile
    template_name = 'profile/edit.html'


def profile_list_view(request):
    qs = all_profiles()
    if request.user.is_anonymous:
        return HttpResponseRedirect('/accounts/login')
    else:
        return render(request, 'profile/profile_list.html', context={'profile_list': qs})


class ProfileDetailView(ListView):
    """Отображение одного пользователя"""

    template_name = 'profile/profile_detail.html'
    context_object_name = 'profile_detail'
    queryset = get_profile