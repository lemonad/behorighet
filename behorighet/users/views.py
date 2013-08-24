# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render

from .models import UserProfile


def user_profile(request, username):
    """
    Detailed information about an individual user.

    """
    user = get_object_or_404(UserProfile, username=username)
    is_self = False

    if request.user.is_authenticated():
        if request.user.id == user.id:
            is_self = True

    units = user.units.all()

    qualifications = []
    # Met qualifications
    for q in user.qualifications():
        criteria_met, criteria_not_met = user.qualification_criteria(q)
        if criteria_not_met:
            raise Exception("That's weird, all criteria should be met here.")
        qualifications.append((q, True, criteria_met))

    # Not met qualifications
    for q in user.qualifications_not_met():
        criteria_met, criteria_not_met = user.qualification_criteria(q)
        criteria = []
        criteria.extend(criteria_met)
        criteria.extend(criteria_not_met)
        qualifications.append((q, False, criteria))

    return render(request,
                  'user.html',
                  {'userinfo': user,
                   'is_self': is_self,
                   'qualifications': qualifications,
                   'units': units})
