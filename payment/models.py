from django.db import models
from django.contrib.auth.models import User
from shop.models import Product
from django.db.models.signals import post_save

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    shipping_full_name = models.CharField(max_length=250)
    shipping_email = models.CharField(max_length=250,blank=True)
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
    
def create_shipping_user(sender, instance, created, **kwargs):
    if created:
        user_shipping = ShippingAddress(user=instance)
        user_shipping.save()

post_save.connect(create_shipping_user, sender=User)
    
class Order(models.Model):
    STATUS_ORDER = [
        ('Pending', 'در انتظار پرداخت'),
        ('Processing', 'در حال پردازش'),
        ('Shipped', 'ارسال شده به پست'),
        ('Delivered', 'تحویل به مشتری'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=300)
    shipping_address = models.TextField(max_length=150000)
    amount_paid = models.DecimalField( max_digits=15, decimal_places=0)
    date_ordered = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_ORDER, default='Pending')

    def __str__(self):
        return f'order - {str(self.id)}'
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    quantity = models.PositiveBigIntegerField(default=1)
    price = models.DecimalField(decimal_places=0, max_digits=15)

    def __str__(self):
        if self.user is not None:
            return f'Order item - {str(self.id)} - for {self.user}'
        else:
            return f'Order item - {str(self.id)}'


    