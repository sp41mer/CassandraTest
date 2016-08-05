__author__ = 'sp41mer'
from bs4 import BeautifulSoup
import json
import requests
from cassandra.cluster import Cluster

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

session.execute(
    """
    INSERT INTO users (userid,name,age,email)
    VALUES ('{}','{}', {}, '{}')
    """.format('user2','Name of User 2',17,'email2@email.com')
)
rows = session.execute('SELECT name, age, email FROM users')
for user_row in rows:
    print user_row.name, user_row.age, user_row.email
