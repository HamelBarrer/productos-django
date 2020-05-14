from enum import Enum


class OrderStatus(Enum):
    CREATED = 'CREATED'
    PAYED = 'PAYED'
    COMPLETED = 'COMPLETED'
    CANCEL = 'CANCEL'


choices = [(tag, tag.value) for tag in OrderStatus]
