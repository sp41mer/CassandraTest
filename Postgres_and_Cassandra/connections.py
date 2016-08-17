__author__ = 'sp41mer'
from models import *


def create_tables():
    database.connect()
    try:
        database.create_tables([User], True)
    except Exception, e:
        print str(e)

