from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User

class UserCreationCustomForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'id': 'inputUsername'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'id': 'inputSenha1'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'id': 'inputSenha2'})

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']

class PasswordChangeCustomForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Senha atual'})
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nova senha'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirme a nova senha'})
