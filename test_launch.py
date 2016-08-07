# -*- coding: utf-8 -*-
__author__ = 'sp41mer'
from bs4 import BeautifulSoup
import json, sys
import requests
from cassandra.cluster import Cluster

reload(sys)
sys.setdefaultencoding('utf-8')

#initial connection Cassandra
cluster = Cluster()
session = cluster.connect('repetitors')

#initial connections for BeautifulSoup
parenturl = 'http://www.virtualacademy.ru'
repetitors_array = []
url = 'www.virtualacademy.ru/repetitory/po-anglyskomu-yazyku/'
r = requests.get("http://" + url)
data = r.text
soup = BeautifulSoup(data)
id = 1
# get every repetitor on the page
for repetitor in soup.find_all('div', attrs={'class': 'result-questionnaire'}):
    # get avatar photo
    ava_url = repetitor.find('div', attrs={'class': 'l-column'}).find('img').get('src')
    content = repetitor.find('div', attrs={'class': 'r-column'})
    name = content.find('div', attrs={'class': 'result-questionnaire-header'}).text
    info = content.find('ul', attrs={'class': 'result-questionnaire-content'})
    iter = 0
    repetitor_info = ['0','0','0','0','0','0']
    for piece_of_info in info.find_all('li'):
        repetitor_info[iter] = piece_of_info.text
        iter += 1
    session.execute("""
        INSERT INTO users (rep_id,avatar,name,subject,education,cost,type,subway)
        VALUES ({},'{}','{}', '{}', '{}','{}','{}', '{}')
        """.format(id,
                   parenturl+ava_url,
                   name,
                   repetitor_info[0],
                   repetitor_info[1],
                   repetitor_info[2],
                   repetitor_info[3],
                   repetitor_info[4]))
    #make array of repetitors
    repetitors_array.append({
        'avatar': parenturl+ava_url,
        'name': name,
        'subject': repetitor_info[0],
        'education': repetitor_info[1],
        'cost': repetitor_info[2],
        'type':  repetitor_info[3],
        'subway': repetitor_info[4],
        'comment': repetitor_info[5]
        })
    id += 1

