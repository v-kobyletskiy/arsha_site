from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('name', 'email', 'subject', 'message')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'id': 'subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': '10'})
        }
        name = forms.CharField(required=True)
        email = forms.EmailField(required=True)
        subject = forms.CharField(required=True)
        message = forms.CharField(required=True)
