from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect

from user.models import Profile
from user.forms import ProfileEdit


def get_my_profile(self):
    """Сервис для получении своего профиля"""

    return Profile.objects.get(slug=self.request.user.profile.slug)


def all_profiles(self):
    """Сервис для получения всех профилей"""
    return Profile.objects.all()


def get_profile(self):
    """Сервис для получение конкретного профиля"""

    return Profile.objects.get(slug=self.kwargs['profile_slug'])


def get_form_for_editing_my_profile(self):
    """Сервис для получения формы для редактирования профиля"""

    profile = Profile.objects.get(id=self.request.user.profile.id)
    return ProfileEdit(instance=profile)


def edit_my_profile(self, request):
    """Сервис для редактирования профиля"""

    my_profile = Profile.objects.get(id=self.request.user.profile.id)
    form = ProfileEdit(request.POST, request.FILES, instance=my_profile)

    if form.is_valid():
        form = form.save(commit=False)
        form.save()

        return redirect('my_profile')