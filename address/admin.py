from django.contrib import admin
from django.forms import CharField
from address.models import Address

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display=('id','country', 'street','city')
    list_filter = ['country']
    search_fields = ['city']
    