from mongoengine import *


class Types(Document):
    name = StringField(required=True, max_length=50)


connect('parking')

