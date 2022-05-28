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
  
    b=crawlTGDD.crawl_cua_tgdd()
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")
  