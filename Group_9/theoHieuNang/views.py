from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Dttheohieunang

def index(request):
  myHieuNang = Dttheohieunang.objects.all().values()
  template = loader.get_template('hieunang.html')
  context = {
    'myHieuNang': myHieuNang,
  }
  return HttpResponse(template.render(context, request))