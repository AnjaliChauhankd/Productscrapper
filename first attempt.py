import requests
from bs4 import BeautifulSoup as soup
from IPython.display import Image
import pandas as pd


query= "mats"

url="https://www.snapdeal.com/search?"

params={"keyword":query}

r=requests.get(url,params=params)

r.url


sd=soup(r.content)


content=sd.findAll("div",attrs = {"class":"product-tuple-listing"})

# len(content)

pr=sd.findAll('span',{'class':'lfloat product-price'})
pc=[]
for i in pr:
    pc.append(i.text)
# print(pri)    

tt=sd.findAll('p', attrs = {"class": "product-title"})
title=[]
for j in tt:
    title.append(j.text)
# print(title ) 


with open('final.csv','w') as file:
    for i in range(len(content)):
        imgs=content[i].find('img')
        if 'src' in imgs.attrs:
            url2=imgs.attrs['src']
        else:
            url2=imgs.attrs['data-src']
        
        file.write(url2+'\n'+title[i]+'\nPrice:'+pc[i]+'\n'+'\n')
        display(Image(url=url2,width=50,height=50))
        print(title[i]+'\nPrice:'+pc[i])


# # Shopclues

url2="https://www.shopclues.com/search?"

params2={"q":query}

r2=requests.get(url2,params=params2)

r2.url

sp=soup(r2.content)

content2=sp.find("div",attrs = {"id":"product-list"})
col=sp.findAll("div",attrs = {"class":"column col3 search_blocks"})

# len(col)

pr=sp.findAll('span',{'class':'p_price'})
pr[0].text
# len(pr)

pri=[]
for i in pr:
    pri.append(i.text)

nam=[]
for j in col:
    nam.append(j.h2.text)


rd={"name":nam,"price":pri}

print('\n\nSHOPCLUES\n\n')
with open('final2.csv','w') as file:
    for i in range(len(col)):
        imgs=col[i].find('img')
        if 'data-img' in imgs.attrs:
            url3=imgs.attrs['data-img']
        else:
            url3=imgs.attrs['src']
     
        file.write(url3+'\n'+nam[i]+'\nPrice:'+pri[i]+'\n')
        display(Image(url=url3,width=50,height=50))
        print(nam[i]+'\nPrice:'+pri[i])
