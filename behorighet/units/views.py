# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render

from .models import Unit


def unit(request, unitname):
    """
    Detailed information about an individual user.

    """
    unit = get_object_or_404(Unit, name__iexact=unitname)
    is_owner = False

    if request.user.is_authenticated():
        if request.user.id == unit.owner.id:
            is_owner = True

    unit_qualification_stats = unit.per_qualification_statistics()

    return render(request,
                  'unit.html',
                  {'unitinfo': unit,
                   'is_owner': is_owner,
                   'unit_qualification_stats': unit_qualification_stats})
