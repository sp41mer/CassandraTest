__author__ = 'sp41mer'
import json, requests, sys, logging, time, datetime
from models import GroupNoSQL, FriendsNoSQL, User, Group
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from cassandra.auth import PlainTextAuthProvider
from vk_access_token import vk_access_token


#for localhost
# connection.setup(['127.0.0.1'], "mykeyspace", protocol_version=3)
#for DigitalOcean
auth_provider = PlainTextAuthProvider(username='rootuser', password='zatreschina')
connection.setup(['178.62.205.208'], "parcer_v1", protocol_version=3, auth_provider=auth_provider)
sync_table(GroupNoSQL)
sync_table(FriendsNoSQL)


# for group in Group.select():
#     method = "groups.getMembers"
#     group_id = str(group.vk_id)
#     preresponse = requests.post('https://api.vk.com/method/' + method,
#                             data={'group_id': group_id,
#                                   'sort': 'id_asc',
#                                   'offset': 0,
#                                   'count': 1000,
#                                   'access_token': vk_access_token})
#     predata = json.loads(preresponse.text)
#
#     try:
#         GroupNoSQL.create(vk_id=group_id, members=set(predata['response']['users']))
#     except Exception,e:
#         print str(e)
#         print predata
#     print group.name
#     time.sleep(0.4)


