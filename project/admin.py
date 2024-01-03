from django.contrib import admin
from .models import daily_log
# Register your models here.

class daily_logAdmin(admin.ModelAdmin):
  list_display= ('id','Script_name','Client_name','Client_code','Buy_date','Buy_rate','Buy_quantity','Buy_amount','Sell_date','Sell_rate','Sell_quantity','Sell_amount','Net_pl')
  list_filter=('id','Buy_date','Sell_date','Client_code')
admin.site.register(daily_log,daily_logAdmin)