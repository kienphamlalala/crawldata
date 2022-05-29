#%%
import sqlite3
from black import GitWildMatchPatternError

from selenium import webdriver
from bs4 import BeautifulSoup 
import pandas as pd
import csv
import time

from classdt import *


def deletetable():
    conn = sqlite3.connect('dienthoai.db')
    c = conn.cursor()
    c.execute("DELETE FROM dienthoaiall")
def crawl_cua_tgdd(numPg):
    try:
        conn = sqlite3.connect('dienthoai.db')
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS dienthoaiall(
                    
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
        #c.execute("DELETE FROM dienthoaiall")

        driver=webdriver.Edge('D:\VISUAL\python\CrawlDataFromWeb\msedgedriver.exe')

        def crawl_tgdd(dienthoai):
            with conn:
                id=1
                c.execute(sql_insert,{'ID':id,'name':dienthoai.name,'brand':dienthoai.brand,'display':dienthoai.display,'hdh':dienthoai.hdh,'camera_sau':dienthoai.camera_sau,'camera_truoc':dienthoai.camera_truoc,'chip':dienthoai.chip,'ram':dienthoai.ram,'rom':dienthoai.rom,'sim':dienthoai.sim,'battery':dienthoai.battery,'price':dienthoai.price,'danhgia':dienthoai.danhgia,'sluong':dienthoai.sluong,'link':dienthoai.link})
        #driver=webdriver.Edge('D:\VISUAL\python\CrawlDataFromWeb\msedgedriver.exe')
        url='https://www.thegioididong.com'
        driver.get(url)
        dt=driver.find_element_by_xpath('/html/body/header/div[2]/div/ul/li[1]/a/span') 
        dt.click()



        def GetUrl():
            
            page_s=BeautifulSoup(driver.page_source) 
            tel_infors=page_s.find_all('a',class_='main-contain') 
        
            all_prod=[]
            for tel_infor in tel_infors:
                tel_ID=tel_infor.get('href')
                tel_If_url='https://www.thegioididong.com'+tel_ID
                if tel_If_url not in all_prod: 
                    all_prod.append(tel_If_url)
            set(all_prod)
            return all_prod

   
            
        Url_all=[]
        
        for i in range(numPg):
            driver.execute_script('window.scrollTo(0,document.body.scrollHeight)') # thực hiện kéo xuống xuối cuối trang 
            next_btn=driver.find_element_by_xpath('//*[@id="categoryPage"]/div[3]/div[2]/a')
            next_btn.click()
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)') # thực hiện kéo xuống xuối cuối trang 
        Url_each_page=GetUrl() 
        
        Url_all=Url_all+Url_each_page  
        time.sleep(5)
        for url in Url_all:
            driver.get(url) #mở web chứa các thông tin chi tiết
            page_source=BeautifulSoup(driver.page_source,"html.parser") #dùng bs4 tải toàn bộ HTML document lên chương trình
            display=[]
            div1=page_source.find('div',class_='parameter')
            #hàm xử lý để tách tên của thiết bị
            try :
                name=page_source.find('h1').get_text()
                tmp_brand=page_source.find('h1').get_text()
                brand=tmp_brand.split(' ')[2]
                # hàm try except để tránh lỗi khi máy không có thông tin như máy mới ra mới phát hành
            except AttributeError:
                name='null'
                continue
            try:
                for a in div1.find('div',class_='liright'):
                    if a.get_text()!='\n':
                        display.append(a.get_text())
            except AttributeError:
                continue
            display2= ",".join(display)#Thông tin màn hình
            path_li=div1.find_all('li')
            #print(type(hdh_path))
            #vì trong các thành phần được trích xuất từ bs4 có dạng mảng nên ta có thể trích xuất các phần tử
            # ở đây ta trích xuất phần tử từ trên xuống theo các phần tử có được trích xuất từ web 
            hdh=path_li[1].find('span').get_text() #Lấy thông tin hệ điều hành
            camera_sau=path_li[2].find('span').get_text() #Lấy thông tin camera sau
            camera_truoc=path_li[3].find('span').get_text() #Lấy thông tin camera trước
            try :
                chip=path_li[4].find('span').get_text() #Lấy thông tin chip
            except AttributeError:
                continue
            ram=path_li[5].find('span').get_text() #Lấy thông tin ram
            rom=path_li[6].find('span').get_text() #Lấy thông tin rom
            try:
                sim=path_li[7].find('span').get_text() #Lấy thông tin sim
            except AttributeError:
                continue
            except IndexError:
                continue
            try:
                gia=page_source.find('p',class_='box-price-present').get_text() #Lấy thông tin giá
                gia=gia.replace('₫','')
                gia=gia.replace('*','')
                gia=gia.replace(' ','')
                gia=int(gia.replace('.',''))
            except AttributeError:
                continue
            
            battery=''
            charge=''
            nameshop="Thế giới di động"
            link=url
            i=0
            #hàm xử lý tách các thông tin pin
            for tmp in  path_li[8].find('div'):
                if i==0 and tmp.get_text()!='\n':
                    battery=battery+tmp.get_text()
                    i=i+1
                else:
                    charge=charge+tmp.get_text().strip()
            try :
                danhgia=page_source.find('p',class_='point').get_text() #Lấy thông tin đánh giá
                tmp=page_source.find('p',class_="detail-rate-total").get_text() #Lấy thông tin số lượng
                tmp=int(tmp.split(' ')[0])
                sluong=tmp
                
            
            except AttributeError:
                

                    continue
            #INSERT ALL DATA TO DATABASE
            print(name ,brand,display2,hdh,camera_sau,camera_truoc,chip,ram,rom,sim,battery,gia,danhgia,sluong,link,nameshop)
            sql_insert=f"""INSERT INTO dienthoaiall VALUES (:ID,:name,:brand,:display,:hdh,:camera_sau,:camera_truoc,:chip,:ram,:rom,:sim,:battery,:price,:danhgia,:sluong,:link)"""
            dt1= dienthoai (name,brand,display2,hdh,camera_sau,camera_truoc,chip,ram,rom,sim,battery,gia,danhgia,sluong,link)
            
            crawl_tgdd(dt1)
          
            
    except IndexError:
        c.close()
        #driver.close()
    except TypeError:
        c.close() 
