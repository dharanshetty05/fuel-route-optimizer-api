from optimizer.models import FuelStation


class FuelService:

    @staticmethod
    def get_cheapest_stations(limit=10):
        return FuelStation.objects.order_by("retail_price")[:limit]

    @staticmethod
    def get_cheapest_price():
        station = FuelStation.objects.order_by("retail_price").first()
        return station.retail_price if station else None