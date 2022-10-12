from django import forms
from adminpanel.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'external_id',
            'name'
        )
        widgets = {
            'name': forms.TextInput
        }
