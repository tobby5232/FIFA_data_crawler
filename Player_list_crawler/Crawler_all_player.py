# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 15:12:49 2022

@author: ch406
"""
from bs4 import BeautifulSoup
import requests
import pandas as pd

url="https://www.sportingnews.com/us/soccer/news/world-cup-squads-2022-team-rosters-official-fifa-qatar/kjcagctfesjt0zpjxctbdqha"
web=requests.get(url)
#get web object from url

soup=BeautifulSoup(web.text,"lxml")
#Set web as Beautiful object named as soup
tag_table=soup.find_all("tbody",limit=34)
#Find TBODY mark in soup

for row in tag_table:
    player=row.text
#Set player string from tag_table
player_list=player.split("\n")
#Seperate player into player list

table=[]
for i in range(0,len(player_list)-5,5):
    player_list2=[]
    for j in range(5):
        player_list2.append(player_list[i+j])
    table.append(player_list2)
# print(table)
#Transfer player_list into two dimention and ready to save as CSV file

df = pd.DataFrame(table,columns=table[0])
#Set table[0] as column title
df1=df.drop(0,axis=0)
#Drop column 1 due to column set as title 
df1.to_csv("player_data.csv")
#Save as CSV file