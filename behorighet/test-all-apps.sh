#!/usr/bin/env bash
flake8 .
# jslint molnet/static/javascript/molnet-*.js
# csslint molnet/static/css/molnet-*.css
python manage.py test criteria qualifications users --settings=test_settings
