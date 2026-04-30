import os
import requests
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

class RoutingService:
    """
    This is the service layer responsible for interacting with the OpenRouteService API.
    It encapsulates all routing-related external API calls.
    """

    # ORS Directions API endpoint
    BASE_URL = "https://api.openrouteservice.org/v2/directions/driving-car"

    @classmethod
    def get_route(cls, start_coords, end_coords):
        """
        Fetches route details between two coordinate points.
        Returns parsed route data including distance, duration and geometry
        """

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