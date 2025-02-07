# Weather App

This project is a simple weather application built with Streamlit. The app allows users to check the temperature or the sky for 1-5 days for a given city. It uses the Weather Open Map API for retrieving real-time weather data and incorporates Cursor AI for speed, efficiency, code organization & clarity.

## Features

- **Real-time weather updates**: Fetches current weather data from Weather Open Map API.
- **Location-based search**: Users can enter a location (city) to get weather information.
- **Temperature & sky condition**: Displays key weather parameters.
- **User-friendly interface**: Built with Streamlit for a simple and intuitive UI.

## Technologies Used

- **Streamlit**: Python framework for building interactive web apps.
- **Weather Open Map API**: Provides real-time weather data.
- **Cursor AI**: Speeds development & enhances the app's functionality.

## Setup and Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/weather-app.git
   ```

2. Obtain an API key from Weather Open Map:

   - Go to [Weather Open Map](https://openweathermap.org/) and sign up for an API key.
   - Save the key in a `.env` file or directly in the app code.

3. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

## API Key Setup

In order to use the weather data, you will need to set up your API key from Weather Open Map. Make sure to add it to your environment variables or replace the placeholder in the app code.

```bash
API_KEY = 'your-api-key-here'
```
