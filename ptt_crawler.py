#!/usr/bin/python3.12
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import sys
import csv
import pandas as pd

finish=list()
result=list()
key=int(input("請輸入頁數:"))+1

for i in range(1,key):
  url="https://www.ptt.cc/bbs/Beauty/index399"+str(i)+".html"
  web = requests.get(url,cookies={'over18':'1'})
  soup = BeautifulSoup(web.text, "lxml")
  link = soup.find_all('div',class_='title')
  for d in link:
    if d.find('a'):
      title=d.find('a').text  #這是標題
      link2=d.find('a')['href'] #這是連結
      link3="https://www.ptt.cc/"+link2
      tmp=[title,link3]
      result.append(tmp)
  finish.append(result)
  result=list()

#utf-8-sig 是防止中文亂碼的中文編碼
f = open('ptt_crawler.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(f, delimiter=',')
writer.writerow(['title', '連結'])

for e in finish:
  for result2 in e:
    # print(result2)
    writer.writerow(result2)

f.close()
print("完成寫入")    