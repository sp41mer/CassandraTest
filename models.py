import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

class GroupNoSQL(Model):
    vk_id = columns.Text(primary_key=True)
    members = columns.List(columns.Integer)

class FriendsNoSQL(Model):
    vk_id = columns.Text(primary_key=True)
    friends = columns.List(columns.Integer)



