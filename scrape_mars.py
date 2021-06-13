#!/usr/bin/env python
# coding: utf-8

# In[2]:


#import dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import time
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pymongo
from flask import Flask, render_template, redirect
import pandas as pd


# In[3]:


# Set up Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=True)
# Visit website
url = "https://mars.nasa.gov/news/"
browser.visit(url)

    
# Scrape page into Soup
html = browser.html
soup = BeautifulSoup(html, "html.parser")


# In[4]:


# Retrieve the latest news title
latest_news_title = soup.find_all('div', class_='content_title')[1].text
latest_news_title


# In[5]:


# Retrieve the lastest paragraph text
latest_news_paragraph = soup.find_all('div', class_='article_teaser_body')[0].text
latest_news_paragraph


# In[6]:


print(latest_news_title)
print(f"-----------------------------------------------")
print(latest_news_paragraph)


# JPL Mars Space Images - Featured Image

# In[7]:


#visit url
jpl_url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"
browser.visit(jpl_url)


# In[8]:


#find and click the image button
full_image_element = browser.find_by_tag('button')[1]
full_image_element.click()


# In[9]:


# HTML object
html = browser.html
# Parse HTML
soup = BeautifulSoup(html,"html.parser")
# Retrieve image url
feature_image_url = soup.find_all('img', class_='headerimage fade-in')


# In[10]:


#find image url
img_url = soup.find('img', class_= 'fancybox-image').get('src')
img_url


# In[11]:


#use base url to create absolute url

absolute_url = f"https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html/{img_url}"
absolute_url


# Mars Facts

# In[ ]:


#use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
#use Pandas to convert the data to a HTML table string.


# In[12]:


# use pd.read_html to pull data from the 2nd table.
df = pd.read_html('https://space-facts.com/mars/')[1]
df


# In[13]:


#change index
df.columns = ['Description', 'Mars', 'Earth']
df.set_index('Description', inplace = True)
df


# In[14]:


#convert df to html format
df.to_html()


# In[15]:


print(df.to_html())


# Mars Hemisphere

# In[16]:


#visit url
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# In[17]:


# <a href="/search/map/Mars/Viking/cerberus_enhanced" class="itemLink product-item"><img class="thumb" src="/cache/images/39d3266553462198bd2fbc4d18fbed17_cerberus_enhanced.tif_thumb.png" alt="Cerberus Hemisphere Enhanced thumbnail"></a>
links = browser.find_by_css('a.product-item img')
links


# In[18]:


#check that there are 4 different links to correspond with the 4 different links provided on the page. 
len(links)


# In[19]:


# do a 'for' loop.  Loop to click on link, find 'sample' anchor tag, return href for all 4 of the links.

#create list to hold all images and titles
hemisphere_imageurl_title = []

for i in range(len(links)):
    hemisphere = {}
    
    #elements needed to be 'clicked' for each of the 4 loops
    browser.find_by_css('a.product-item img')[i].click()
    
    #sample anchor tag
    sample = browser.find_by_text('Sample').first
    hemisphere['img_url']= sample['href']
    
    #get title of hemisphere
    hemisphere['title'] = browser.find_by_css('h2.title').text
    
    #append 'hemisphere' object to 'hemisphere_imageurl_title' list
    hemisphere_imageurl_title.append(hemisphere)
    
    #click back to go back to page and start the next loop.
    browser.back()


# In[21]:


hemisphere_imageurl_title


# In[22]:


browser.quit()


# In[23]:


get_ipython().system('jupyter nbconvert --to script we.ipynb')


# In[ ]:




