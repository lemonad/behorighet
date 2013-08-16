from django.contrib import admin

from .models import Unit


class UnitAdmin(admin.ModelAdmin):
    pass

admin.site.register(Unit, UnitAdmin)
