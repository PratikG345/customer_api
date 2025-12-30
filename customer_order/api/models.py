from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    
    status_choices = [
        ("SHIPPED", "Shipped"),
        ("PLACED", "Placed"),
        ("DELIVERED", "Delivered")
    ]
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    order_date = models.DateField()
    total_amount = models.IntegerField()
    status = models.CharField(max_length=100,choices=status_choices)
    
    def __str__(self):
        return f"{self.customer} - {self.total_amount} - {self.order_date}"