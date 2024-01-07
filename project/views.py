from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import daily_log
from .resources import daily_logResource
from django.contrib import messages
from tablib import Dataset
# Create your views here.

def excel_file_upload(request):
  if request.method=='POST':
    dataset=Dataset()
    new_daily_log=request.FILES['myfile']

    if not new_daily_log.name.endswith('xlsx'):
      messages.info(request,'wrong format')
      return render(request,'upload.html')
    
    imported_data=dataset.load(new_daily_log.read(),format='xlsx')
    for data in imported_data:
      value= daily_log(
        data[0],
        data[1],
        data[2],
        data[3],
        data[4],
        data[5],
        data[6],
        data[7],
        data[8],
        data[9],
        data[10],
        data[11],
        data[12],
        data[13],
      )
      value.save()
  return render(request,'upload.html')

def data_entered(request):
  account=daily_log.objects.all()
  return render(request,'project/entered_data.html',{
    "account":account
  })


def index(request):
  return render(request,'project/index.html')
