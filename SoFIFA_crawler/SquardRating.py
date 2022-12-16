# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 17:33:21 2022

@author: ch406
"""

import numpy as np
import pandas as pd
import re
import requests
from bs4 import BeautifulSoup as Soup

#%%
column = ['nation','overall','attack','mid','defence','year']
FIFAdata = pd.DataFrame(columns = column)
r=["070002","080002","090002","100002","110002","120002","130034","140052","150059",
   "160058","170099","180084","190075","200061","210064","220069","230007"]
all_time_data=pd.DataFrame()


for i in range(len(r)):
    url = "https://sofifa.com/teams?type=national&r="
    url = url + str(r[i])+"&set=true"
    # print(url)
    year=int('20'+str(r[i])[0:2])-1
    print(year)
    p_html = requests.get(url)
    p_soup = p_html.text
    data = Soup(p_soup,'html.parser')
    table = data.find('tbody')
    print(type(table))
    for i in table.findAll('tr'):
        td = i.findAll('td')
        nation=td[1].find('a').text
        ova=td[2].find('span').text
        att=td[3].find('span').text
        mid=td[4].find('span').text
        defe=td[5].find('span').text
        
        team_data=pd.DataFrame([[nation,ova,att,mid,defe,year]],columns=column)
        all_time_data=all_time_data.append(team_data,ignore_index=True)

#%%
# print(all_time_data)


#%%
all_time_data.to_csv('AllTeamRating.csv', index = None)