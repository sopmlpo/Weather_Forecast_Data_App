import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider, selectbox, and subheader
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1,
                 max_value=5, help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")
 
if place:
    try:
        # Get the temperature or sky data
        filtered_data = get_data(place, days)
        
        # Check if filtered_data is an error message (string)
        if isinstance(filtered_data, str) and "Error" in filtered_data:
            st.error("Unfortunately, there is no available data for this place.")
        else:
            if option == "Temperature":
                temperatures = [round(dict["main"]["temp"] - 273.15, 1) for dict in filtered_data]
                dates = [dict["dt_txt"] for dict in filtered_data]
                # Create a temperature plot
                figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
                st.plotly_chart(figure)

            if option == "Sky":  
                images = {
                    "Clear": "images/clear.png",
                    "Clouds": "images/cloud.png",
                    "Rain": "images/rain.png",
                    "Snow": "images/snow.png"
                }
                sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
                image_paths = [images.get(condition, "images/clear.png") for condition in sky_conditions]
                st.image(image_paths)
    except Exception as e:
        st.error("Unfortunately, there is no available data for this place.")
else:
    st.info("Please enter a place to see the forecast.") 