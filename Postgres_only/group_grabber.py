__author__ = 'sp41mer'
import json, requests, sys, logging, time, datetime, psycopg2
from models import User, Group
from vk_access_token import vk_access_token


conn_string = "host='localhost' dbname='only_postgres_parcing' user='root' password='root'"
conn = psycopg2.connect(conn_string)

for group in Group.select():
    method = "groups.getMembers"
    group_id = group.vk_id
    preresponse = requests.post('https://api.vk.com/method/' + method,
                            data={'group_id': group_id,
                                  'sort': 'id_asc',
                                  'offset': 0,
                                  'count': 1000,
                                  'access_token': vk_access_token})
    predata = json.loads(preresponse.text)

    try:
        cur = conn.cursor()
        cur.execute("INSERT INTO groups_and_users (vk_id, users) VALUES (%s,%s)",
                    (group_id, predata['response']['users']))
        conn.commit()
        cur.close()
    except Exception, e:
        print str(e)
        print predata
    print group.name
    time.sleep(0.4)
conn.close()





