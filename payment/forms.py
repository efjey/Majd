from django import forms 
from .models import ShippingAddress

class ShippingForm(forms.ModelForm):
    shipping_full_name = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'نام و نام خانوادگی'}),
        required=True

    )
    shipping_address1 = forms.CharField(label="",
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'آدرس اصلی'}),
        required=True)
    
    shipping_email = forms.CharField(
        label="",
        widget=forms.TimeInput(attrs={'class':'form-control', 'placeholder':'Email'}),
        required=False,

    )
    
    # shipping_address2 = forms.CharField(label="",
        # widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'آدرس دوم'})
        # required=False)
    
    shipping_city = forms.CharField(label="",
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'شهر'}),
        required=True)
    
    shipping_state = forms.CharField(label="",
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'استان'}),
        required=True)

    shipping_zipcode = forms.CharField(label="",
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'کدپستی'}),
        required=True)
    
    # shipping_country = forms.CharField(label="",
    #     widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':''})
    #     required=False)shipping_

    class Meta:
        model = ShippingAddress
        fields=[
            'shipping_full_name',
            'shipping_email',
            'shipping_address1',
            'shipping_email',
            'shipping_city',
            'shipping_state',
            'shipping_zipcode',        
        ]

        exclude = ['user',]