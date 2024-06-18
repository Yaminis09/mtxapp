import streamlit as st
import datetime


# Get the current day of the week
current_day = datetime.datetime.now().strftime("%A")

# Define greetings for each day of the week
greetings = {
    "Monday": "Happy Monday!",
    "Tuesday": "Terrific Tuesday!",
    "Wednesday": "Wonderful Wednesday!",
    "Thursday": "Thrilling Thursday!",
    "Friday": "Fantastic Friday!",
    "Saturday": "Superb Saturday!",
    "Sunday": "Sunny Sunday!"
}

# Get the greeting for the current day
greeting = greetings.get(current_day, "Hello!")

# Streamlit app
st.title("Hello!")
st.write(greeting)

# Display the message in the middle of the page in capital letters
st.markdown("<div style='text-align: center; font-size: 24px;'><strong>HAVE A NICE DAY</strong></div>", unsafe_allow_html=True)
