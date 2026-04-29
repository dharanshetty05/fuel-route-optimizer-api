import pandas as pd
from decimal import Decimal
from django.core.management.base import BaseCommand
from optimizer.models import FuelStation


class Command(BaseCommand):
    help = "Import fuel stations from CSV"

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str)

    def handle(self, *args, **kwargs):
        file_path = kwargs["file_path"]

        df = pd.read_csv(file_path)

        FuelStation.objects.all().delete()

        records = []

        for _, row in df.iterrows():
            try:
                station = FuelStation(
                    truckstop_name=str(row["Truckstop Name"]).strip(),
                    address=str(row.get("Address", "")).strip(),
                    city=str(row["City"]).strip(),
                    state=str(row["State"]).strip(),
                    retail_price=Decimal(str(row["Retail Price"]))
                )
                records.append(station)
            except Exception:
                continue

        FuelStation.objects.bulk_create(records, batch_size=1000)

        self.stdout.write(
            self.style.SUCCESS(f"Imported {len(records)} fuel stations.")
        )