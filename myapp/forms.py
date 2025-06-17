from django import forms
from myapp.models import Staff


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'
