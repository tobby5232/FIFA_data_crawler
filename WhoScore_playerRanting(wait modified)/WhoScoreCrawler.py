# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 14:47:36 2022

@author: ch406
"""
from bs4 import BeautifulSoup
import requests
import pandas as pd

url="https://fbref.com/en/comps/1/stats/World-Cup-Stats"
web=requests.get(url)
#get web object from url

soup=BeautifulSoup(web.text,"lxml")
#Set web as Beautiful object named as soup
tag_table=soup.find_all("tbody",limit=1)
#Find TBODY mark in soup



for row in tag_table:
    player=row.text
#Set player string from tag_table
print(player)

