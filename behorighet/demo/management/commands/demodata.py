# -*- coding: utf-8 -*-
import random

from django.core.management.base import BaseCommand

from demo.fakegen import FakeGenerator
from units.models import Unit


class Command(BaseCommand):
    args = ""
    help = "Populates application with demo data."

    def handle(self, *args, **options):
        fakegen = FakeGenerator()

        owner_a = fakegen.user()
        owner_b = fakegen.user()
        owner_c = fakegen.user()
        owner_d = fakegen.user()

        unit_a = Unit.objects.create(name="Unit A", owner=owner_a)
        for n in range(random.randint(5, 15)):
            user = fakegen.user()
            unit_a.members.add(user)

        unit_b = Unit.objects.create(name="Unit B", owner=owner_b)
        for n in range(random.randint(5, 15)):
            user = fakegen.user()
            unit_b.members.add(user)

        unit_c = Unit.objects.create(name="Unit C", owner=owner_c)
        for n in range(random.randint(5, 15)):
            user = fakegen.user()
            unit_c.members.add(user)

        unit_d = Unit.objects.create(name="Unit D", owner=owner_d)
        for n in range(random.randint(5, 15)):
            user = fakegen.user()
            unit_d.members.add(user)
