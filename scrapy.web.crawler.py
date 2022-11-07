#!/usr/bin/env python
# coding: utf-8

# In[1]:


import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


# In[8]:


class SipSpider(CrawlSpider):
    name = 'sip'
    allowed_domains - ['sipwhiskey.com']
    start_urls = ['http://sipwhiskey.com/']


# In[11]:


rules = (
     Rule(LinkExtractor(allow='collections', deny='products')),
     Rule(LinkExtractor(allow='products'), callback='parse_item')
 )


# In[12]:


def parse_item(self,response):
    yield {
        'brand' : response.css('div.vendor a::text').get(),
        
    }


# In[ ]:




