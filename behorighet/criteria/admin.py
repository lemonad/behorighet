from django.contrib import admin

from .models import Criterion, MetCriterion


class CriterionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Criterion, CriterionAdmin)


class MetCriterionAdmin(admin.ModelAdmin):
    list_display = ('user', 'criterion', 'basis', 'basis_description')
    search_fields = ('user__username',)

admin.site.register(MetCriterion, MetCriterionAdmin)
