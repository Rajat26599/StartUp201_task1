from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password'}))

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = ''
        self.fields['email'].label = ''
        self.fields['password'].label = ''

    class Meta():
        model = User
        fields = ('username','email','password')

        widgets = {
            'username': forms.TextInput(attrs = {'class':'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs = {'class':'form-control', 'placeholder': 'Email address'}),
        }


class UserProfileInfoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserProfileInfoForm, self).__init__(*args, **kwargs)
        self.fields['portfolio_site'].label = ''

    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')

        widgets = {
            'portfolio_site': forms.TextInput(attrs = {'class':'form-control', 'placeholder': 'Portfolio site'}),
        }
