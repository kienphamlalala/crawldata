
#%%

from selenium import webdriver
from bs4 import BeautifulSoup 
import pandas as pd
import csv
import time
driver=webdriver.Edge('D:\VISUAL\python\CrawlDataFromWeb\msedgedriver.exe')
def init (url):
    #driver=webdriver.Edge('D:\VISUAL\python\CrawlDataFromWeb\msedgedriver.exe')
    url='https://www.thegioididong.com'
    driver.get(url)
    dt=driver.find_element_by_xpath('/html/body/header/div[2]/div/ul/li[1]/a/span') 
    dt.click()

#%%

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

numPg=3
    
Url_all=[]
  
for i in range(numPg):
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)') # thực hiện kéo xuống xuối cuối trang 
    next_btn=driver.find_element_by_xpath('//*[@id="categoryPage"]/div[3]/div[2]/a')
    next_btn.click()
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)') # thực hiện kéo xuống xuối cuối trang 
Url_each_page=GetUrl() 

Url_all=Url_all+Url_each_page  

time.sleep(8)
 



with open('d1.csv','w',newline='',encoding='utf-8')as file_output:
    #ghi ra các tiêu đề cột
    header=['Name','Brand','Display','HDH','Camera sau','Camera trước','Chip','Ram','Rom','Sim','Battery','Charge','Gia','Danh gia','So Luong','Link','Tên cửa hàng']
    #tạo ra các tiêu đề cột
    writer =csv.DictWriter(file_output,fieldnames=header)
    writer.writeheader() 
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
            
            print(name,display2,hdh,camera_sau,camera_truoc,chip,ram,rom,sim,battery,charge,gia,danhgia,sluong)
        except AttributeError:
                danhgia='NULL'
                sluong=0
                #viết các thông tin vào file csv
                writer.writerow({ header[0]:name,header[1]:brand,header[2]:display2,header[3]:hdh,header[4]:camera_sau,header[5]:camera_truoc,header[6]:chip,header[7]:ram,header[8]:rom,header[9]:sim,header[10]:battery,header[11]:charge,header[12]:gia,header[13]:danhgia,header[14]:sluong,header[15]:link,header[16]:nameshop})
              
              
              #print(name,display2,hdh,camera_sau,camera_truoc,chip,ram,rom,sim,battery,charge,gia,danhgia,sluong)

                continue
       #print(name,display2,brand,hdh,camera_sau,camera_truoc,chip,ram,rom,sim,battery,charge,gia,danhgia,sluong)
        writer.writerow({ header[0]:name,header[1]:brand,header[2]:display2,header[3]:hdh,header[4]:camera_sau,header[5]:camera_truoc,header[6]:chip,header[7]:ram,header[8]:rom,header[9]:sim,header[10]:battery,header[11]:charge,header[12]:gia,header[13]:danhgia,header[14]:sluong,header[15]:link,header[16]:nameshop})
           
    
# %%
