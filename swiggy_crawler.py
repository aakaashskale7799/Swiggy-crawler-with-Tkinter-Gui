# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 13:25:39 2020
working
@author: User
"""
from selenium import  webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import webbrowser
import re
import csv
from random import random
import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
def new(link):
    #link = 'https://www.swiggy.com/'
    response = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    #driver= webdriver.Chrome()
    print("===================")
    #print(driver.current_url)
    #driver.get(link)
    #time.sleep(2)
    
    #print(driver.current_url)
    name = soup.find(class_="_1_sSy")
    name_list=name.find_all("a")
    cities=[]
    links=[]
    #name of the cities and their links extracted here
    for n in name_list:
        city=n.contents[0]
        #print(city)
        link="https://www.swiggy.com"+n.get("href")
        cities.append(city)
        links.append(link)
    list_of_tuples = list(zip(cities,links))
    df=pd.DataFrame(list_of_tuples, columns=["Cities","Links"])
    df.to_csv("city links.csv")
    print("done city")
    
    
def link(i):
    page=requests.get(i,headers={'User-Agent': 'Mozilla/5.0'})
    html = page.content
    #first landing page hotel names of the city
    soup=BeautifulSoup(html,"html.parser")
    cat=soup.findAll("div", {"class":"nA6kb"})
    if not cat:
        pass
    else:
        hotel_name=[]
        print("="*60)
        print("This hotel belongs to city",i)
        print("="*60)
        for name in cat:
            #hlink=cat.get
            hotel=name.get_text()
            hotel_name.append(hotel)
        #First landing page hotel's links
        name = soup.find(class_="_129-b")
        name_list=name.find_all("a")
        hlinks=[]
        for n in name_list:
            l=n.get("href")
            l=str(l)
            sw="https://www.swiggy.com"
            hlink=sw+l
            hlinks.append(hlink)
            for d in hlinks:
                if d=="https://www.swiggy.comNone":
                    hlinks.remove("https://www.swiggy.comNone")        
        #let's start collecting data beyond 1st page
        page_no=soup.find(class_="_2OmLw")
        new_page=page_no.find_all("a")
        page_nums=[]
        page_links=[]
        for x in new_page:
            l=x.get("href")
            l=str(l)
            sw="https://www.swiggy.com"
            hlink=sw+l
            page_nums.append(hlink)
            #print(page_nums)
        leng=len(page_nums)+1
        page_links=page_nums[1:leng]
        #page_nums=pagelinks[1:leng]
        for h in page_links:
             page=requests.get(h,headers={'User-Agent': 'Mozilla/5.0'})
             html = page.content
             #next page hotel names
             soup=BeautifulSoup(html,"html.parser")
             cat=soup.findAll("div", {"class":"nA6kb"})
             for name in cat:
                 #hlink=cat.get
                 hotel=name.get_text()
                 hotel_name.append(hotel)
             #here links of the hotels of the next page
             name = soup.find(class_="_129-b")
             name_list=name.find_all("a")
             for n in name_list:
                 l=str(n.get("href"))
                 #l=str(l)
                 sw="https://www.swiggy.com"
                 hlink=sw+l
                 hlinks.append(hlink) 
             for d in hlinks:
                 if d=="https://www.swiggy.comNone":
                     hlinks.remove("https://www.swiggy.comNone")
        list_of_tuples = list(zip(hotel_name,hlinks))
        df=pd.DataFrame(list_of_tuples, columns=["Hotel Name","Links"])
        #print("\n Printing df \n")
        file=soup.find("span",{"class":"kpkwa"})
        file_name=file.get_text()
        df.to_csv(file_name+".csv")
        print("done res")
    
#city=input("Enter city link :")
#link(city)   
    
