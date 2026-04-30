from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import RouteRequestSerializer
from optimizer.services.routing_service import RoutingService
from optimizer.services.optimizer import RouteOptimizer


class OptimizeRouteView(APIView):

    def post(self, request):
        serializer = RouteRequestSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.validated_data

        try:
            route = RoutingService.get_route(
                [data["start_lng"], data["start_lat"]],
                [data["end_lng"], data["end_lat"]],
            )

            optimized = RouteOptimizer.optimize(route)

            return Response({
                "route": {
                    "distance_miles": round(route["distance_miles"], 2),
                    "duration_hours": round(route["duration_hours"], 2),
                    "polyline": route["geometry"]
                },
                "fuel_analysis": {
                    "total_gallons": round(optimized["total_gallons_needed"], 2),
                    "stops_required": optimized["stops_needed"],
                    "cost_per_gallon": optimized["fuel_price_per_gallon"],
                    "total_cost": round(optimized["total_fuel_cost"], 2),
                    "recommended_stations": optimized["recommended_stations"]
                }
            })

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )