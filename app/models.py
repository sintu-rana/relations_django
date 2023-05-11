from django.db import models

# Create your models here.
'''
1. We can have multiple Markets
2. Each market can have multiple Shops
3. Each Shop can have multiple Products
4. Each Product can have multiple Brands, Price
5. Each Product can have different Rating according to Brand
'''

class Market(models.Model):                 
    name=models.CharField(max_length=50)

class Shop(models.Model):
    name=models.CharField(max_length=50)
    market=models.ForeignKey(Market, on_delete=models.CASCADE, related_name='shops')


class Product(models.Model):
    name=models.CharField(max_length=50)
    shop=models.ForeignKey(Shop, on_delete=models.CASCADE,related_name='products')


class Brand(models.Model):
    name=models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="brands")
    price=models.DecimalField(max_digits=10, decimal_places=2)
    rate = models.DecimalField(max_digits=10, decimal_places=2)


    






