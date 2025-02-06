import streamlit as st
import pandas as pd
import plotly.express as px

# Title
st.title("In Search for Happiness")

# Select boxes
option1 = st.selectbox("Select the data for the X-axis",
                      ("GDP", "Happiness", "Generosity"))
option2 = st.selectbox("Select the data for the Y-axis",
                      ("GDP", "Happiness", "Generosity"))

# Subheader
st.subheader(f"{option1} and {option2}")

# Load dataframe
data = pd.read_csv("mini_project/happy.csv")

# Match value for option 1
def get_data_x(x):
    match x:
        case "GDP":
            return data["gdp"]
        case "Happiness":
            return data["happiness"]
        case "Generosity":
            return data["generosity"]


# Match value for option 2
def get_data_y(y):
    match y:
        case "GDP":
            return data["gdp"]
        case "Happiness":
            return data["happiness"]
        case "Generosity":
            return data["generosity"]

# Create values
x = get_data_x(option1)
y = get_data_y(option2)

# Create the plot and it to the webpage
figure = px.scatter(x=x,y=y,labels={"x": f"{option1}", "y": f"{option2}"})
st.plotly_chart(figure)