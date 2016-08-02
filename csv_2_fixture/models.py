import csv
import json

from django.db import models


class CsvToDjangoFixture(object):
    def __init__(self, model, fields):
        self.model = "%s.%s" % (model.__module__.split(".")[0], model.__name__)
        self.fields = fields
        self.in_file = "%s.csv" % model.__name__
        self.out_file = '%s_fixture.json' % model.__name__

    def to_fixture(self):
        with open(self.in_file, 'rb') as csvfile:
            objects = csv.reader(csvfile, quotechar="|")

            with open(self.out_file, 'wb') as json_file:
                json_container = []
                for index, obj in enumerate(objects):
                    item = {"fields": {}, "model": self.model, "pk": index + 1}
                    for field in self.fields:
                        if isinstance(field.index, int):
                            value = obj[field.index]
                        else:
                            # por aca todavia no va a entrar porque siempre es entero la col
                            value = field.index
                        item["fields"][field.name] = value
                    json_container.append(item)
                print json_container
                json_file.write(json.dumps(json_container))


class Column(object):
    def __init__(self, index, name, is_literal=False):
        self.index = index
        self.name = name
        self.is_literal = is_literal
