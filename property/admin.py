from django.contrib import admin

from .models import Flat, Owner
from .models import Report


class FlatInLine(admin.TabularInline):
    model = Owner.apartments_in_property.through
    list_display = ['owner']
    raw_id_fields = ['owner']


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'Owner']
    readonly_fields = ['created_at']

    list_display = ['address', 'price', 'town',
                    'construction_year', 'new_building']

    list_filter = ['new_building']

    inlines = [FlatInLine]  
    raw_id_fields = ['liked_by']


class ReportAdmin(admin.ModelAdmin):
    raw_id_fields = ['snitch', 'reported_flat']


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['apartments_in_property']
    list_display = ('owner', 'phonenumber', 'pure_phone')


admin.site.register(Flat, FlatAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Owner, OwnerAdmin)
