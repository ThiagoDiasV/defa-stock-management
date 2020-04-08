from django.core.management.base import BaseCommand
import csv
from pgc.models import PgcProduct
import os
from django.apps import apps


class Command(BaseCommand):
    help = (
        "Uploads an existing csv file to PGC items database."
        "You must insert an valid csv file with 5 columns at least: "
        "ID, List Name, Description, Reference number or CATMAT, Unit"
        "If the ref number is catmat, you must insert the boolean True after csv file"
        "Like this: python manage.py upload_pgc_list csvfile.csv --has_catmat=True"
        "Else, you don't need to insert anything, only the csv file."
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model_name = PgcProduct

    def get_current_app_path(self):
        return apps.get_app_config("pgc").path

    def get_csv_file(self, filename):
        app_path = self.get_current_app_path()
        file_path = os.path.join(app_path, "management", "commands", filename)
        return file_path

    def add_arguments(self, parser):
        parser.add_argument(
            "csv_file",
            type=str,
            help="Indicates the exactly csv file to upload to database",
        )
        parser.add_argument(
            "--has_catmat",
            type=bool,
            help="Indicates if the ref number is catmat or not",
        )

    def handle(self, *args, **kwargs):
        csv_file = kwargs["csv_file"]
        has_catmat = kwargs["has_catmat"]
        csv_file_path = self.get_csv_file(csv_file)
        with open(csv_file_path, "r") as file:
            has_header = csv.Sniffer().has_header(file.read())
            file.seek(0)
            reader = csv.reader(file, delimiter=";")
            if has_header:
                next(reader)
            if has_catmat:
                for row in reader:
                    PgcProduct.objects.create(
                        list_name=row[1],
                        product_description=row[2],
                        has_catmat=True,
                        catmat=row[3],
                        unit=row[4],
                    )
            else:
                for row in reader:
                    PgcProduct.objects.create(
                        list_name=row[1],
                        product_description=row[2],
                        has_catmat=False,
                        ref_number=row[3],
                        unit=row[4],
                    )
            self.stdout.write(f"Data of {csv_file} succesfully uploaded to database")
