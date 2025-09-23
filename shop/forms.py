from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django import forms
from .models import Profile


class UpdateUserInfo(forms.ModelForm):
    phone = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'شماره موبایل'}),
        required=False

    )
    address1 = forms.CharField(label="",
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'آدرس اصلی'}),
        required=False)
    
    # address2 = forms.CharField(label="",
        # widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'آدرس دوم'})
        # required=False)
    
    city = forms.CharField(label="",
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'شهر'}),
        required=False)
    
    state = forms.CharField(label="",
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'استان'}),
        required=False)

    zipcode = forms.CharField(label="",
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'کدپستی'}),
        required=False)
    
    # country = forms.CharField(label="",
    #     widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':''})
    #     required=False)

    class Meta:
        model = Profile
        fields = ("phone","address1","city","state","zipcode",)


class UpdatePasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
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

    new_password2 = forms.CharField(
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
        fields =  ['new_password1', 'new_password2']



class UpdateUserForm(UserChangeForm):
    password = None
    first_name = forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'نام خود را وارد کنید'}),
        required=False

    )

    last_name = forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'نام خانوادگی خود را وارد کنید'}),
        required=False

    )

    email = forms.EmailField(
        
        label="",
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'ایمییل خود را وارد کنید'}),
        required=False

    )

    username = forms.CharField(
        label="",
        max_length=15,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'نام کاربری خود را وارد کنید'}),
        required=False

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