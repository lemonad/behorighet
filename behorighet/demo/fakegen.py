# -*- coding: utf-8 -*-
import csv
from datetime import date
import os
import random

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User


class FakeGenerator:
    users = []

    def __init__(self):
        path = os.path.abspath(__file__)
        dir_path = os.path.dirname(path)

        path = os.path.join(dir_path, 'demo-data/users.csv')
        with open(path, 'rb') as csvfile:
            csvreader = csv.reader(csvfile)
            # Skip first line containing column names
            csvreader.next()
            for row in csvreader:
                self.users.append(
                    {'first_name': row[0],
                     'last_name': row[1],
                     'username': row[2],
                     'email': row[3],
                     'password': row[4]})
            random.shuffle(self.users)

    def random_date(self):
        start_date = date(day=1, month=1, year=1980).toordinal()
        end_date = date.today().toordinal()
        return date.fromordinal(random.randint(start_date, end_date))

    def user(self):
        User = get_user_model()
        data = self.users.pop()
        user = User.objects.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            username=data['username'],
            email=data['email'],
            password=make_password(data['password']))
        return user
