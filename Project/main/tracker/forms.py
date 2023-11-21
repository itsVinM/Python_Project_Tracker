# forms.py
from django import forms
from .models import ProjectTracker

class EditGateForm(forms.ModelForm):
    class Meta:
        model = ProjectTracker
        fields = ['actual_sgate_date', 'actual_agate_date', 'actual_vgate_date', 'actual_rgate_date']
        widgets = {
            'actual_sgate_date': forms.DateInput(attrs={'type': 'date'}),
            'actual_agate_date': forms.DateInput(attrs={'type': 'date'}),
            'actual_vgate_date': forms.DateInput(attrs={'type': 'date'}),
            'actual_rgate_date': forms.DateInput(attrs={'type': 'date'}),
        }
