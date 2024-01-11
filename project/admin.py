from datetime import datetime
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from rangefilter.filters import (
    DateRangeFilterBuilder,
    DateTimeRangeFilterBuilder,
    NumericRangeFilterBuilder,
    DateRangeQuickSelectListFilterBuilder,
)
from .models import daily_log
# Register your models here.

class daily_logAdmin(admin.ModelAdmin):
  list_display= ('Id','Script_Name','Client_Name','Client_Code','Buy_Date','Buy_Rate','Buy_Quantity','Buy_Amount','Sell_Date','Sell_Rate','Sell_Quantity','Sell_Amount','Net_Quantity','Net_Avg','Net_Amount','Cmp_Rate','Net_Pl','M2M')
  list_filter=('Id','Buy_Date','Sell_Date','Client_Code',("Buy_Date", DateRangeFilterBuilder()),
                (
            "Sell_Date",
            DateTimeRangeFilterBuilder(
                title="Sell Date",
                default_start=datetime(2020, 1, 1),
                default_end=datetime(2030, 1, 1),
            )),
        ("Buy_Date", DateRangeQuickSelectListFilterBuilder()),  # Range + QuickSelect Filter
    )
admin.site.register(daily_log,daily_logAdmin)
