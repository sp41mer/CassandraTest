__author__ = 'sp41mer'
from cassandra.cqlengine import connection
from cassandra.cluster import Cluster
from cassandra.cqlengine.management import sync_table
from cassandra.auth import PlainTextAuthProvider


userid = 5
cluster = Cluster(['127.0.0.1'])
session = cluster.connect()
session.set_keyspace('parse_keyspace')

string_of_fields = 'userid int PRIMARY KEY, '
string_of_input_fields = 'userid,'
list_of_values = str(userid)+', '
for i in range(1,11):
    string_of_fields += 'friend'+str(i) +' int,'
    string_of_input_fields += 'friend'+str(i)+','
    list_of_values += str(i)+','

session.execute("CREATE TABLE user_"+str(userid) + "(" +string_of_fields+")")
session.execute("INSERT INTO parse_keyspace.user_"+str(userid)+" ("+string_of_input_fields[:-1]+")"+" VALUES ("+list_of_values[:-1]+")")

