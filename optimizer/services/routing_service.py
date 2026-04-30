import os
import requests
from dotenv import load_dotenv

load_dotenv()


class RoutingService:
    BASE_URL = "https://api.openrouteservice.org/v2/directions/driving-car"

    @classmethod
    def get_route(cls, start_coords, end_coords):
        api_key = os.getenv("ORS_API_KEY")

        headers = {
            "Authorization": api_key,
            "Content-Type": "application/json",
        }

        body = {
            "coordinates": [
                start_coords,
                end_coords
            ]
        }

        response = requests.post(
            cls.BASE_URL,
            json=body,
            headers=headers,
            timeout=20
        )

        response.raise_for_status()
        data = response.json()

        route = data["routes"][0]
        summary = route["summary"]

        return {
            "distance_m": summary["distance"],
            "distance_miles": summary["distance"] * 0.000621371,
            "duration_sec": summary["duration"],
            "duration_hours": summary["duration"] / 3600,
            "geometry": route["geometry"],
        }