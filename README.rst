=============
Csv 2 fixture
=============

A simple Django app to convert a csv to django fixture.

Quick start
-----------

1. Add "csv-2-fixture" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'csv_2_fixture',
    ]

2. Copy the csv file to the root of the project
3. Run `python manage.py csv_to_fixture <app_name.model_name>`
4. Follow the menu to finish.
5. Look at the root of the project, you must have the fixture in there.
6. Use `./manage.py loaddata <fixture>.json` to load data to your db.


TODO
----

1. Handle FK beetween csv.
2. A flag --in to specify from where get csv file.
3. A flag --out to specify where save the fixture file.
