# Fuel Route Optimizer API

A Django REST API that computes the most cost-effective fuel strategy for a given driving route in the USA.

---

## 🚀 Overview

This project provides an API that:

- Accepts start and end locations (latitude & longitude)
- Fetches route data using OpenRouteService
- Calculates fuel requirements based on:
  - Vehicle range: 500 miles
  - Mileage: 10 miles per gallon
- Determines the number of required fuel stops
- Recommends cost-effective fuel stations using CSV fuel price data
- Returns total estimated fuel cost along the route

---

## 🧠 Key Features

- Single external API call for routing (optimized for performance)
- Fast response time with minimal computation
- Bulk CSV ingestion (~8000 fuel stations)
- Cost-optimized fuel strategy
- Clean modular architecture (services layer)
- Handles edge cases (short routes, zero stops)

---

## 🏗️ Tech Stack

- Python
- Django
- Django REST Framework
- OpenRouteService API
- SQLite
- Pandas

---

## 📂 Project Structure

fuel-route-optimizer-api/
│
├── config/                 # Django project settings  
├── optimizer/  
│   ├── models.py           # FuelStation model  
│   ├── views.py            # API view  
│   ├── serializers.py      # Input validation  
│   ├── services/  
│   │   ├── routing_service.py  
│   │   ├── fuel_service.py  
│   │   ├── optimizer.py    # Core logic  
│   ├── management/  
│       └── commands/  
│           └── import_fuel_csv.py  
│
├── requirements.txt  
├── .env  
└── README.md  

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

git clone <your_repo_url>  
cd fuel-route-optimizer-api  

---

### 2. Create Virtual Environment

python -m venv venv  

Activate:

Mac/Linux:  
source venv/bin/activate  

Windows:  
venv\Scripts\activate  

---

### 3. Install Dependencies

pip install -r requirements.txt  

---

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

DEBUG=True  
SECRET_KEY=your_secret_key  
ORS_API_KEY=your_openrouteservice_api_key  

---

### 5. Run Migrations

python manage.py migrate  

---

### 6. Import Fuel Data

python manage.py import_fuel_csv <path_to_csv>  

---

### 7. Run Development Server

python manage.py runserver  

---

## 📡 API Usage

### Endpoint

POST /api/optimize-route/  

---

### Request Body

{
  "start_lat": 32.7767,
  "start_lng": -96.7970,
  "end_lat": 29.7604,
  "end_lng": -95.3698
}

---

### Response Example

{
  "route": {
    "distance_miles": 238.84,
    "duration_hours": 3.74,
    "polyline": "encoded_route_string"
  },
  "fuel_analysis": {
    "total_gallons": 23.88,
    "stops_required": 0,
    "cost_per_gallon": 2.687,
    "total_cost": 64.18,
    "recommended_stations": []
  }
}

---

## ⚡ Optimization Logic

- Total fuel needed = distance / mileage  
- Number of stops = ceil(distance / 500) - 1  
- Fuel cost calculated using cheapest available fuel stations  

---

## ⚠️ Assumptions & Tradeoffs

To prioritize performance and fast delivery:

- Fuel station selection is cost-optimized, not strictly route-constrained  
- Route is returned as an encoded polyline (can be rendered on a map)  
- Only one routing API call is made per request  

---

## 🔮 Future Improvements

- Filter fuel stations based on actual route path  
- Decode polyline and place fuel stops geographically  
- Add caching for repeated routes  
- Support address-based input (geocoding)  

---

## 🧪 Edge Cases Handled

- Routes shorter than 500 miles → no fuel stops required  
- Invalid inputs → handled via serializer validation  
- External API errors → handled gracefully  

---

## 🎥 Demo

A Loom video demonstrating the API functionality and code walkthrough is included in the submission.

---

## 📌 Summary

This project demonstrates a practical backend system that integrates routing APIs with real-world fuel price data to compute cost-effective travel strategies under time and performance constraints.