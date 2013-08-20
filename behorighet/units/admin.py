from django.contrib import admin

from .models import Unit


class UnitAdmin(admin.ModelAdmin):
    readonly_fields = ('date_created',)
    fields = ('name', 'owner', 'members', 'qualifications', 'date_created')
    filter_horizontal = ('members', 'qualifications')
    list_display = ('name', 'owner')
    search_fields = ['name']
    save_as = True

admin.site.register(Unit, UnitAdmin)
