#%%
import imp
from selenium import webdriver
from bs4 import BeautifulSoup 
import pandas as pd
import csv
import requests
from classdt import dienthoai
import sqlite3

conn = sqlite3.connect('dienthoai.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS dienthoai3(
            
            name TEXT,
            brand TEXT,
            display TEXT,
            hdh TEXT,
            camera_sau TEXT,
            camera_truoc TEXT,
            chip TEXT,
            ram TEXT,
            rom TEXT,
            sim TEXT,
            battery TEXT,
         
            price INTEGER,
            danhgia TEXT,
            sluong TEXT,
            link TEXT
            )""")
#create class dienthoai
#delete all data in table dienthoai2.db
#c.execute("DELETE FROM dienthoai3")
def crawl_tgdd(dienthoai):
    with conn:
        c.execute(sql_insert,{'name':dienthoai.name,'brand':dienthoai.brand,'display':dienthoai.display,'hdh':dienthoai.hdh,'camera_sau':dienthoai.camera_sau,'camera_truoc':dienthoai.camera_truoc,'chip':dienthoai.chip,'ram':dienthoai.ram,'rom':dienthoai.rom,'sim':dienthoai.sim,'battery':dienthoai.battery,'price':dienthoai.price,'danhgia':dienthoai.danhgia,'sluong':dienthoai.sluong,'link':dienthoai.link})
driver=webdriver.Edge('D:\VISUAL\python\CrawlDataFromWeb\msedgedriver.exe')
url='https://fptshop.com.vn/dien-thoai' #Lấy link để mở web tự động
driver.get(url)
def GetUrl():
    page_s=BeautifulSoup(driver.page_source,"html.parser") #dùng bs4 tải toàn bộ HTML document lên chương trình

    tel_infors=page_s.find('div',class_='cdt-product-wrapper m-b-20')

    all_prod=[]

    for tel_infor in tel_infors:
        
        tel_ID=tel_infor.find('a').get('href') # lấy link đuôi trong thành phần có tên là href
        tel_If_url=''
        if tel_ID !=None and tel_If_url not in all_prod:
            tel_If_url='https://fptshop.com.vn'+tel_ID
            all_prod.append(tel_If_url)
        set(all_prod)
    return all_prod
    

numPg=3 
Url_all=[]
  
for i in range(numPg):
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)') # thực hiện kéo xuống xuối cuối trang 
    next_btn=driver.find_element_by_xpath('//*[@id="root"]/main/div/div[3]/div[2]/div[2]/div/div[3]/a')
    next_btn.click()
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)') # thực hiện kéo xuống xuối cuối trang 
Url_each_page=GetUrl() # Lấy thông tin tất cả từng trang
Url_all=Url_all+Url_each_page 

for url in Url_all:

    driver.get(url)
    page_source=BeautifulSoup(driver.page_source,"html.parser")

    div1=page_source.find('table',class_='st-pd-table')

    try :
        display=div1.find_all('td')[1].get_text()
    except AttributeError                            :
        continue

    name=page_source.find_all('h1',class_='st-name')[0].get_text()
    name=name.split(' ')
    brand=name[0]
    name2=name.pop(-1)
    name=" ".join(name)
    ram=div1.find_all('td')[7].get_text()
    rom=div1.find_all('td')[9].get_text()
    cpu=div1.find_all('td')[11].get_text()
    try:
        battery=div1.find_all('td')[15].get_text()
    except IndexError:
        continue
    try:
        hdh=div1.find_all('td')[19].get_text()
    except IndexError:
        continue

    sim=div1.find_all('td')[17].get_text()


    camera_sau=div1.find_all('td')[3].get_text()
    camera_truoc=div1.find_all('td')[5].get_text()


    nameshop="Cửa hàng FPT"


    gia_tmp=page_source.find_all('div',class_='st-price-main')[0].get_text()
    gia=gia_tmp.replace('₫','')
    gia=int(gia.replace('.',''))

    try :

        danhgia=page_source.find_all('div',class_='point')[0].get_text()
        danhgia=danhgia.split('/')
        danhgia=float(danhgia[0])
    except IndexError :
        continue


    soluong=page_source.find_all('a',class_='re-link',id='re-rate')[0].get_text()
    soluong=soluong.split(' ')
    soluong=int(soluong[0])

    link=url
    #INSERT ALL DATA TO DATABASE
    print(name,brand,display,hdh,camera_sau,camera_truoc,cpu,ram,rom,sim,battery,gia,danhgia,soluong,link)
    sql_insert="INSERT INTO dienthoai3 VALUES(:name,:brand,:display,:hdh,:camera_sau,:camera_truoc,:chip,:ram,:rom,:sim,:battery,:price,:danhgia,:sluong,:link)"
    dt1= dienthoai (name,brand,display,hdh,camera_sau,camera_truoc,cpu,ram,rom,sim,battery,gia,danhgia,soluong,link)
    
    crawl_tgdd(dt1)
    
   
c.close()  
    