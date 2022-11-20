from django.contrib import admin
from .models import *

admin.site.register(Case)
admin.site.register(History)
admin.site.register(Order)
admin.site.register(Objection)
admin.site.register(DocumentDetails)