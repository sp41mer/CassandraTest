# -*- coding: utf-8 -*-
__author__ = 'sp41mer'
import json, requests, sys, logging, time, datetime
from models import Group
from vk_access_token import vk_access_token


def get_groups(query):
    method = "groups.search"
    search_query = query
    response = requests.post('https://api.vk.com/method/' + method,
                                data={'q': search_query,
                                      'count': 1000,
                                      'v': 5.53,
                                      'access_token': vk_access_token})
    data = json.loads(response.text)
    print data
    group_list = data['response']['items']
    for group in group_list:
        print group.get('name', '')
        new_group = Group(
            vk_id=group.get('id', ''),
            query_string= search_query,
            name=group.get('name', ''),
            screen_name=group.get('screen_name', ''),
            type=group.get('type', ''),
            photo_50=group.get('photo_50', ''),
            photo_100=group.get('photo_100', ''),
            photo_200=group.get('photo_200', '')
        )
        new_group.save()
        # time.sleep(0.4)
