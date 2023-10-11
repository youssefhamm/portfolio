from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    

    class Meta:
        model = Contact
        fields = ['nom', 'email', 'subject', 'message']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }