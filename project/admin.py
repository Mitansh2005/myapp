from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import daily_log
# Register your models here.

class daily_logAdmin(admin.ModelAdmin):
  list_display= ('Id','Script_Name','Client_Name','Client_Code','Buy_Date','Buy_Rate','Buy_Quantity','Buy_Amount','Sell_Date','Sell_Rate','Sell_Quantity','Sell_Amount','Net_Quantity','Net_Pl')
  list_filter=('Id','Buy_Date','Sell_Date','Client_Code')
admin.site.register(daily_log,daily_logAdmin)
