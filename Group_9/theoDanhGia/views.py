from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Dttheodanhgia

def index(request):
  myDanhGia = Dttheodanhgia.objects.all().values()
  template = loader.get_template('danhgia.html')
  context = {
    'myDanhGia': myDanhGia,
  }
  return HttpResponse(template.render(context, request))

