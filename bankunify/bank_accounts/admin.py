from django.contrib import admin
from .models import BankAccount, BankName

class BankNameAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(BankName, BankNameAdmin)
