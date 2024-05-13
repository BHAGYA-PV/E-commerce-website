from django.db import models
from django.contrib.auth.models import AbstractUser
# # Create your models here.

class User(AbstractUser):
    name=models.CharField(
        max_length=30,
        null=False,
        blank=False
    )
    
    phone=models.BigIntegerField(
        null=True,
        blank=False,
    )
    adress=models.TextField(
        max_length=80,
        null=False,
        blank=False
    )
    email=models.EmailField(
        max_length=50,
        null=False,
        blank=False
    )
    city=models.CharField(
        max_length=50,
        null=False,
        blank=False
    )
    


    

class categories(models.Model):
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.FileField(upload_to="accessory",null=True,blank=True)
    status=models.BooleanField(default=False,help_text="0=default,1=Hidden")
    trending=models.BooleanField(default=False,help_text="0=default,1=Trending")
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    





class product(models.Model):
         name=models.CharField(max_length=100,null=False,blank=False)
         price=models.FloatField(null=False,blank=False)
         image=models.FileField(upload_to="Media",null=True,blank=True)
         categories=models.ForeignKey(categories,on_delete=models.CASCADE)
         status=models.BooleanField(default=False,help_text="0=default,1=Hidden")
         
         def __str__(self):
          return self.name
         


class Cart(models.Model):
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=100,default="cart")
    count=models.IntegerField(default=1)




class Order(models.Model):
     user=models.ForeignKey(User,on_delete=models.CASCADE)
     phone=models.IntegerField()
     address=models.CharField(max_length=500)
    #  options=(
    #       ("order placed","order placed"),
    #       ("shipped","shipped"),
    #       ("out for delivery","out for delivery"),
    #       ("Delivered","Delivered"),
    #       ("cancel","cancel")
    #  )
    #  status=models.CharField(max_length=100,choices=options,default="Order placed")
     date=models.DateField(auto_now_add=True)


class Orderitem(models.Model):
     user=models.ForeignKey(User,on_delete=models.CASCADE)
     products=models.ForeignKey(product,on_delete=models.CASCADE)
     order=models.ForeignKey(Order,on_delete=models.CASCADE)
     price=models.FloatField(null=True)
     options=(
          ("order placed","order placed"),
          ("shipped","shipped"),
          ("out for delivery","out for delivery"),
          ("Delivered","Delivered"),
          ("cancel","cancel")
     )
     status=models.CharField(max_length=100,choices=options,default="Order placed")
     count=models.IntegerField(default=1)