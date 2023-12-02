from django.db import models

class Purchase(models.Model):
    customer_name = models.CharField(max_length=255)
    customer_address = models.CharField(max_length=255,default='')
    customer_email = models.EmailField()
    product_name = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)