from neomodel import DateTimeProperty as NeoDateTimeProperty
from datetime import datetime


class DateTimeProperty(NeoDateTimeProperty):

    def inflate(self, value):
        return datetime.timestamp(super().inflate(value)) * 1000
