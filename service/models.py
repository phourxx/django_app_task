from django.db import models


class Service(models.Model):
    code = models.CharField(max_length=50, verbose_name="Service Code", null=False, blank=False)
    package_code = models.CharField(max_length=50, verbose_name="Package Code", null=False, blank=False)
    name = models.CharField(max_length=200, verbose_name="Service Name", null=False, blank=False)
    schedule = models.CharField(max_length=100, null=False, blank=False)
    price = models.SmallIntegerField()
    period_length = models.SmallIntegerField()
    free_length = models.SmallIntegerField()
    status = models.SmallIntegerField()
    created_time = models.DateTimeField(auto_now=True)


class Request(models.Model):
    service = models.ForeignKey(Service, related_query_name="requests", null=False, blank=False)
    system = models.ForeignKey("service.System", null=False, blank=False, related_query_name="requests")
    msisdn = models.CharField(max_length=30, null=False, blank=False)
    service_number = models.CharField(max_length=20, null=False, blank=False)
    message = models.TextField(max_length=500, null=False, blank=False)
    status = models.CharField(max_length=2, null=False, blank=False)
    received_time = models.DateTimeField(auto_now=True)
    responsed_time = models.DateTimeField(blank=True, null=True)


class Response(models.Model):
    service = models.ForeignKey(Service, related_query_name="responses", null=False, blank=False)
    request = models.ForeignKey(Request, related_query_name="responses", null=False, blank=False)
    system = models.ForeignKey("service.System", related_query_name="responses", null=False, blank=False)
    msisdn = models.CharField(max_length=30, null=False, blank=False)
    service_number = models.CharField(max_length=20, null=False, blank=False)
    content = models.TextField(max_length=500, null=False, blank=False)
    status = models.CharField(max_length=1, null=False, blank=False)
    num_of_sm = models.SmallIntegerField()
    num_of_receipt = models.SmallIntegerField()
    created_time = models.DateTimeField(auto_now=True)
    effective_time = models.DateTimeField(blank=True, null=True)
    expiry_time = models.DateTimeField(blank=True, null=True)
    sent_time = models.DateTimeField(blank=True, null=True)


class Keyword(models.Model):
    service = models.ForeignKey(Service, related_query_name="keywords", null=False, blank=False)
    reg_keyword = models.CharField(max_length=30, null=False, blank=False)
    unreg_keyword = models.CharField(max_length=30, null=False, blank=False)
    service_number = models.CharField(max_length=30, null=False, blank=False)


class Content(models.Model):
    service = models.ForeignKey(Service, related_query_name="contents", null=False, blank=False)
    title = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField(max_length=500, null=False, blank=False)
    sent_status = models.SmallIntegerField()
    status = models.SmallIntegerField()
    created_time = models.DateTimeField(auto_now=True)
    effective_time = models.DateTimeField(blank=True, null=True)
    expiry_time = models.DateTimeField(blank=True, null=True)
    sent_time = models.DateTimeField(blank=True, null=True)


class Cdr(models.Model):
    service = models.ForeignKey(Service, related_query_name="cdrs", null=False, blank=False)
    msisdn = models.CharField(max_length=30, null=False, blank=False)
    price = models.SmallIntegerField()
    reason = models.CharField(max_length=10, null=False, blank=False)
    channel = models.CharField(max_length=20, null=False, blank=False)
    description = models.CharField(max_length=50, null=False, blank=False)
    result = models.SmallIntegerField()
    charge_time = models.DateTimeField(blank=True, null=True)


class RegisterLog(models.Model):
    service = models.ForeignKey(Service, related_query_name="register_logs", null=False, blank=False)
    msisdn = models.CharField(max_length=30, null=False, blank=False)
    request_type = models.SmallIntegerField()
    channel = models.CharField(max_length=20, null=False, blank=False)
    result = models.SmallIntegerField()
    message = models.CharField(max_length=200, null=False, blank=False)
    description = models.CharField(max_length=200, null=False, blank=False)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(blank=True, null=True)


class ServiceConfirmation(models.Model):
    service_id = models.BigIntegerField()   # Didn't use foreign key here because there's no linkage between this model and the Service model on the data model sent
    msisdn = models.CharField(max_length=20, null=False, blank=False)
    status = models.CharField(max_length=2, null=False, blank=False)
    created_time = models.DateTimeField(auto_now_add=True)
    expired_time = models.DateTimeField(blank=True, null=True)


class DndUser(models.Model):
    msisdn = models.CharField(max_length=255, null=False, blank=False)
    type = models.CharField(max_length=255, null=False, blank=False)


class ServiceResponse(models.Model):
    service_id = models.BigIntegerField()   # Didn't use foreign key here because there's no linkage between this model and the Service model on the data model sent
    code = models.CharField(max_length=20, null=False, blank=False)
    type = models.TextField(max_length=320, null=False, blank=False)


class System(models.Model):
    system_id = models.CharField(max_length=2, null=False, blank=False, verbose_name="System ID")   # Created this because it has a datatype on the data model that differs from Django's datatype for id
    code = models.CharField(max_length=50, null=False, blank=False, verbose_name="System Code")
