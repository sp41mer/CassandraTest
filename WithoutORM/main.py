__author__ = 'sp41mer'
from cassandra.cqlengine import connection
from cassandra.cluster import Cluster
from cassandra.cqlengine.management import sync_table
from cassandra.auth import PlainTextAuthProvider


userid = 123456
cluster = Cluster(['127.0.0.1'])
session = cluster.connect()
session.set_keyspace('parse_keyspace')

string_of_fields = 'pk uuid PRIMARY KEY, '
for i in range(1,11):
    string_of_fields += 'friend'+str(i) +' int,'

session.execute("CREATE TABLE "+str(userid)+ "(" +string_of_fields+")")
