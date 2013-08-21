# -*- coding: utf-8 -*-
from django.shortcuts import render

from units.models import Unit


def startpage(request):
    """Start page.

    Shows list of units available for statistics/filtering.

    """
    units = Unit.objects.all()

    # t = loader.get_template('startpage.html')
    # c = RequestContext(request, {
    #                    'units': units,
    #                    })
    # return HttpResponse(t.render(c)).
    return render(request,
                  'startpage.html',
                  {'units': units,})
