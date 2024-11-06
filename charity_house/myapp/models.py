from django.db import models


# Create your models here.
class daily(models.Model):
    userid=models.ForeignKey('auth.User',on_delete=models.CASCADE,db_column='userid')
    ngo_id=models.IntegerField()
    type=models.CharField(max_length=500)
    items=models.CharField(max_length=5000)
    Address=models.CharField(max_length=5000)
    Status=models.CharField(max_length=50,default="UnResponded")

class food(models.Model):
    userid=models.ForeignKey('auth.User',on_delete=models.CASCADE,db_column='userid')
    ngo_id=models.IntegerField()
    Item=models.CharField(max_length=30)
    Place=models.CharField(max_length=30)
    Time=models.CharField(max_length=20)
    Serving=models.CharField(max_length=50)
    Expire=models.CharField(max_length=20)
    Address=models.CharField(max_length=5000)
    Status=models.CharField(max_length=50,default="UnResponded")
    
class money(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    ngo_id=models.IntegerField(null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    razorpay_order_id = models.CharField(max_length=100, blank=True, null=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True, null=True)
    razorpay_signature = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    
    
class ngo(models.Model):
    n_id=models.ForeignKey('auth.User',on_delete=models.CASCADE,db_column='n_id')
    email=models.CharField(max_length=50)

class ngo_details(models.Model):
    u_id=models.ForeignKey('auth.User',on_delete=models.CASCADE,db_column='u_id')
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=5000)
    category=models.CharField(max_length=30)
    works=models.CharField(max_length=500)
    awards=models.CharField(max_length=200)
    pimage = models.ImageField(upload_to='ngo_images')
    
class connected_ngos(models.Model):
    c_id=models.ForeignKey('auth.User',on_delete=models.CASCADE,db_column='userid')
    n_id=models.ForeignKey('ngo_details',on_delete=models.CASCADE,db_column='ngo')
    
class connected_donor(models.Model):
    d_id=models.ForeignKey('auth.User',on_delete=models.CASCADE,db_column='userid')
    ngo_id=models.ForeignKey('ngo_details',on_delete=models.CASCADE,db_column='ngo')
    
class user_details(models.Model):
    d_id=models.ForeignKey('auth.User',on_delete=models.CASCADE,db_column='userid')
    # ngo_id=models.ForeignKey('ngo_details',on_delete=models.CASCADE,db_column='ngo')
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=15,null=True)
    address=models.CharField(max_length=5000)
