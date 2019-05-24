from django.contrib.auth.models import AbstractUser
from django.db import models

from service.models import Service


class User(AbstractUser):
    service = models.ForeignKey(Service, related_query_name="users", null=True, blank=True)
    msisdn = models.CharField(max_length=30, null=True, blank=True)
    channel = models.CharField(max_length=30, null=True, blank=True)
    status = models.SmallIntegerField(default=1)
    first_reg_time = models.DateTimeField(blank=True, null=True)
    last_reg_time = models.DateTimeField(blank=True, null=True)
    last_unreg_time = models.DateTimeField(blank=True, null=True)
    last_renew_time = models.DateTimeField(blank=True, null=True)
    last_reply_time = models.DateTimeField(blank=True, null=True)
    effective_time = models.DateTimeField(blank=True, null=True)
    expiry_time = models.DateTimeField(blank=True, null=True)
