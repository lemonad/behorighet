How to populate application with demo data
------------------------------------------
Set up local_settings according to instructions in
`local_settings.py.sample`. Then run the following
commands:

    $ ./manage.py syncdb --migrate --noinput
    $ ./manage.py demodata

Running demo
------------
Start the web server with the following command
    $ ./manage.py runserver --settings=development

Browse to [http://127.0.0.1:8000/].
