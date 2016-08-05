#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==============
#      Main script file
# ==============
import peewee, datetime
 
database = peewee.SqliteDatabase("parser.db")
########################################################################
class Parsing(peewee.Model):
	"""
	ORM model of album table
	"""
	name = peewee.CharField(default='')
	node_id = peewee.CharField(default='')
	created_date = peewee.DateTimeField(default=datetime.datetime.now)
	total_users = peewee.IntegerField(default=0)
	current_offset = peewee.IntegerField(default=0)
	offset = peewee.IntegerField(default=999)
	finished = peewee.IntegerField(default=0)
	comment = peewee.CharField(default='')
 
	class Meta:
		database = database 
########################################################################
class User(peewee.Model):
	"""
	ORM model of the User table
	"""
	vk_id = peewee.IntegerField(default=0, null = True)
	first_name = peewee.CharField(default='', null = True)
	last_name = peewee.CharField(default='', null = True)
	sex = peewee.IntegerField(default=0, null = True)
	bdate = peewee.CharField(default='', null = True)
	status = peewee.CharField(default='', null = True)
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
	inspired_by	= peewee.CharField(default='', null = True)
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
	interests = peewee.CharField(default='', null = True)
	created_date = peewee.DateTimeField(default=datetime.datetime.now, null = True)
	parsing_id = peewee.ForeignKeyField(Parsing, related_name='parsing', null = True)
	class Meta:
		database = database

########################################################################

if __name__ == "__main__":
    try:
        Parsing.create_table()
    except peewee.OperationalError:
        print "Artist table already exists!"
 
    try:
        User.create_table()
    except peewee.OperationalError:
        print "Album table already exists!"