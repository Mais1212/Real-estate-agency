from django.contrib import admin

from .models import Flat
from .models import Report


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']

    list_display = ['address', 'price', 'town',
                    'construction_year', 'new_building']

    list_filter = ['new_building']


class ReportAdmin(admin.ModelAdmin):
    raw_id_fields = ['snitch', 'reported_flat']


admin.site.register(Flat, FlatAdmin)
admin.site.register(Report, ReportAdmin)
