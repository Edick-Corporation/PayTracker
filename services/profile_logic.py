from django.shortcuts import redirect, render

from user.models import Profile
from services.main_logic import user_is_anonymous
from user.forms import ProfileEdit


def get_my_profile(self):
    return Profile.objects.filter(slug=self.request.user.profile.slug)


def all_profiles():
    return Profile.objects.all()


def get_profile(self):
    return Profile.objects.filter(slug=self.kwargs['profile_slug'])


def get_form_for_editing_my_profile(self):
    profile = Profile.objects.get(slug=self.request.user.profile.slug)
    return ProfileEdit(instance=profile)


def edit_my_profile(self, request):
    my_profile = Profile.objects.get(slug=self.request.user.profile.slug)
    form = ProfileEdit(self.request.POST, instance=my_profile)

    if form.is_valid():
        my_profile = form.save(commit=False)
        my_profile.save()
        return redirect('my_profile')