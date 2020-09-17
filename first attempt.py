#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup as soup
from IPython.display import Image
import pandas as pd


# In[2]:


query= "mats"


# In[3]:


url="https://www.snapdeal.com/search?"


# In[4]:


params={"keyword":query}


# In[5]:


r=requests.get(url,params=params)


# In[6]:


r.url


# In[7]:


sd=soup(r.content)


# In[8]:


content=sd.findAll("div",attrs = {"class":"product-tuple-listing"})
# content[0]


# In[9]:


len(content)


# In[10]:


pr=sd.findAll('span',{'class':'lfloat product-price'})
pc=[]
for i in pr:
    pc.append(i.text)
# print(pri)    


# In[11]:


tt=sd.findAll('p', attrs = {"class": "product-title"})
title=[]
for j in tt:
    title.append(j.text)
# print(title ) 


# In[65]:


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

# In[37]:


url2="https://www.shopclues.com/search?"


# In[38]:


params2={"q":query}


# In[39]:


r2=requests.get(url2,params=params2)


# In[40]:


r2.url


# In[41]:


sp=soup(r2.content)


# In[42]:


content2=sp.find("div",attrs = {"id":"product-list"})
col=sp.findAll("div",attrs = {"class":"column col3 search_blocks"})


# In[43]:


len(col)


# In[44]:


pr=sp.findAll('span',{'class':'p_price'})
pr[0].text
len(pr)


# In[45]:


col[0].img.attrs['data-img']


# In[46]:


pri=[]
for i in pr:
    pri.append(i.text)


# In[47]:


nam=[]
for j in col:
    nam.append(j.h2.text)
with open('try.csv',"w") as file:
    for i in nam:
        file.write(i)
        file.write('\n')
    


# In[48]:


rd={"name":nam,"price":pri}
pk=pd.DataFrame(rd)


# In[51]:


pk.head()


# In[63]:


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


# In[ ]:




