from django.contrib import admin

from .models import Qualification


class QualificationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Qualification, QualificationAdmin)
