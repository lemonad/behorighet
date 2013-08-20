from django.contrib import admin

from .models import Qualification


class QualificationAdmin(admin.ModelAdmin):
    readonly_fields = ('date_created',)
    fields = ('name', 'description', 'criteria', 'date_created')
    filter_horizontal = ('criteria',)
    list_display = ('name',)
    search_fields = ['name']
    save_as = True

admin.site.register(Qualification, QualificationAdmin)
