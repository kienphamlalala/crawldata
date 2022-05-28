from ast import Num
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Dt3
import crawlTGDD

def index(request):
  mymembers = Dt3.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def crawl_TGDD(request):
    # get the number of pages from html page index.html
    link_name=request.GET['linkname']
    if link_name=='TGDD':
      
      numPg1=request.GET['page']
      numPg=int(numPg1)
      b=crawlTGDD.crawl_cua_tgdd(numPg)
    elif link_name=='FPT':
      numPg1=request.GET['page']
      numPg=int(numPg1)
      b=crawlTGDD.Crawl_cua_FPT(numPg)
    elif link_name=='cellphones' :
      numPg1=request.GET['page']
      numPg=int(numPg1)
      b=crawlTGDD.crawl_Cellphones(numPg)
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")
