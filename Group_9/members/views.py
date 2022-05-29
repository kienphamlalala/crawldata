from ast import Num
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Dt1, Dt2, Dt3, Dt4,Dt5
import crawlTGDD
import locdienthoai
import crawlmulti
link_name=""
def index(request):
  mymembers = Dt1.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
def crawl_TGDD(request):
    name1=request.GET['linkname']
    link_name=name1.split(',')
    lenlk=len(link_name)
    if (lenlk>1):
      crawlmulti.deletetable()
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
      else:
        for i in range(lenlk):
          if link_name[i]=='TGDD':
        
            numPg1=request.GET['page']
            numPg=int(numPg1)
            b=crawlmulti.crawl_cua_tgdd(numPg)
           
          elif (link_name[i]=='FPT'):
            numPg1=request.GET['page']
            numPg=int(numPg1)
            b=crawlmulti.Crawl_cua_FPT(numPg)
          
          elif (link_name[i]=='cellphones') :
            numPg1=request.GET['page']
            numPg=int(numPg1)
            b=crawlmulti.crawl_Cellphones(numPg)
      mymembers = Dt5.objects.all().values()
      template = loader.get_template('index.html')
      context = {
      'mymembers': mymembers,}
      return HttpResponse(template.render(context, request))
    else :
      if link_name[0]=='TGDD':
        numPg1=request.GET['page']
        numPg=int(numPg1)
        b=crawlTGDD.crawl_cua_tgdd(numPg)
        mymembers = Dt1.objects.all().values()
        template = loader.get_template('index.html')
        context = {
        'mymembers': mymembers,
        }
        return HttpResponse(template.render(context, request))
      elif link_name[0]=='FPT':
        numPg1=request.GET['page']
        numPg=int(numPg1)
        b=crawlTGDD.Crawl_cua_FPT(numPg)
        mymembers = Dt3.objects.all().values()
        template = loader.get_template('index.html')
        context = {
        'mymembers': mymembers,
        }
        return HttpResponse(template.render(context, request))
      elif link_name[0]=='cellphones' :

        numPg1=request.GET['page']
        numPg=int(numPg1)
        b=crawlTGDD.crawl_Cellphones(numPg)
        mymembers = Dt2.objects.all().values()
        template = loader.get_template('index.html')
        context = {
        'mymembers': mymembers,
        }
        return HttpResponse(template.render(context, request))
def filterdanhgia(request):
  name1=request.GET['nameshop']
  brand=request.GET['brand']
  link_name=name1.split(',')
  lenlk=len(link_name)
  if (lenlk==1):
    danhgia=request.GET['danhgia']
    if(danhgia==""):
      danhgia=0
    else:
      danhgia=float(danhgia)
    giadau=request.GET['giadautien']
    if( giadau==""):
      giadau=0
    else:
      giadau=int(giadau)
    giacuoi=request.GET['giacuoi']
    if (giacuoi==""):
      giacuoi=100000000
    else:
      giacuoi=int(giacuoi)
    if (link_name[0]=="TGDD"):
      tensql="dienthoai.db"
      tenbang="dienthoai1"
      a=locdienthoai.loc(tensql,tenbang,giadau,giacuoi,danhgia,brand)
      mymembers = Dt4.objects.all().values()
      template = loader.get_template('index.html')
      context = {
        'mymembers': mymembers,
        }
      return HttpResponse(template.render(context, request))
    elif (link_name[0]=="FPT"):
      tensql="dienthoai.db"
      tenbang="dienthoai3"
      a=locdienthoai.loc(tensql,tenbang,giadau,giacuoi,danhgia,brand)
      mymembers = Dt4.objects.all().values()
      template = loader.get_template('index.html')
      context = {
        'mymembers': mymembers,
        }
      return HttpResponse(template.render(context, request))
    elif (link_name[0]=="cellphones"):
      tensql="dienthoai.db"
      tenbang="dienthoai2"
      a=locdienthoai.loc(tensql,tenbang,giadau,giacuoi,danhgia,brand)
      mymembers = Dt4.objects.all().values()
      template = loader.get_template('index.html')
      context = {
        'mymembers': mymembers,
        }
      return HttpResponse(template.render(context, request))
    elif (link_name[0]==""):
      return  HttpResponse("""Mời bạn điền thông tin""")
  else:
    danhgia=request.GET['danhgia']
    if(danhgia==""):
      danhgia=0
    else:
      danhgia=float(danhgia)
    giadau=request.GET['giadautien']
    if( giadau==""):
      giadau=0
    else:
      giadau=int(giadau)
    giacuoi=request.GET['giacuoi']
    if (giacuoi==""):
      giacuoi=100000000
    else:
      giacuoi=int(giacuoi)
    tensql="dienthoai.db"
    tenbang="dienthoaiall"
    a=locdienthoai.loc(tensql,tenbang,giadau,giacuoi,danhgia)
    mymembers = Dt5.objects.all().values()
    template = loader.get_template('index.html')
    context = {
      'mymembers': mymembers,
      }
    return HttpResponse(template.render(context, request))
