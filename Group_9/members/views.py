from ast import Num
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Dt1, Dt2, Dt3, Dt4
import crawlTGDD
import locdienthoai
link_name=""
def index(request):
  mymembers = Dt1.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def crawl_TGDD(request):
    link_name=request.GET['linkname']
    if link_name=='TGDD':
      
      numPg1=request.GET['page']
      numPg=int(numPg1)
      b=crawlTGDD.crawl_cua_tgdd(numPg)
      mymembers = Dt1.objects.all().values()
      template = loader.get_template('index.html')
      context = {
      'mymembers': mymembers,
      }
      return HttpResponse(template.render(context, request))
    elif link_name=='FPT':
      numPg1=request.GET['page']
      numPg=int(numPg1)
      b=crawlTGDD.Crawl_cua_FPT(numPg)
      mymembers = Dt3.objects.all().values()
      template = loader.get_template('index.html')
      context = {
      'mymembers': mymembers,
      }
      return HttpResponse(template.render(context, request))
    elif link_name=='cellphones' :
      numPg1=request.GET['page']
      numPg=int(numPg1)
      b=crawlTGDD.crawl_Cellphones(numPg)
      mymembers = Dt2.objects.all().values()
      template = loader.get_template('index.html')
      context = {
      'mymembers': mymembers,
      }
      return HttpResponse(template.render(context, request))
    #return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")
def filterdanhgia(request):
  link_name=request.GET['nameshop']
  danhgia=request.GET['danhgia']
  if(danhgia==""):
    danhgia=0
  else:
    danhgia=float(danhgia)
  giadau=request.GET['giadautien']
  giadau=int(giadau)
  giacuoi=request.GET['giacuoi']
  giacuoi=int(giacuoi)
  if (link_name=="TGDD"):
    tensql="dienthoai.db"
    tenbang="dienthoai1"
    a=locdienthoai.loc(tensql,tenbang,giadau,giacuoi,danhgia)
    mymembers = Dt4.objects.all().values()
    template = loader.get_template('index.html')
    context = {
      'mymembers': mymembers,
      }
    return HttpResponse(template.render(context, request))
  elif (link_name=="FPT"):
    tensql="dienthoai.db"
    tenbang="dienthoai3"
    a=locdienthoai.loc(tensql,tenbang,giadau,giacuoi,danhgia)
    mymembers = Dt4.objects.all().values()
    template = loader.get_template('index.html')
    context = {
      'mymembers': mymembers,
      }
    return HttpResponse(template.render(context, request))
  elif (link_name=="cellphones"):
    tensql="dienthoai.db"
    tenbang="dienthoai2"
    a=locdienthoai.loc(tensql,tenbang,giadau,giacuoi,danhgia)
    mymembers = Dt4.objects.all().values()
    template = loader.get_template('index.html')
    context = {
      'mymembers': mymembers,
      }
    return HttpResponse(template.render(context, request))
  elif (link_name==""):
    return  HttpResponse("""Mời bạn điền thông tin""")
    
