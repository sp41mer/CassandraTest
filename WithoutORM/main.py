__author__ = 'sp41mer'
# from cassandra.cqlengine import connection
# from cassandra.cluster import Cluster
# from cassandra.cqlengine.management import sync_table
# from cassandra.auth import PlainTextAuthProvider

#
# cluster = Cluster(['127.0.0.1'])
# session = cluster.connect()
# session.set_keyspace('parse_keyspace')

string_of_fields = 'friend1 int PRIMARY KEY, '
for i in range(2,11):
    string_of_fields += 'friend'+str(i) +' int,'

print string_of_fields[:-1]