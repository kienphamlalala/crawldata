from selenium import webdriver
from bs4 import BeautifulSoup 
import pandas as pd
import csv
import requests
import time
import sqlite3
from classdt import dienthoai

# Open web automaticly
def crawl_Cellphones():
    conn = sqlite3.connect('dienthoai.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS dienthoai1(
                
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
    
    def crawl_cellphones(dienthoai):
        with conn:
            c.execute(sql_insert,{'name':dienthoai.name,'brand':dienthoai.brand,'display':dienthoai.display,'hdh':dienthoai.hdh,'camera_sau':dienthoai.camera_sau,'camera_truoc':dienthoai.camera_truoc,'chip':dienthoai.chip,'ram':dienthoai.ram,'rom':dienthoai.rom,'sim':dienthoai.sim,'battery':dienthoai.battery,'price':dienthoai.price,'danhgia':dienthoai.danhgia,'sluong':dienthoai.sluong,'link':dienthoai.link})
    driver=webdriver.Edge('D:\VISUAL\python\CrawlDataFromWeb\msedgedriver.exe')
    url='https://cellphones.com.vn/mobile.html' #Lấy link để mở web tự động
    driver.get(url)

    def GetUrl():
        page_s=BeautifulSoup(driver.page_source,"html.parser") #dùng bs4 tải toàn bộ HTML document lên chương trình
        tel_infors=page_s.find_all('div',class_='block-products san-pham-cate')
        div1=tel_infors[0].find_all('div',class_='box-products')
        div2=div1[0].find_all('div',class_='item-product')
        all_prod=[]

        for tel_infor in div2:
            tel_ID=tel_infor.find('a').get('href')
        
            if tel_ID!=None and tel_ID not in all_prod:
                all_prod.append(tel_ID)
            set(all_prod)

        return all_prod


    numPg=3
    Url_all=[]
    for i in range(numPg):
        #sroll down until found element next button 
        driver.execute_script("arguments[0].scrollIntoView();", driver.find_element_by_xpath("/html/body/div[1]/div/section/div/div[5]/div/a"))
        driver.execute_script("window.scrollBy(0, -150);")
        e=driver.find_element_by_xpath("/html/body/div[1]/div/section/div/div[5]/div/a")
        e.click()
    time.sleep(13)

    Url_all=[]
    Url_all =GetUrl()

    for url in Url_all:

            driver.get(url)
            page_source=BeautifulSoup(driver.page_source,"html.parser")
            div1=page_source.find_all('table',id='tskt')
            #get text of element has tag td in div1
            try:
                    display=div1[0].find_all('th')[23].get_text()
            except IndexError:
                    continue
            name=page_source.find_all('div',class_='box-name__box-product-name')[0].get_text()
            camera_sau=display=div1[0].find_all('th')[5].get_text()
            camera_truoc=display=div1[0].find_all('th')[7].get_text()
            chip=display=div1[0].find_all('th')[9].get_text()
            ram=display=div1[0].find_all('th')[11].get_text()
            rom=display=div1[0].find_all('th')[13].get_text()
            battery=display=div1[0].find_all('th')[15].get_text()
            sim=display=div1[0].find_all('th')[17].get_text()
            hdh=display=div1[0].find_all('th')[19].get_text()
            sl_tmp=page_source.find_all('p',class_='rating-total')
            soluong=sl_tmp[0].get_text()
            soluong=soluong.split(' ')
            soluong=int(soluong[0])
            dgtmp=page_source.find_all('div',class_='chart-vote__box-left')[0].get_text()
            danhgia=dgtmp.split('/')
            danhgia=float(danhgia[0])
            
            nameshop='Cellphones'
            link=url
            brand=name.split(' ')[0]
            try:
                    giatmp=page_source.find_all('p',class_='special-price')[0].get_text()
                    gia=giatmp.replace('₫','')
                    gia=int(gia.replace('.',''))
            except AttributeError:
                    giatmp=page_source.find_all('p',class_='old-price')[0].get_text()
                    gia=giatmp.replace('₫','')
                    gia=int(gia.replace('.',''))
                    
            except IndexError:
                    continue
            brand=brand.strip()
            name=name.strip()
            print(name,brand,display,hdh,camera_sau,camera_truoc,chip,ram,rom,sim,battery,gia,danhgia,soluong,link)
            sql_insert="INSERT INTO dienthoai1 VALUES(:name,:brand,:display,:hdh,:camera_sau,:camera_truoc,:chip,:ram,:rom,:sim,:battery,:price,:danhgia,:sluong,:link)"
            dt1= dienthoai (name,brand,display,hdh,camera_sau,camera_truoc,chip,ram,rom,sim,battery,gia,danhgia,soluong,link)

            crawl_cellphones(dt1)

crawl_Cellphones()        
                
               

  