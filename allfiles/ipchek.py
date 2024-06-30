import ipinfo
import folium
from geopy.geocoders import Nominatim

# Initialize the IPinfo client with your API key
access_token = ""
handler = ipinfo.getHandler(access_token)

# Get IP address information
ip_address = input("Enter the IP address: ")
details = handler.getDetails(ip_address)

# Extract location information
city = details.city if hasattr(details, 'city') else None
region = details.region if hasattr(details, 'region') else None
country = details.country if hasattr(details, 'country') else None

# Combine location details into a single string
location_str = ", ".join(filter(None, [city, region, country]))

# Use geopy to get latitude and longitude coordinates
geolocator = Nominatim(user_agent="ip_location_app")
location = geolocator.geocode(location_str)

if location:
    # Print latitude and longitude
    print("Latitude:", location.latitude)
    print("Longitude:", location.longitude)

    # Create a map
    myMap = folium.Map(location=[location.latitude, location.longitude], zoom_start=9)

    # Add a marker for the location
    folium.Marker([location.latitude, location.longitude], popup=location_str).add_to(myMap)

    # Save the map to an HTML file
    myMap.save("ip_location.html")
else:
    print("Location information not found for the given IP address.")
