#!/usr/bin/python3.12
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os
import sys
import csv

# 爬內文網址用的
def content_link(link2):
    web2 = requests.get(link2)
    soup2 = BeautifulSoup(web2.text, "lxml")
    item2_div=soup2.find('div','group-box headline__box')
    item2_h3=item2_div.find('h3').text
    item2_ul=item2_div.find('ul')
    item2_li=item2_ul.find_all('li')
    li_ay=[]
    li_ay.append(item2_h3)
    i=0
    for r in item2_li:
        result2=r.find('a').text
        li_ay.append(result2)
        i+=1
        if i==2:
            break
    return li_ay

url='https://www.ctee.com.tw/'
web = requests.get(url)
soup = BeautifulSoup(web.text, "lxml")
itemobj=soup.find('div','list-box livenews')

itemobj_ul=itemobj.find('ul')
itemobj_li=itemobj_ul.find_all('li')

finish=[]
i=0
for e in itemobj_li:
    time=e.find('time').text
    title=e.find('a').text
    link=e.find('a')['href']
    # 進入內文網址
    li_ay2=content_link(url+link)
    content=e.find('h4').text
    finish.append({
        '標題':title,
        '內文內容':li_ay2,
        '時間':time,
        '內文':content
    })

fn='chinatimes.csv'
with open(fn,mode='w', newline='', encoding='utf-8-sig') as csvFile:           #開啟csv檔案
    csvWriter=csv.writer(csvFile)
    csvWriter.writerow(['標題','內文內容','時間','內文'])
    for p in finish:
        content_str=''
        for p2 in p['內文內容']:
            content_str+=p2+','
        csvWriter.writerow([p['標題'],content_str,p['時間'],p['內文']])

print('完成')