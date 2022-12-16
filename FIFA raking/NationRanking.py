# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 14:55:47 2022

@author: ch406
"""

import pandas as pd
import requests
import json

#%%
#Crawler FIFA ranking json

id=["141","152","8415","8779","9164","9507","9878","10243","10607",
   "10964","11328","11699","12070","12455","12833","13197","13554"]

year_list=list(i for i in range(2006,2023))

headers ={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }

team_allTime_df=pd.DataFrame(columns =['Country_Code','Total_Points','Previous_Rank','Year'])
for i in range(len(id)):
    url = "https://www.fifa.com/api/ranking-overview?locale=en&dateId=id"
    url = url + str(id[i])
    p_html = requests.get(url,headers=headers)
    data1 = p_html.text
    
    file_dic=json.loads(data1)
    file_list=file_dic["rankings"]
    team_df=pd.DataFrame(columns =['Country_Code','Total_Points','Previous_Rank','Year'])
    for j in range(len(file_list)):
        countryCode=file_list[j]['rankingItem']['countryCode']
        totalPoints=file_list[j]['rankingItem']['totalPoints']
        previousRank=file_list[j]['rankingItem']['previousRank']
        year=year_list[i]
        team_df.loc[j]=[countryCode,totalPoints,previousRank,year]
    print(team_df)
    team_allTime_df=team_allTime_df.append(team_df)
        
team_allTime_df=team_allTime_df.reset_index(drop=True)
print(team_allTime_df)


#%%
#Output CSV
team_allTime_df.to_csv("AllTime_ranking.csv", index = None)