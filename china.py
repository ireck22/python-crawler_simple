#!/usr/bin/python3.12
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os
import sys
import csv

headers={'User-Agent':'Mozilla/5.0(Windows NT 6.1; WOW64)\
         AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
         Safari/537.36'
}

url='https://www.chinatimes.com/world/?chdtv'
web = requests.get(url,headers=headers)
soup = BeautifulSoup(web.text, "lxml")
itemobj=soup.find_all('div','articlebox-compact')

finish=[]
i=0
for e in itemobj:
    if i>=2:
        tempfh=[]
        if e.find('h3'):
            t3=e.find('h3')
            title=t3.find('a').text             #標題
            link=t3.find('a')['href']           #連結
            tempfh.append([title,link])
        if e.find('div','meta-info'):
            d2=e.find('div','meta-info')
            date=d2.find('span','date').text    #日期 
            tempfh[0].append(date)
        finish.append(tempfh[0])
    i+=1

fn='china.csv'
with open(fn,mode='w', newline='', encoding='utf-8-sig') as csvFile:           #開啟csv檔案
    csvWriter=csv.writer(csvFile)
    csvWriter.writerow(['標題','連結','時間'])
    for p in finish:
        if len(p)>2:
            csvWriter.writerow([p[0],p[1],p[2]])

print('完成')