def crawl_Cellphones(numPg):
    try:

        conn = sqlite3.connect('dienthoai.db')
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS dienthoaiall(
                    
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
        #c.execute("DELETE FROM dienthoaiall")
        def crawl_cellphones(dienthoai):
            with conn:
                id=1
                c.execute(sql_insert,{'ID':id,'name':dienthoai.name,'brand':dienthoai.brand,'display':dienthoai.display,'hdh':dienthoai.hdh,'camera_sau':dienthoai.camera_sau,'camera_truoc':dienthoai.camera_truoc,'chip':dienthoai.chip,'ram':dienthoai.ram,'rom':dienthoai.rom,'sim':dienthoai.sim,'battery':dienthoai.battery,'price':dienthoai.price,'danhgia':dienthoai.danhgia,'sluong':dienthoai.sluong,'link':dienthoai.link})
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


        
        Url_all=[]
        for i in range(numPg):
            #sroll down until found element next button 
            driver.execute_script("arguments[0].scrollIntoView();", driver.find_element_by_xpath("/html/body/div[1]/div/section/div/div[5]/div/a"))
            driver.execute_script("window.scrollBy(0, -150);")
            e=driver.find_element_by_xpath("/html/body/div[1]/div/section/div/div[5]/div/a")
            e.click()
        time.sleep(3)

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
              
                link=url
                
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
                name=name.strip()

        
                name=name.replace('\n','')
                brand=name.split(' ')[0]
            
                brand=brand.strip()
                print(name,brand,display,hdh,camera_sau,camera_truoc,chip,ram,rom,sim,battery,gia,danhgia,soluong,link)
                sql_insert="INSERT INTO dienthoaiall VALUES(:ID,:name,:brand,:display,:hdh,:camera_sau,:camera_truoc,:chip,:ram,:rom,:sim,:battery,:price,:danhgia,:sluong,:link)"
                dt1= dienthoai (name,brand,display,hdh,camera_sau,camera_truoc,chip,ram,rom,sim,battery,gia,danhgia,soluong,link)

                crawl_cellphones(dt1)
           
          
    
    except IndexError:
        c.close()
        #driver.close()
    except TypeError:
        c.close()     
def Crawl_cua_FPT(numPg):

    try:
        conn = sqlite3.connect('dienthoai.db')
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS dienthoaiall(
                    
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
        #c.execute("DELETE FROM dienthoaiall")
        def crawl_tgdd(dienthoai):
            with conn:
                id=1
                c.execute(sql_insert,{'ID':id,'name':dienthoai.name,'brand':dienthoai.brand,'display':dienthoai.display,'hdh':dienthoai.hdh,'camera_sau':dienthoai.camera_sau,'camera_truoc':dienthoai.camera_truoc,'chip':dienthoai.chip,'ram':dienthoai.ram,'rom':dienthoai.rom,'sim':dienthoai.sim,'battery':dienthoai.battery,'price':dienthoai.price,'danhgia':dienthoai.danhgia,'sluong':dienthoai.sluong,'link':dienthoai.link})
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
            if(brand=="Oppo"):
                brand="OPPO"
            
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
            sql_insert="INSERT INTO dienthoaiall VALUES(:ID,:name,:brand,:display,:hdh,:camera_sau,:camera_truoc,:chip,:ram,:rom,:sim,:battery,:price,:danhgia,:sluong,:link)"
            dt1= dienthoai (name,brand,display,hdh,camera_sau,camera_truoc,cpu,ram,rom,sim,battery,gia,danhgia,soluong,link)
            
            crawl_tgdd(dt1)
            
        
        c.close() 

    except IndexError:
        c.close()
        #driver.close()
    except TypeError:
        c.close()     


