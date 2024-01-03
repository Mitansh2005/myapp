from django.shortcuts import render
from django.http import HttpResponse
from .models import daily_log
# Create your views here.



def data_entered(request):
  account=daily_log.objects.all()
  return render(request,'project/entered_data.html',{
    "account":account
  })