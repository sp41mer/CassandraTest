# -*- coding: utf-8 -*-
__author__ = 'sp41mer'
import json, requests, sys, logging, time, datetime
from models import Group
from vk_access_token import vk_access_token

method = "groups.search"
search_query = "материнский капитал"
response = requests.post('https://api.vk.com/method/' + method,
                            data={'q': search_query ,
                                  'count': 1000,
                                  'access_token':vk_access_token})
data = json.loads(response.text)
group_list = data['response'][1:]
for group in group_list:
    print group.get('name','')
    g = Group(
        vk_id = group.get('gid', ''),
        name = group.get('name',''),
        screen_name = group.get('screen_name', ''),
        type = group.get('type',''),
        photo_50 = group.get('photo_50',''),
        photo_100 = group.get('photo_100',''),
        photo_200 = group.get('photo_200','')
    )
    g.save()
    time.sleep(0.4)
