from user.models import Profile
from services.main_logic import user_is_anonymous


def get_my_profile(self):
    return Profile.objects.filter(slug=self.request.user.profile.slug)


def all_profiles():
    return Profile.objects.all()


def get_profile(self):
    return Profile.objects.filter(slug=self.kwargs['profile_slug'])