from django import forms

from user.models import Profile


class ProfileEdit(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'bio']