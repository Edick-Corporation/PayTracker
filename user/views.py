from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, View
from services.profile_logic import get_my_profile, all_profiles, get_profile, get_form_for_editing_my_profile,\
    edit_my_profile
from services.main_logic import user_is_anonymous
from user.utils import MyProfileEditMixin


def my_profile_view(request):
    if request.user.is_anonymous:
        return HttpResponseRedirect('/accounts/login/')
    else:
        return render(request, 'profile/my_profile.html', context={'my_profile': get_profile})

# class MyProfileView(ListView):
#     """Отображение своего Профиля"""
#
#     template_name = 'profile/my_profile.html'
#     context_object_name = 'my_profile'
#
#     def get_queryset(self):
#         if self.request.user.is_anonymous:
#
#
#         else:
#             return get_my_profile(self)


class MyProfileEdit(MyProfileEditMixin, View):
    """Редактирование своего Профиля"""

    queryset = get_form_for_editing_my_profile
    form = edit_my_profile
    template_name = 'profile/edit.html'


def profile_list_view(request):
    qs = all_profiles
    if request.user.is_anonymous:
        return HttpResponseRedirect('/accounts/login')
    else:
        return render(request, 'profile/profile_list.html', context={'profile_list': qs})


class ProfilesListView(ListView):
    """Список всех пользователей"""

    template_name = 'profile/profile_list.html'
    context_object_name = 'profile_list'
    queryset = all_profiles


class ProfileDetailView(ListView):
    """Отображение одного пользователя"""

    template_name = 'profile/profile_detail.html'
    context_object_name = 'profile_detail'
    queryset = get_profile
