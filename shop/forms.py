from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

class UpdateUserForm(UserChangeForm):
    password = None
    first_name = forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'نام خود را وارد کنید'})

    )

    last_name = forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'نام خانوادگی خود را وارد کنید'})

    )

    email = forms.EmailField(
        
        label="",
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'ایمییل خود را وارد کنید'})

    )

    username = forms.CharField(
        label="",
        max_length=15,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'نام کاربری خود را وارد کنید'})

    )

    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'نام خود را وارد کنید'})

    )

    last_name = forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'نام خانوادگی خود را وارد کنید'})

    )

    email = forms.EmailField(
        
        label="",
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'ایمییل خود را وارد کنید'})

    )

    username = forms.CharField(
        label="",
        max_length=15,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'نام کاربری خود را وارد کنید'})

    )

    password1 = forms.CharField(
        label="",
        widget = forms.PasswordInput(
            attrs={
                'class':'form-control',
                'name':'password',
                'type':'password',
                'placeholder':'رمز بیشتر از 8 کاراکتر وارد کنید'
            }
        )
    )

    password2 = forms.CharField(
        label="",
        widget = forms.PasswordInput(
            attrs={
                'class':'form-control',
                'name':'password',
                'type':'password',
                'placeholder':'تکرار رمز عبور'
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')