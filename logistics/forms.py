from django import forms
from .models import Enquiries

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiries
        fields = '__all__'
        