# pylint: disable=no-name-in-module, import-error
from django.db import models

class subaccount(models.Model):
    name = models.CharField(max_length=15)
    owner = models.ForeignKey(
        'jwt_auth.User',
        related_name="subaccount_owner",
        on_delete=models.CASCADE
    )


    def __str__(self):
        return f'{self.name}'
