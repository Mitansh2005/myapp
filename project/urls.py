from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.index,name='home'),
    path('data/',views.data_entered,name='data-page'),
    path('upload/',views.excel_file_upload,name='upload-page'),
    path('cmp/',views.Cmp_Entry,name='cmp-page')
]
