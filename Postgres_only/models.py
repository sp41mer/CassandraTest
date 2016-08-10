__author__ = 'sp41mer'
import uuid, peewee

database = peewee.PostgresqlDatabase(
    'only_postgres_parcing',
    user='root',
    password='root',
    host='localhost'
)

class User(peewee.Model):
    vk_id = peewee.IntegerField(default=0, null = True)
    first_name = peewee.CharField(default='', null = True)
    last_name = peewee.CharField(default='', null = True)
    sex = peewee.IntegerField(default=0, null = True)
    bdate = peewee.CharField(default='', null = True)
    status = peewee.TextField(default='', null = True)
    deactivated = peewee.CharField(default='', null = True)
    has_photo = peewee.IntegerField(default=0, null = True)
    mobile_phone = peewee.CharField(default='', null = True)
    home_phone = peewee.CharField(default='', null = True)
    skype = peewee.CharField(default='', null = True)
    facebook = peewee.CharField(default='', null = True)
    twitter = peewee.CharField(default='', null = True)
    livejournal = peewee.CharField(default='', null = True)
    instagram = peewee.CharField(default='', null = True)
    political = peewee.IntegerField(default=0, null = True)
    religion = peewee.CharField(default='', null = True)
    people_main = peewee.IntegerField(default=0, null = True)
    life_main = peewee.IntegerField(default=0, null = True)
    smoking = peewee.IntegerField(default=0, null = True)
    alcohol = peewee.IntegerField(default=0, null = True)
    inspired_by	= peewee.TextField(default='', null = True)
    occupation_type = peewee.CharField(default='', null = True)
    occupation_id = peewee.IntegerField(default=0, null = True)
    occupation_name = peewee.CharField(default='', null = True)
    country_id = peewee.IntegerField(default=0, null = True)
    country_title = peewee.CharField(default='', null = True)
    city_id = peewee.IntegerField(default=0, null = True)
    city_title = peewee.CharField(default='', null = True)
    last_seen_time = peewee.IntegerField(default=0, null = True)
    last_seen_platform = peewee.IntegerField(default=0, null = True)
    online = peewee.IntegerField(default=0, null = True)
    online_app = peewee.CharField(default='', null = True)
    online_mobile = peewee.IntegerField(default=0, null = True)
    relation = peewee.IntegerField(default=0, null = True)
    interests = peewee.TextField(default='', null = True)

    class Meta:
		database = database


class Group(peewee.Model):
    vk_id = peewee.CharField(default='', null = True)
    name = peewee.CharField(default='', null = True)
    screen_name = peewee.CharField(default='', null = True)
    type = peewee.CharField(default='', null = True)
    description = peewee.CharField(default='', null = True)
    photo_50 = peewee.CharField(default='', null = True)
    photo_100 = peewee.CharField(default='', null = True)
    photo_200 = peewee.CharField(default='', null = True)

    class Meta:
		database = database
