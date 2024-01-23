# investments/admin.py

from django.contrib import admin
from .models import Investment, Account

admin.site.register(Investment)
admin.site.register(Account)
