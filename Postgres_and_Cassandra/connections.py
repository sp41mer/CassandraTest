__author__ = 'sp41mer'
from models import *

def create_tables():
    database.connect()
    database.create_tables([User,Group])
