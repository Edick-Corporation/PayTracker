from django.contrib import admin

from main.models import Type, Purchase


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['user', 'cost', 'type', 'pk']
    list_editable = ['cost', 'type']
    list_filter = ['type']


class TypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Type, TypeAdmin)
admin.site.register(Purchase, PurchaseAdmin)
