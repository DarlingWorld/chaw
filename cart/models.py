from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User 
from techbro.models import Dish 
# Create your models here.


class Shopcart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    c_item = models.IntegerField(default=1)
    c_date = models.DateTimeField(auto_now=True)
    c_name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    c_price = models.IntegerField()
    amount = models.IntegerField()
    cart_code = models.CharField(max_length=255, default='a')
    paid = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username
        
    class meta: 
        db_table = 'shopcart'
        managed = True
        verbose_name = 'Shopcart'
        verbose_name_plural = 'Shopcarts'
  

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,editable= False)
    first_name = models.CharField(max_length= 50, editable= False)
    last_name = models.CharField(max_length= 50, editable= False) 
    total = models.IntegerField(editable= False)
    cart_code = models.CharField(max_length= 255, editable= False)
    pay_code = models.CharField(max_length= 36, editable= False )
    phone = models.CharField(max_length= 36, default='a')
    paid = models.BooleanField (default = False, editable= False)
    pay_date = models.DateTimeField(auto_now_add= True)
    admin_note = models.CharField(max_length= 255, )
    admin_update = models.DateTimeField(auto_now= True)

    def _str_(self):
        return self.user.username

    class Meta:
        db_table = "payment"
        managed = True
        verbose_name = 'Payment'
        verbose_name_plural ='Payments'
           
