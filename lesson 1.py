# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 19:19:18 2017

@author: YIJU.TING
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html=urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs0bj=BeautifulSoup(html)

nameList=bs0bj.findAll('span',{'class':'green'})
for name in nameList:
    print(name.get_text())
    

html=urlopen('http://www.pythonscraping.com/pages/page3.html')
bs0bj=BeautifulSoup(html)

for child in bs0bj.find('table',{'id':'giftList'}).children :
    print(child)


bs0bj.findAll('table')


for sibling in bs0bj.find('table',{'id':'giftList'}).tr.next_siblings :
    print(sibling)
    
images=bs0bj.findAll('img',{'src':re.compile('\.\.\/img\/gifts/img.*\.jpg')})
myTag=bs0bj.table
imgtag.attrs
imgtag.attrs['src']
imgtag=images[0]

####################
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
pages=set()
def getLinks(pageUrl):
    global pages
    html=urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj=BeautifulSoup(html)
    for link in bsObj.findAll('a',href=re.compile('^(/wiki/)((?!:).)*$')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage=link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)
getLinks('')                
    
                



