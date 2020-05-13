from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def shipping_address(self):
        return self.shippingaddress_set.filter(default=True).first()

    def has_shipping_address(self):
        return self.shipping_address is not None
