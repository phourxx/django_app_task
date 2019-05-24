from django.contrib import admin
from .models import *


# class RequestAdmin(admin.TabularInline):
#     model = Request
#     # fields = "__all__"
#     extra = 1
#     can_delete = True
#     verbose_name_plural = "Addresses"


admin.site.register(Service)
admin.site.register(Request)
admin.site.register(Response)
admin.site.register(Keyword)
admin.site.register(Content)
admin.site.register(Cdr)
admin.site.register(RegisterLog)
admin.site.register(ServiceConfirmation)
admin.site.register(DndUser)
admin.site.register(ServiceResponse)
admin.site.register(System)
