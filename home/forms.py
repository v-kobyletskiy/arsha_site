from django import forms
from .models import Message, Subscriber


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
        required = {
            'name': True,
            'email': True,
            'subject': True,
            'message': True
        }


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ('email',)
        widgets = {
            'email': forms.EmailInput()
        },
        required = {
            'email': True,
        }
