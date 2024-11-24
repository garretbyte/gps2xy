import xml.etree.ElementTree as ET

# Load the GPX file
gpx_file = "trees-of-interest-in-saint-rose-woodland.gpx"

# Parse the GPX file
tree = ET.parse(gpx_file)
root = tree.getroot()

# GPX namespace
namespace = {"default": "http://www.topografix.com/GPX/1/1"}

# Extract waypoints (wpt elements)
waypoints = root.findall("default:wpt", namespace)

# Collect latitude and longitude
coordinates = []
for wpt in waypoints:
    lat = wpt.get("lat")
    lon = wpt.get("lon")
    coordinates.append((lat, lon))

# Print extracted coordinates
for lat, lon in coordinates:
    print(f"Latitude: {lat}, Longitude: {lon}")