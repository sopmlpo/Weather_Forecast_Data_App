import requests
import json
import os
from dotenv import load_dotenv
import requests
import json

# Load environment variables
load_dotenv()

# Get API key from environment variable
API_KEY = os.getenv("API_KEY")

def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    try:
        response = requests.get(url)
        content = response.content
        # Try to decode and parse step by step
        decoded_content = content.decode()
        data = json.loads(decoded_content)
        filtered_data = data["list"]
        if forecast_days is None:
            return filtered_data
            
        nr_values = 8 * forecast_days
        filtered_data = filtered_data[:nr_values]
        return filtered_data
        
    except json.JSONDecodeError as e:
        return f"Error decoding JSON: {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3))