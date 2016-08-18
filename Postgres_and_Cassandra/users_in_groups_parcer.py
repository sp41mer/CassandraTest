__author__ = 'sp41mer'
import json, requests, sys, logging, time, datetime
from models import GroupNoSQL, FriendsNoSQL, User, Group
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from cassandra.auth import PlainTextAuthProvider
from vk_access_token import vk_access_token
import usefull


def parse_users_from_groups():
    fields = 'exports,personal,occupation,connections,sex,country,city,' \
             'bdate,sex,deactivated,has_photo,contacts,status,last_seen,' \
             'followers_count,online,relation,interests'

    auth_provider = PlainTextAuthProvider(username='rootuser', password='zatreschina')
    connection.setup(['178.62.205.208'], "parse_db", protocol_version=3, auth_provider=auth_provider)
    sync_table(GroupNoSQL)
    sync_table(FriendsNoSQL)

    for group in Group.select():
        group_id = group.vk_id
        print group.name
        print group.query_string
        q = GroupNoSQL.objects.filter(vk_id=group_id)
        data = q[0].members + q[0].members_65p + q[0].members_130p + q[0].members_195p + \
               q[0].members_260p + q[0].members_325p +q[0].members_390p + \
               q[0].members_455p + q[0].members_520p + q[0].members_585p + \
               q[0].members_650p + q[0].members_715p + q[0].members_780p + \
               q[0].members_845p + q[0].members_910p + q[0].members_975p
        data = [x for x in data if x != 0]
        data_array = list(usefull.chunks(data, 999))

        for info_array in data_array:
            user_ids = info_array
            #grabbing friends to Cassandra
            # method = "friends.get"
            # response = requests.post('https://api.vk.com/method/' + method,
            #                          data={'user_id': user_id,
            #                                'access_token': vk_access_token})
            # data = json.loads(response.text)
            # try:
            #     friends = data['response']
            #     FriendsNoSQL.create(vk_id=str(user_id), friends=friends)
            # except Exception:
            #     print str(user_id)+' '+data['error']['error_msg']
            #grab info to PotsgresSQL
            method = "users.get"
            string = str(user_ids).strip('[]')
            response = requests.post('https://api.vk.com/method/' + method,
                                     data={'user_ids': string.replace(" ", ""),
                                           'fields': fields,
                                           'v': 5.53,
                                           'access_token': vk_access_token})
            data = json.loads(response.text)
            for info in data['response']:
                try:
                    a = User(
                        vk_id=info.get('id', None),
                        first_name=info.get('first_name', None),
                        last_name=info.get('last_name', None),
                        sex=info.get('sex', None),
                        bdate=info.get('bdate', None),
                        status=info.get('status', None),
                        deactivated=info.get('deactivated', None),
                        has_photo=info.get('has_photo', None),
                        mobile_phone=info.get('mobile_phone', None),
                        home_phone=info.get('home_phone', None),
                        skype=info.get('skype', None),
                        facebook=info.get('facebook', None),
                        twitter=info.get('twitter', None),
                        livejournal=info.get('livejournal', None),
                        instagram=info.get('instagram', None),
                        political=info.get('political', None),
                        religion=info.get('religion', None),
                        people_main=info.get('people_main', None),
                        life_main=info.get('life_main', None),
                        smoking=info.get('smoking', None),
                        alcohol=info.get('alcohol', None),
                        inspired_by=info.get('inspired_by', None),
                        online=info.get('online', None),
                        online_app=info.get('online_app', None),
                        online_mobile=info.get('online_mobile', None),
                        relation=info.get('relation', None),
                        interests=info.get('interests', None),
                        country_id=info.get('country', None),
                        city_id=info.get('city', None)
                    )
                    if info.get('occupation', None):
                        a.occupation_type = info.get('occupation').get('type', None)
                        a.occupation_id = info.get('occupation').get('id', None)
                        a.occupation_name = info.get('occupation').get('name', None)
                    if info.get('country'):
                        a.country_id = info.get('country').get('id')
                        a.country_title = info.get('country').get('title')
                    if info.get('city'):
                        a.city_id = info.get('city').get('id')
                        a.city_title = info.get('city').get('title')
                    if info.get('last_seen', None):
                        a.last_seen_time = info.get('last_seen').get('time', None)
                        a.last_seen_platform = info.get('last_seen').get('platform', None)
                    a.save()
                    print info.get('last_name', None)
                except Exception, e:
                    print str(e)
                    print data

            time.sleep(0.4)



