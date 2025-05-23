from django import forms
from .models import PassportApplication

class PassportApplicationForm(forms.ModelForm):
    class Meta:
        model = PassportApplication
        exclude = ['user', 'status', 'submission_date']
