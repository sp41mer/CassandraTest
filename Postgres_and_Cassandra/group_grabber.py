__author__ = 'sp41mer'
import json, requests, sys, logging, time, datetime
from models import GroupNoSQL, FriendsNoSQL, User, Group
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from cassandra.auth import PlainTextAuthProvider
from vk_access_token import vk_access_token
import usefull


def write_to_cassandra_db():
    #for localhost
    # connection.setup(['127.0.0.1'], "parse_keyspace", protocol_version=3)
    # sync_table(GroupNoSQL)
    # sync_table(FriendsNoSQL)

    #for DigitalOcean
    auth_provider = PlainTextAuthProvider(username='rootuser', password='zatreschina')
    connection.setup(['178.62.205.208'], "parse_db", protocol_version=3, auth_provider=auth_provider)
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
                                      'v': 5.53,
                                      'access_token': vk_access_token})
        predata = json.loads(preresponse.text)
        counter = predata['response']['count']
        data = predata['response']['items']
        times = (counter//1000)+1
        time.sleep(0.4)
        if times > 1:
            for i in range(1, times):
                response = requests.post('https://api.vk.com/method/' + method,
                                    data={'group_id': group_id,
                                          'sort': 'id_asc',
                                          'offset': 1000*i,
                                          'count': 1000,
                                          'v': 5.53,
                                          'access_token': vk_access_token})
                jsondata = json.loads(response.text)
                data = data + jsondata['response']['items']
                time.sleep(0.4)
                print group.name + ' offset ' + str(1000*i)
        try:
            members_array = list(usefull.chunks(data, 65000))
            GroupNoSQL.create(vk_id=group_id,
                            members=set(usefull.safe_list_get (members_array, 0, {0})),
                            members_65p = set(usefull.safe_list_get (members_array, 1, {0})),
                            members_130p = set(usefull.safe_list_get (members_array, 2, {0})),
                            members_195p = set(usefull.safe_list_get (members_array, 3, {0})),
                            members_260p = set(usefull.safe_list_get (members_array, 4, {0})),
                            members_325p = set(usefull.safe_list_get (members_array, 5, {0})),
                            members_390p = set(usefull.safe_list_get (members_array, 6, {0})),
                            members_455p = set(usefull.safe_list_get (members_array, 7, {0})),
                            members_520p = set(usefull.safe_list_get (members_array, 8, {0})),
                            members_585p = set(usefull.safe_list_get (members_array, 9, {0})),
                            members_650p = set(usefull.safe_list_get (members_array, 10, {0})),
                            members_715p = set(usefull.safe_list_get (members_array, 11, {0})),
                            members_780p = set(usefull.safe_list_get (members_array, 12, {0})),
                            members_845p = set(usefull.safe_list_get (members_array, 13, {0})),
                            members_910p = set(usefull.safe_list_get (members_array, 14, {0})),
                            members_975p = set(usefull.safe_list_get (members_array, 15, {0})))
        except Exception, e:
            print str(e)
            print predata
        print group.name + ' finished'
        time.sleep(0.4)


