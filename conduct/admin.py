from django.contrib import admin
from .models import Contestant, Account


# Register your models here.


class ContestantAdmin(admin.ModelAdmin):
    list_display = ('contestant_name', 'position', 'gender', 'votes')
    ordering = ('-votes',)
    list_filter = ('gender', 'position')


class AccountAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'voter_class', 'voter_section')


admin.site.register(Contestant, ContestantAdmin)
admin.site.register(Account, AccountAdmin)
