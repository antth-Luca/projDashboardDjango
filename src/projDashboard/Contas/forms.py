from typing import Any, Mapping
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList

class UserCreationCustomForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'id': 'inputUsername', 'placeholder': 'Digite seu username'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'id': 'inputSenha1', 'placeholder': 'Digite sua senha'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'id': 'inputSenha2', 'placeholder': 'Repita a senha'})


class AuthenticationCustomForm(AuthenticationForm):
    def __init__(self, request, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'id': 'inputUsername', 'placeholder': 'Digite seu username'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'id': 'inputSenha', 'placeholder': 'Digite sua senha'})


class EditUserForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'inputUsername', 'placeholder': 'Digite seu novo username'}),
        max_length=150, required=True,
        help_text='150 caracteres ou menos. Letras, dígitos e @/./+/-/_ apenas.'
    )

    class Meta:
        model = User
        fields = ['username']
