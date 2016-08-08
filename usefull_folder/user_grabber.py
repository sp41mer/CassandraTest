#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==============
#      Main script file
# ==============
from __future__ import division
import json, requests, sys, logging, time, datetime
import peewee

from models import Parsing, User

# ===============
reload(sys)
sys.setdefaultencoding('utf-8')
logging.basicConfig(format='%(asctime)s %(message)s', filename='group_onliners.log', level=logging.WARNING)
# ===============
method = "users.getFollowers"
vk_id = 53083705
fields = 'exports,personal,occupation,connections,sex,country,city,bdate,sex,deactivated,has_photo,contacts,status,last_seen,followers_count,online,relation,interests'
preresponse = requests.post('https://api.vk.com/method/' + method, data={'user_id': vk_id, 'count': 1, 'v': '5.5'})
predata = json.loads(preresponse.text)
print predata['response']['count']
pstart = parsing.current_offset
for i in xrange(pstart, parsing.total_users, parsing.offset):
    apreresponse = requests.post('https://api.vk.com/method/' + method,
                                 data={'user_id': vk_id, 'fields': fields, 'count': parsing.offset, 'v': '5.50'})
    predata = json.loads(apreresponse.text)
    if len(predata['response']['items']):
        for user in predata['response']['items']:
            # try:
            # print user
            vk_user = User(
                vk_id=user.get('id'),
                first_name=user.get('first_name'),
                last_name=user.get('last_name'),
                sex=user.get('sex'),
                bdate=user.get('bdate'),
                status=user.get('status'),
                deactivated=user.get('deactivated'),
                has_photo=user.get('has_photo'),
                mobile_phone=user.get('mobile_phone'),
                home_phone=user.get('home_phone'),
                skype=user.get('skype'),
                facebook=user.get('facebook'),
                twitter=user.get('twitter'),
                livejournal=user.get('livejournal'),
                instagram=user.get('instagram'),
                political=user.get('political'),
                religion=user.get('religion'),
                people_main=user.get('people_main'),
                life_main=user.get('life_main'),
                smoking=user.get('smoking'),
                alcohol=user.get('alcohol'),
                inspired_by=user.get('inspired_by'),
                online=user.get('online'),
                online_app=user.get('online_app'),
                online_mobile=user.get('online_mobile'),
                relation=user.get('relation'),
                interests=user.get('interests'),
                parsing_id=parsing
            )
            if user.get('occupation'):
                vk_user.occupation_type = user.get('occupation').get('type')
                vk_user.occupation_id = user.get('occupation').get('id')
                vk_user.occupation_name = user.get('occupation').get('name')
            if user.get('country'):
                vk_user.country_id = user.get('country').get('id')
                vk_user.country_title = user.get('country').get('title')
            if user.get('city'):
                vk_user.city_id = user.get('city').get('id')
                vk_user.city_title = user.get('city').get('title')
            if user.get('last_seen'):
                vk_user.last_seen_time = user.get('last_seen').get('time')
                vk_user.last_seen_platform = user.get('last_seen').get('platform')
            # except Exception:
            # 	print 'error'
            vk_user.save()
    else:
        print "no reply"
        sys.exit()
    time.sleep(2)
