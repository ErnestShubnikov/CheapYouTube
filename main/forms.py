from django import forms
from .models import CustomUser
from django.core.validators import MinLengthValidator

class UploadForm(forms.Form):
    title = forms.CharField(max_length=40)
    photo = forms.ImageField()
    video = forms.FileField()



class RegForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label='Password', validators=[MinLengthValidator(5)])
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password', validators=[MinLengthValidator(5)])
    
    class Meta:
        model  = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match')
        return password2
    
class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
