from django.db import models

class daily_log(models.Model):
  id=models.AutoField(primary_key=True)
  Script_name=models.CharField(max_length=256)
  Client_name=models.CharField(max_length=256)
  Client_code=models.CharField(max_length=8)
  Buy_date=models.DateField()
  Buy_rate=models.FloatField()
  Buy_quantity=models.IntegerField()
  Buy_amount=models.FloatField(default="",null=False,editable=False)
  Sell_date=models.DateField()
  Sell_rate=models.FloatField()
  Sell_quantity=models.IntegerField()
  Sell_amount=models.FloatField(default="",null=False,editable=False)
  Net_quantity=models.IntegerField(default="",null=False,editable=False)
  Net_pl=models.FloatField(default=0.0,null=False,editable=False)

  
  
  
  class Meta:
    ordering=['id']
  def save(self,*args, **kwargs):
    self.Buy_amount=self.Buy_rate*self.Buy_quantity
    self.Sell_amount=self.Sell_rate*self.Sell_quantity
    self.Net_pl=self.Sell_amount-self.Buy_amount
    self.Net_quantity=self.Buy_quantity-self.Sell_quantity
    
    super().save(*args,**kwargs)
  # def __str__(self):
  #   return f'{self.id} {self.Script_name} {self.Client_name} {self.Client_code} {self.Buy_date} {self.Buy_rate} {self.Buy_quantity} {self.Buy_amount} {self.Sell_date} {self.Sell_rate} {self.Sell_quantity} {self.Sell_amount}  '
