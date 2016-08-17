__author__ = 'sp41mer'
from cassandra.cqlengine import connection
from cassandra.cluster import Cluster
from cassandra.cqlengine.management import sync_table
from cassandra.auth import PlainTextAuthProvider


cluster = Cluster(['127.0.0.1'])
session = cluster.connect()
session.set_keyspace('parse_keyspace')
session.execute("CREATE TABLE users (id int PRIMARY KEY, location text)")
# session = connection.setup(['127.0.0.1'], "parse_keyspace", protocol_version=3)
# session.execute("CREATE TABLE IF NOT EXISTS simplex.songs (" +
#             "id uuid PRIMARY KEY," +
#             "title text," +
#             "album text," +
#             "artist text," +
#             "tags set<text>," +
#             "data blob" +
#             ");")
