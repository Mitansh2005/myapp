from django.db import models

class daily_log(models.Model):
  Id=models.AutoField(primary_key=True)
  Script_Name=models.CharField(max_length=256)
  Client_Name=models.CharField(max_length=256)
  Client_Code=models.CharField(max_length=8)
  Buy_Date=models.DateField()
  Buy_Rate=models.FloatField()
  Buy_Quantity=models.IntegerField()
  Buy_Amount=models.FloatField(default="",null=False,editable=False)
  Sell_Date=models.DateField(default="",null=True,blank=True)
  Sell_Rate=models.FloatField(default="0",null=True,blank=True)
  Sell_Quantity=models.IntegerField(default="0",null=True,blank=True)
  Sell_Amount=models.FloatField(default="0",null=True,editable=False,blank=True)
  Net_Quantity=models.IntegerField(default="",null=False,editable=False)
  Net_Pl=models.FloatField(default=0.0,null=False,editable=False)

  class Meta:
    ordering=['Id']
  
  
  def save(self,*args, **kwargs):
    self.Buy_Amount=self.Buy_Rate*self.Buy_Quantity
    self.Sell_Amount=self.Sell_Rate*self.Sell_Quantity
    self.Net_Pl=(self.Sell_Quantity*self.Sell_Rate)-(self.Sell_Quantity*self.Buy_Rate)
    self.Net_Quantity=self.Buy_Quantity-self.Sell_Quantity
    
    super().save(*args,**kwargs)
  # def __str__(self):
  #   return f'{self.id} {self.Script_name} {self.Client_name} {self.Client_code} {self.Buy_date} {self.Buy_rate} {self.Buy_quantity} {self.Buy_amount} {self.Sell_date} {self.Sell_rate} {self.Sell_quantity} {self.Sell_amount}  '

