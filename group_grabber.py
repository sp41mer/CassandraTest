__author__ = 'sp41mer'
import json, requests, sys, logging, time, datetime
from models import GroupNoSQL, FriendsNoSQL, User, Group
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from vk_access_token import vk_access_token

connection.setup(['127.0.0.1'], "mykeyspace", protocol_version=3)
sync_table(GroupNoSQL)
sync_table(FriendsNoSQL)

for group in Group.select():
    method = "groups.getMembers"
    group_id = str(group.vk_id)
    preresponse = requests.post('https://api.vk.com/method/' + method,
                            data={'group_id': group_id,
                                  'sort': 'id_asc',
                                  'offset': 0,
                                  'count': 1000,
                                  'access_token': vk_access_token})
    predata = json.loads(preresponse.text)

    GroupNoSQL.create(vk_id=group_id, members=set(predata['response']['users']))
    time.sleep(0.4)


