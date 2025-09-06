from django.db import models
import datetime
from django.core.validators import MinValueValidator, MaxValueValidator

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.name}'
    
class Customer(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.name} - {self.last_name}'


class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=400, default='', null=True)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=12)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    picture = models.ImageField(upload_to='upload/product/')
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=20 )
    star = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    is_available = models.BooleanField(default=False)

    AMOUNTS = (('1 baste', 1),('2baste',2),('3 baste',3)) 
    amount = models.CharField(max_length=20, choices=AMOUNTS, default=1)
    
   
    def __str__(self):
        return f'{self.name} - {self.price}'
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    costumer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=300, default='', blank=False)
    phone = models.CharField(max_length=20, blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.product} - {self.costumer}'

class Expense(models.Model):
    name = models.CharField(max_length=50)
    text = models.CharField(max_length=300, default='', null=True)
    price = models.BigIntegerField()
    date = models.DateField(default=datetime.datetime.today)
    def __str__(self):
        return f'{self.name} - {self.price}'

class Income(models.Model):
    branch = models.CharField(max_length=50)
    income = models.BigIntegerField(default=0)
    date = models.DateField(default=datetime.datetime.today)
    def __str__(self):
        return f'{self.branch} - {self.date}'


