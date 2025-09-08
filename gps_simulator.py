import requests
import time
import math

BASE_URL = "http://127.0.0.1:8000"
UPDATE_INTERVAL = 3  # seconds between updates
SPEED = 0.0003  # distance moved per update (~very small for demo)

def distance(lat1, lon1, lat2, lon2):
    # Simple Euclidean distance for small scale
    return math.sqrt((lat2 - lat1)**2 + (lon2 - lon1)**2)

def move_towards(lat1, lon1, lat2, lon2, step):
    """Move from (lat1, lon1) towards (lat2, lon2) by 'step' amount"""
    d = distance(lat1, lon1, lat2, lon2)
    if d == 0:
        return lat2, lon2
    ratio = step / d
    if ratio >= 1:
        return lat2, lon2
    new_lat = lat1 + (lat2 - lat1) * ratio
    new_lon = lon1 + (lon2 - lon1) * ratio
    return new_lat, new_lon

def get_buses():
    resp = requests.get(f"{BASE_URL}/buses/")
    if resp.status_code == 200:
        return resp.json()
    else:
        print("Failed to fetch buses:", resp.text)
        return []

def get_bus_stops(bus_id):
    resp = requests.get(f"{BASE_URL}/bus_stops/{bus_id}")
    if resp.status_code == 200:
        return resp.json()
    else:
        print(f"Failed to fetch stops for bus {bus_id}: {resp.text}")
        return []

def update_bus(bus_id, lat, lon):
    # Update bus location
    resp = requests.patch(f"{BASE_URL}/buses/{bus_id}/location", json={"latitude": lat, "longitude": lon})
    if resp.status_code != 200:
        print(f"Failed to update bus {bus_id}: {resp.text}")
    # Store tracking
    resp2 = requests.post(f"{BASE_URL}/tracking/", json={"bus_id": bus_id, "latitude": lat, "longitude": lon})
    if resp2.status_code != 200:
        print(f"Failed to store tracking for bus {bus_id}: {resp2.text}")

if __name__ == "__main__":
    buses = get_buses()
    bus_positions = {}
    bus_routes = {}

    # Initialize positions and routes
    for bus in buses:
        stops = get_bus_stops(bus["id"])
        if not stops:
            continue
        bus_routes[bus["id"]] = stops
        lat = bus["latitude"] if bus["latitude"] is not None else stops[0]["latitude"]
        lon = bus["longitude"] if bus["longitude"] is not None else stops[0]["longitude"]
        bus_positions[bus["id"]] = {"lat": lat, "lon": lon, "next_stop": 1}

    print(f"Simulating {len(bus_positions)} buses along their routes...")

    try:
        while True:
            for bus_id, pos in bus_positions.items():
                stops = bus_routes[bus_id]
                next_stop_idx = pos["next_stop"]
                if next_stop_idx >= len(stops):
                    next_stop_idx = 0  # loop back to start
                stop = stops[next_stop_idx]

                # Move towards next stop
                new_lat, new_lon = move_towards(pos["lat"], pos["lon"], stop["latitude"], stop["longitude"], SPEED)
                update_bus(bus_id, new_lat, new_lon)

                # Check if reached stop
                if distance(new_lat, new_lon, stop["latitude"], stop["longitude"]) < 0.00005:
                    pos["next_stop"] = (next_stop_idx + 1) % len(stops)
                pos["lat"], pos["lon"] = new_lat, new_lon

            time.sleep(UPDATE_INTERVAL)
    except KeyboardInterrupt:
        print("\nSimulation stopped.")
