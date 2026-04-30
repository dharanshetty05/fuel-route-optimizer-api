from math import ceil
from optimizer.services.fuel_service import FuelService


class RouteOptimizer:

    MILES_PER_GALLON = 10
    MAX_RANGE_MILES = 500

    @classmethod
    def optimize(cls, route_data):
        distance = route_data["distance_miles"]

        # total fuel needed
        total_gallons = distance / cls.MILES_PER_GALLON

        # number of refuels required
        stops_needed = max(0, ceil(distance / cls.MAX_RANGE_MILES) - 1)

        cheapest_price = FuelService.get_cheapest_price()

        total_cost = total_gallons * float(cheapest_price)

        cheapest_stations = FuelService.get_cheapest_stations(limit=stops_needed)

        return {
            "distance_miles": distance,
            "total_gallons_needed": total_gallons,
            "stops_needed": stops_needed,
            "fuel_price_per_gallon": float(cheapest_price),
            "total_fuel_cost": total_cost,
            "recommended_stations": [
                {
                    "name": s.truckstop_name,
                    "city": s.city,
                    "state": s.state,
                    "price": float(s.retail_price),
                }
                for s in cheapest_stations
            ]
        }