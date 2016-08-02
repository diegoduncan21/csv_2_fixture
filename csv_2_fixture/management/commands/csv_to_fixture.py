from django.core.management import BaseCommand
from django.apps import apps

from csv_2_fixture.models import CsvToDjangoFixture, Column


class Command(BaseCommand):
    help = "Can generate a fixture from a csv file to then load data to de db."

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('model', nargs='+', type=str)

    def handle(self, *args, **options):
        self.stdout.write("\n Wellcome, You have to match index of column "
                          "of your csv with field name of the model.")

        fields = self.get_fields()
        if fields:
            app, model_name = options.get('model')[0].split('.')
            try:
                model_class = apps.get_model(app_label=app,
                                             model_name=model_name)
            except Exception, e:
                self.stdout.write("\n%s \n" % e)
            else:
                if model_class:
                    instance = CsvToDjangoFixture(model=model_class,
                                                  fields=fields)
                    instance.to_fixture()
        else:
            self.stdout.write(
                "\nYou must specify at least one field of the model. \n")

    def get_fields(self):
        fields = []
        option = input("\n1) Add new match(field, csv column). \n"
                       "2) Finish.")
        while option != 2:
            if option != 1:
                continue

            field = raw_input("Field name: ")
            column_number = input("Column csv number: ")
            fields.append(Column(column_number, field))

            option = input("\n1) Add new match(field, csv column). \n"
                           "2) Finish.")
        return fields
