import requests
from django.shortcuts import render
import pandas as pd
import random # Added for dummy data generation
from datetime import date, timedelta

def index(request):
    # Step 1: Get data (using dummy JSON for demonstration)
    # In a real application, you would fetch this data from an API or database
    
    # More comprehensive dummy data for Popular Routes
    # Increased the number of routes and added more city pairs
    all_city_pairs = [
        ("Sydney", "Melbourne"), ("Brisbane", "Sydney"), ("Perth", "Adelaide"),
        ("Melbourne", "Brisbane"), ("Gold Coast", "Sydney"), ("Adelaide", "Melbourne"),
        ("Sydney", "Perth"), ("Brisbane", "Melbourne"), ("Melbourne", "Perth"),
        ("Perth", "Sydney"), ("Adelaide", "Brisbane"), ("Cairns", "Brisbane"),
        ("Hobart", "Melbourne"), ("Canberra", "Sydney"), ("Darwin", "Perth"),
        ("Sunshine Coast", "Sydney"), ("Gold Coast", "Melbourne"), ("Launceston", "Melbourne"),
    ]
    
    popular_routes_data = []
    for origin, destination in all_city_pairs:
        popular_routes_data.append({
            "origin": origin,
            "destination": destination,
            "bookings": random.randint(300, 1500) # Wider range for bookings
        })
    
    # Sort by bookings in descending order to ensure it's always "top"
    popular_routes_data = sorted(popular_routes_data, key=lambda x: x['bookings'], reverse=True)


    # Dummy data for Price Trends (Past 14 Days)
    # Generate somewhat realistic fluctuating prices around a base for 14 days
    base_price = 220 # Slightly higher base price
    price_trend_data = []
    price_trend_labels = []
    
    # Generate data for the past 14 days
    for i in range(14):
        current_date = date.today() - timedelta(days=13 - i)
        price_trend_labels.append(current_date.strftime('%b %d')) # e.g., 'Jul 01'
        
        # Introduce more variability and slight trend
        price_change = random.uniform(-15, 25) # Price can fluctuate more significantly
        if i > 0:
            # Tend to follow previous day's price with some variation
            current_price = price_trend_data[-1] + price_change
            # Ensure prices don't drop too low or go too high unrealistically
            current_price = max(150, min(350, current_price))
        else:
            current_price = base_price + price_change
            current_price = max(150, min(350, current_price))
            
        price_trend_data.append(round(current_price, 2))


    context = {
        'popular_routes': popular_routes_data,
        'price_trend_data': price_trend_data,
        'price_trend_labels': price_trend_labels,
    }

    return render(request, "index.html", context)
def about(request):
    return render(request, "about.html")
def contact(request):
    return render(request, "contact.html")