from peewee import Model, CharField, IntegerField, ForeignKeyField
from peewee import *  
import sys

sys.path.append('C:/Beauty_studio_data_base')

import settings


db = SqliteDatabase(database=f'{settings.DATABASE_PATH}/{settings.DATABASE_NAME}')


class BaseModel(Model):
    class Meta:
        power_level = 0
        database = db


class Position(BaseModel):
    post = CharField(default='')
    power_level = IntegerField(default=0)
    class Meta:
        power_level = 0
        database = db
        identifier_field = 'post'


class User(BaseModel):
    position_id = ForeignKeyField(model=Position, backref='Users', default=0)
    login = CharField(default='')
    password = CharField(default='')
    class Meta:
        power_level = 0
        database = db
        identifier_field = 'login'


class Worker(BaseModel):
    position_id = ForeignKeyField(Position, backref='Workers', default=0)
    name = CharField(default='')
    surname = CharField(default='')
    telephone_number = CharField(default='')
    class Meta:
        power_level = 0
        database = db
        identifier_field = 'surname'


class Service(BaseModel):
    name = CharField(default='')
    price = IntegerField(default=0)
    description = CharField(default='')
    class Meta:
        power_level = 0
        database = db
        identifier_field = 'name'

        
class Client(BaseModel):
    name = CharField(default='')
    address = CharField(default='')
    telephone_number = CharField(default='')
    class Meta:
        power_level = 0
        database = db
        identifier_field = 'name'


class Visit(BaseModel):
    client_id = ForeignKeyField(Client, backref='visits', default=0)
    service_id = ForeignKeyField(Service, backref='visits', default=0)
    worker_id = ForeignKeyField(Worker, backref='visits', default=0)
    datetime = DateTimeField(default='')
    class Meta:
        power_level = 0
        database = db
        identifier_field = 'datetime'


db_models = [User, Worker, Position, Service, Client, Visit]

db.create_tables(db_models)

