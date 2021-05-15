from django import forms

from .models import BeneficiaryDetails


class BeneficiaryDetailsModelForm(forms.ModelForm):
    class Meta:
        model = BeneficiaryDetails
        fields = ['name', 'boid',]
