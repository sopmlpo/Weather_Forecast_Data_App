import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key from environment variable
API_KEY = os.getenv("API_KEY")

def get_data(place, forecast_days=None):
    # Check if API key exists
    if not API_KEY:
        return "Error: No API key provided. Please set up your API key in the .env file."
        
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    try:
        response = requests.get(url)
        data = response.json()  # Simplified JSON handling
        
        if response.status_code != 200:
            return f"Error: Unable to fetch weather data"
            
        filtered_data = data["list"]
        if forecast_days is None:
            return filtered_data
            
        nr_values = 8 * forecast_days
        filtered_data = filtered_data[:nr_values]
        return filtered_data
        
    except Exception as e:
        return f"Error: {str(e)}"

# Remove or modify this section before publishing
if __name__ == "__main__":
    print("Please set up your API key in .env file to use this application")