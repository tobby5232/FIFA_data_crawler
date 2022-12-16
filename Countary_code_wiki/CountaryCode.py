# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 20:54:17 2022

@author: ch406
"""

import numpy as np
import pandas as pd
import re
import requests
from bs4 import BeautifulSoup as Soup

url = "https://en.wikipedia.org/wiki/List_of_FIFA_country_codes"
all_data=pd.DataFrame()
column=['Country','Country_Code']

p_html = requests.get(url)
p_soup = p_html.text
data = Soup(p_soup,'html.parser')
for j in range(4):
    table_all = data.findAll('tbody')
    table=table_all[j]
    for i in range(1,len(table.findAll('tr'))):
        td = table.findAll('tr')[i].findAll('td')
        # print(td)
        nation=td[0].find('a').text
        code=td[1].text.strip('\n')
        print(code)
        
        code_data=pd.DataFrame([[nation,code]],columns=column)
        all_data=all_data.append(code_data,ignore_index=True)
        
print(all_data.info())

all_data.to_csv('Country_code.csv', index = None)