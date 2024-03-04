from django import forms
from .models import Enquiries

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiries
        fields = '__all__'
        widgets = {'scope_of_work': forms.TextInput(attrs={
            'class': 'form-control form-control-lg'}),
            'status': forms.TextInput(attrs={
            'class' : 'disabledTextInput'}),
            }