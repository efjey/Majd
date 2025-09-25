from django.db import models
from django.contrib.auth.models import User

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    shipping_full_name = models.CharField(max_length=250)
    shipping_email = models.CharField(max_length=250)
    shipping_phone = models.CharField(max_length=25, blank=True)
    shipping_address1 = models.CharField(max_length=225, blank=True)
    shipping_address2 = models.CharField(max_length=225, blank=True, null=True)
    shipping_city = models.CharField(max_length=125, blank=True)
    shipping_state = models.CharField(max_length=125, blank=True)
    shipping_zipcode = models.CharField(max_length=25, blank=True)
    shipping_country = models.CharField(max_length=25, default='IRAN')
    shipping_old_cart = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Shipping Address'

    def __str__(self):
        return f"shipping Address From {self.shipping_full_name}"
    