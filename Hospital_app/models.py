from django.db import models

class d_type(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.type_name}"

class product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    product_type = models.ForeignKey(d_type, on_delete=models.CASCADE)
    product_qty = models.IntegerField()
    product_exp = models.DateField()
    def __str__(self):
        return f"{self.product_name} , {self.product_exp}"
    
class userbuy(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    tal = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.username} , {self.tal}"
    
class report_buy(models.Model):
    report_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    tal = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    product_qty = models.IntegerField()
    def __str__(self):
        return f"{self.username} , {self.product_qty}"
    

    