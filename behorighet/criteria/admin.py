from django.contrib import admin

from .models import Criterion, MetCriterion


class CriterionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Criterion, CriterionAdmin)


class MetCriterionAdmin(admin.ModelAdmin):
    pass

admin.site.register(MetCriterion, MetCriterionAdmin)
