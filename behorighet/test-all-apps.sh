#!/usr/bin/env bash
flake8 .
# jslint molnet/static/javascript/molnet-*.js
# csslint molnet/static/css/molnet-*.css
python manage.py test common criteria demo login main qualifications units users --settings=test_settings
