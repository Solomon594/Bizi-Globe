import gmaps
import gmaps.datasets
from datetime import datetime

def main():
    # Replace with your Google Maps API key
    gmaps.configure(api_key="YOUR_GOOGLE_API_KEY")

    # Define the two GPS coordinates (latitude, longitude)
    origin = (37.7749, -122.4194)  # San Francisco, CA
    destination = (34.0522, -118.2437)  # Los Angeles, CA

    # Create a map centered between the two locations
    fig = gmaps.figure(center=(38.5, -120), zoom_level=5)

    # Create a directions layer using the Directions API
    directions_layer = gmaps.directions_layer(
        origin, destination, show_markers=False, stroke_color='blue', stroke_opacity=0.7
    )

    # Add the directions layer to the map
    fig.add_layer(directions_layer)

    # Display the map
    return fig

if __name__ == "__main__":
    fig = main()
    fig
