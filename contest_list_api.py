#!/usr/bin/env python
# coding: utf-8

# In[6]:


import json
import re
# DO NOT import this after requests
import grequests
import requests
import os
from datetime import datetime, timedelta

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from dateutil import parser

class Contest:
    def contest_list(self):
        contest_list=[]

        #Atcoder
        url = 'https://atcoder.jp/contests'
        page = requests.get(url)

        if page.status_code ==200:
            soup = BeautifulSoup(page.text, 'html.parser')
            upcoming_contests=soup.find_all('div',id='contest-table-upcoming')
            if(len(upcoming_contests)>0):
                upcoming_contest_list=upcoming_contests[0].find_all('tr')
                cn=0
                for contest in upcoming_contest_list:
                    contest_detail=contest.find_all('td')
                    if(cn==1):
                        hms = contest_detail[2].text
                        a = hms.split(':')
                        seconds = int(a[0]) * 60 * 60 + int(a[1]) * 60
                        detail={
                            "site":"AtCoder",
                            "name":contest_detail[1].text.split("\n")[3],
                            "url":"https://atcoder.jp"+contest_detail[1].find_all('a')[0]['href'],
                            "start_time":contest_detail[0].text,
                            "duration":str(seconds)
                        }
                        contest_list.append(detail)
                    cn=1

            active_contests=soup.find_all('div',id='contest-table-action')
            if(len(active_contests)>0):
                active_contest_list=active_contests[0].find_all('tr')
                cn=0
                for contest in active_contest_list:
                    contest_detail=contest.find_all('td')
                    if(cn==1):
                        hms = contest_detail[2].text
                        a = hms.split(':')
                        seconds = int(a[0]) * 60 * 60 + int(a[1]) * 60
                        detail={
                            "site":"AtCoder",
                            "name":contest_detail[1].text.split("\n")[3],
                            "url":"https://atcoder.jp"+contest_detail[1].find_all('a')[0]['href'],
                            "start_time":contest_detail[0].text,
                            "duration":str(seconds)
                        }
                        contest_list.append(detail)
                    cn=1

        #codechef
        url = 'https://www.codechef.com/api/list/contests/all?sort_by=START&sorting_order=asc&offset=0&mode=all'
        page = requests.get(url)

        if page.status_code==200:

            codechef_json=page.json()

            ####upcoming contest

            for data in codechef_json['future_contests']:
                detail={
                            "site":"CodeChef",
                            "name":data['contest_name'],
                            "url":"https://www.codechef.com/contests/"+data['contest_code'],
                            "start_time":data['contest_start_date_iso'],
                            "duration":str((int)(data['contest_duration'])*60)
                        }
                contest_list.append(detail)

            ####present contest\

            for data in codechef_json['present_contests']:
                detail={
                            "site":"CodeChef",
                            "name":data['contest_name'],
                            "url":"https://www.codechef.com/contests/"+data['contest_code'],
                            "start_time":data['contest_start_date_iso'],
                            "duration":str((int)(data['contest_duration'])*60)
                        }
                contest_list.append(detail)


        #codeforces
        url = 'https://codeforces.com/api/contest.list'
        page = requests.get(url)

        if page.status_code == 200:

            codeforces_json=page.json()

            for data in codeforces_json['result']:
                if(data['phase']=='BEFORE'):
                    detail={
                            "site":"CodeForces",
                            "name":data['name'],
                            "url":"https://codeforces.com/contest/"+str(data['id']),
                            "start_time":datetime.fromtimestamp(data['startTimeSeconds']).isoformat(),
                            "duration":str(data['durationSeconds'])
                    }
                    contest_list.append(detail)
                else:
                    break
            #print(contest_list)

        #leetcode
        url = 'https://leetcode.com/graphql?query={%20allContests%20{%20title%20titleSlug%20startTime%20duration%20__typename%20}%20}'
        page = requests.get(url)

        if page.status_code == 200:

            leetcode_json=page.json()

            for data in leetcode_json['data']['allContests']:
                start_time=datetime.fromtimestamp(data['startTime']).isoformat()
                DT = parser.parse(start_time)
                end_time=DT+timedelta(seconds=data['duration'])
                if datetime.now() > end_time:
                    continue
                else:
                    detail={
                            "site":"LeetCode",
                            "name":data['title'],
                            "url":"https://leetcode.com/contest/"+str(data['titleSlug']),
                            "start_time":start_time,
                            "duration":str(data['duration'])
                    }
                    contest_list.append(detail)
        return contest_list
if __name__ == '__main__':
    contest=Contest()
    print(contest.contest_list())


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




