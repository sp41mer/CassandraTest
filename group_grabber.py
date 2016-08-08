import json, requests, sys, logging, time, datetime
from models import GroupNoSQL, FriendsNoSQL
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table

connection.setup(['127.0.0.1'], "mykeyspace", protocol_version=3)
sync_table(GroupNoSQL)
sync_table(FriendsNoSQL)

method = "groups.getMembers"
group_id = '48273281'
preresponse = requests.post('https://api.vk.com/method/' + method,
                            data={'group_id': group_id,
                                  'sort': 'id_asc',
                                  'offset': 0,
                                  'count': 1000})
predata = json.loads(preresponse.text)

GroupNoSQL.create(vk_id=group_id, members=set(predata['response']['users']))

q = GroupNoSQL.objects(vk_id=group_id)

for user in q[0].members:
    method = "friends.get"
    user_id = user
    response = requests.post('https://api.vk.com/method/' + method,
                             data={'user_id': user_id})
    data = json.loads(response.text)
    try:
        friends = data['response']
        FriendsNoSQL.create(vk_id=str(user_id), friends=friends)
    except Exception:
        print str(user_id)+' '+data['error']['error_msg']
    time.sleep(1)

