# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 17:32:20 2023

@author: amrit
"""

import streamlit as st
import pydeck as pdk
import pandas as pd
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
import base64
import plotly.graph_objects as go
import numpy as np
import time
from sklearn.neighbors import KernelDensity
import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import openai
import pdfplumber


#-----App Layout Settings-----#
st.set_page_config(
    page_title="Amrit Mandal",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded",
)


#---Setting the sidebar menu-----#

with st.sidebar:
    selected = option_menu("Amrit Mandal", ["Home", 'LinkedIn'], 
        icons=['house', 'gear'], menu_icon="cast", default_index=0, orientation="vertical")
    st.write('email: amrit.mandal0191@gmail.com')
    st.write('Contact: +91 8116401052')

# Example URLs
home_url = "https://profile-amrit-mandal.streamlit.app/"
LinkedIn_url = "https://www.linkedin.com/in/amritmandal/"

# Display hyperlinks based on the selected menu item
if selected == "Home":
    with st.sidebar:
        st.markdown(f"[Go to Home]({home_url})", unsafe_allow_html=True)
elif selected == "LinkedIn":
    with st.sidebar:
        st.markdown(f"[Go to LinkedIn]({LinkedIn_url})", unsafe_allow_html=True)



st.title('Welcome Guest!')

#-----End of App Layout Setting----#

#-----Section Header CSS--------#

# CSS for the entire app
app_css = """
<style>
    .section-header {
        position: relative; /* Required for positioning the pseudo-elements */
        padding: 10px 20px;
        margin: 20px 0;
        background-color: #f9f9f9;
        color: #333333;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        text-align: center;
        font-family: 'Arial', sans-serif;
        font-size: 22px;
        font-weight: bold;
        font-style: italic;
        border-left: 4px solid #007bff;
        border-right: 4px solid #007bff;
        transition: background-color 0.3s ease, border-color 0.3s ease;
    }
    .section-header:hover {
        background-color: #e9ecef;
        border-color: #0056b3;
        cursor: pointer;
    }

    /* Pseudo-elements for horizontal lines */
    .section-header:before, .section-header:after {
        content: '';
        position: absolute;
        top: 50%;
        width: 30%; /* Width of the lines */
        height: 0px; /* Thickness of the lines */
        background-color: #333333; /* Color of the lines */
        transform: translateY(-50%);
    }
    .section-header:before {
        left: 5%; /* Positioning the left line */
    }
    .section-header:after {
        right: 5%; /* Positioning the right line */
    }
</style>
"""

# Function to create HTML for section headers
def create_section_header(title):
    return f"""
    <div class="section-header">{title}</div>
    """

#------End of Section Header CSS-----#

#-----Header section-------#

# Function to encode image file to base64
def get_image_as_base64(path):
    with open(path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return f"data:image/png;base64,{encoded_string}"

# Image path
image_path = 'images/profile_pic.png'  # Replace with your image file path
image_base64 = get_image_as_base64(image_path)

# HTML and CSS
header_html = f"""
<link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600&display=swap" rel="stylesheet">
<style>
.header-card {{
    padding: 20px;
    display: flex;
    align-items: center;
    background-color: #ffffff; /* White background */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Adding a subtle shadow */
    border-radius: 15px; /* Rounded corners */
    width: 95%;
    margin: 10px auto;
    transition: transform 0.3s, box-shadow 0.3s; /* Smooth transition for hover effect */
}}

.header-card:hover {{
    transform: translateY(-10px); /* Slight lift on hover */
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2); /* Increased shadow on hover */
}}

.profile-image {{
    width: 150px; /* Adjusted profile image size */
    height: 150px;
    border-radius: 50%; /* Circular image */
    background-image: url("{image_base64}");
    background-size: cover;
    margin-right: 20px; /* Spacing between image and text */
}}

.profile-text {{
    font-family: 'Open Sans', sans-serif;
    font-size: 22px; /* Slightly larger font for name and title */
    color: #333333; /* Darker text for better readability */
}}

.catchy-text {{
    font-family: 'Open Sans', sans-serif;
    font-size: 16px;
    color: #666666; /* Keeping the text color subtle */
    margin-top: 5px; /* Spacing for better layout */
}}
</style>

<div class="header-card">
    <div class="profile-image"></div>
    <div>
        <div class="profile-text">Amrit Mandal</div>
        <div class="profile-text">Transformative Renewable Energy Manager</div>
        <div class="catchy-text">Driving Global Solar Projects with Cutting-Edge Innovations</div>
        <div class="catchy-text">PV | BESS | AI | ML</div>
    </div>
</div>

"""

# Render the custom HTML/CSS in the Streamlit app
components.html(header_html, height=240)

#--------Intro Section------#




intro_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        .intro-section {
            background-color: #f2f2f2; /* Light grey background */
            border-left: 4px solid #007bff; /* Blue accent border */
            padding: 20px;
            margin: 10px 0;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Soft shadow for depth */
            font-family: Arial, sans-serif; /* Professional font */
        }

        .intro-section h2 {
            color: #333333; /* Dark grey color for text */
            font-size: 24px; /* Slightly larger font for heading */
            margin-bottom: 10px; /* Space below the heading */
        }

        .intro-section p {
            color: #555555; /* Medium grey for paragraph */
            font-size: 16px; /* Readable font size for paragraph */
            line-height: 1.6; /* Spacing for line height */
        }
    </style>
</head>
<body>

<div class="intro-section">
    <h2>Introduction</h2>
    <p>Dynamic Solar Energy Expert and Visionary Leader, Amrit Mandal, brings over nine years of experience in solar PV project development, data analytics, and BESS across global projects. Passionate about driving innovations in renewable energy solutions, Amrit aspires to contribute significantly to sustainable, smart city initiatives and groundbreaking solar technologies. His goal is to elevate the renewable energy landscape, leveraging his extensive experience to make a lasting impact in the sector.</p>
</div>

</body>
</html>

"""
components.html(intro_html, height=300)

#------End of Intro Section------#

#------Intro Line for Each Section-------#

intro_css="""
    <style>
        .intro-section {
            background-color: #f2f2f2; /* Light grey background */
            border-left: 4px solid #007bff; /* Blue accent border */
            padding: 10px;
            margin: 10px 0;
            border-radius: 6px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Soft shadow for depth */
            font-family: Arial, sans-serif; /* Professional font */
            font-style: italic;
        }

        .intro-section h2 {
            color: #333333; /* Dark grey color for text */
            font-size: 24px; /* Slightly larger font for heading */
            margin-bottom: 10px; /* Space below the heading */
        }

        .intro-section p {
            color: #555555; /* Medium grey for paragraph */
            font-size: 16px; /* Readable font size for paragraph */
            line-height: 1.6; /* Spacing for line height */
        }
    </style>
    """

def create_section_intro(intro):
    return f"""
    <div class="intro-section"><p>{intro}</p></div>
    """

#components.html(intro_css + create_section_intro("Global Impacts text text tetx"), height=150)

#------Impact Created----------#

components.html(app_css + create_section_header("Global Impacts"), height=100)

components.html(intro_css + create_section_intro("Showcasing a decade of dedication to sustainability, I've steered solar projects amounting to 383 MWp, successfully offsetting 2.25 million tons of CO2. My strategic management has also directed $289.3M in investments, fueling the growth of renewable energy on a global scale.")
                                                 , height=150)

#-----MW of Projects Done-------#


# CSS for the image
image_css = """
<style>
.solar-image-container {
    text-align: center;
    margin-top: 40px; /* Adjust this to position the image */
}

.solar-image {
    width: 80px; /* Adjust as needed */
    height: auto;
    transition: transform 0.3s ease;
}

.solar-image:hover {
    transform: translateY(-20px); /* Adjust the hover effect as needed */
}
</style>
"""

# HTML for the image
image_html = """
<div class="solar-image-container">
    <img class="solar-image" src="https://i.imgur.com/kescOjS.png" alt="Sun and Solar Array">
</div>
"""

# Display the image in Streamlit
components.html(image_css + image_html, height=120) # Adjust the height as needed

# CSS for the text box
text_box_css = """
<style>
.mw-showcase {
    text-align: center;
    margin: 10px auto; /* Top and bottom margin 20px, left and right auto for centering */
    padding: 10px;
    background-color: #007bff; /* Blue background for emphasis */
    color: white; /* White text for contrast */
    border-radius: 7px; /* Rounded corners */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Shadow for depth */
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    max-width: 90%; /* Adjust this value to set your desired width */
    font-family: Arial, sans-serif;
}

.mw-showcase:hover {
    transform: scale(1.05); /* Slight increase in size on hover */
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3); /* Increased shadow on hover */
}

.mw-value {
    font-size: 36px; /* Large font size for the MW value */
    font-weight: bold; /* Bold font for impact */
    margin: 10px 0; /* Spacing */
}

.mw-description {
    font-size: 18px; /* Smaller font size for the description */
}
</style>
"""

# HTML for the text box
text_box_html = """
<div class="mw-showcase">
    <div class="mw-value">383 MWp</div>
    <div class="mw-description">Total Solar PV Projects Managed Directly</div>
</div>
"""

# Display the text box in Streamlit
components.html(text_box_css + text_box_html, height=130) # Adjust the height as needed
    

#-----End of MW of Projects Done-------#
col1,col2= st.columns(2)
#-------CO2 Offset------#

# Constants
CO2_OFFSET_PER_MWH = 0.85  # Metric tonnes CO2 offset per MWh of solar energy produced
DAILY_ENERGY_PRODUCTION_PER_MW = 5.0  # Average daily energy production per MW
DAYS_IN_YEAR = 365

# Data of MW installed each year
installed_mw = {
    "Year End": [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022],
    "MW Installed": [2, 5, 7, 10, 50, 100, 200, 10, 15, 10]
}

# Calculate the cumulative MW installed each year and total energy produced by the end of 2022
cumulative_mw = np.cumsum(installed_mw["MW Installed"])
total_energy_produced = np.sum(cumulative_mw[:-1] * DAYS_IN_YEAR * DAILY_ENERGY_PRODUCTION_PER_MW)
total_co2_offset = total_energy_produced * CO2_OFFSET_PER_MWH

# Current ongoing MW capacity
current_capacity_mw = cumulative_mw[-1]

# Initialize session state for CO2 offset and start time
if 'co2_offset' not in st.session_state:
    st.session_state.co2_offset = total_co2_offset
    st.session_state.start_time = time.time()

# Function to calculate the current CO2 offset
# Assume this function calculates the current CO2 offset based on the current capacity
def calculate_current_co2_offset(start_offset, current_capacity_mw, start_time):
    elapsed_time = time.time() - start_time
    additional_offset = (elapsed_time / (24 * 3600)) * current_capacity_mw * DAILY_ENERGY_PRODUCTION_PER_MW * CO2_OFFSET_PER_MWH
    return start_offset + additional_offset

# Initialize session state
if 'co2_offset' not in st.session_state:
    st.session_state.co2_offset = total_co2_offset
    st.session_state.start_time = time.time()

# Calculate the current CO2 offset
st.session_state.co2_offset = calculate_current_co2_offset(
    st.session_state.co2_offset, 
    current_capacity_mw, 
    st.session_state.start_time
)

# Create the gauge chart using plotly
current_offset = st.session_state.co2_offset
max_offset_value = current_offset * 1.2  # To set the gauge's maximum value

# The gauge chart
# The gauge chart
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=current_offset,
    domain={'x': [0.1, 0.9], 'y': [0.2, 0.9]},  # Adjust domain to center gauge
    title={'text': "CO2 Offset"},
    gauge={
        'axis': {'range': [None, max_offset_value], 'tickwidth': 1, 'tickcolor': "darkblue"},
        'bar': {'color': "green"},
        'steps': [
            {'range': [0, current_offset], 'color': "lightgreen"}
        ],
        'threshold': {
            'line': {'color': "red", 'width': 4},
            'thickness': 0.75,
            'value': current_offset
        }
    }
))

# Adjust the size of the gauge chart to make it more compact
fig.update_layout(
    autosize=False,
    width=350,  # Adjust the width to match the other gauge
    height=200,  # Adjust the height to match the other gauge
    margin=dict(l=105, r=5, t=5, b=5),  # Adjust margins to center the gauge
)

# Convert the Plotly figure to HTML with full HTML structure
fig_html = fig.to_html(full_html=False, include_plotlyjs='cdn')

# Custom HTML and CSS for the card container
card_html = f"""
<div class="card" style="border: 1px solid #E1E1E1; border-radius: 7px; padding: 10px;font-family: Arial, sans-serif; box-shadow: 3px 3px 10px rgba(0,0,0,0.1); text-align: center; transition: transform 0.3s ease, box-shadow 0.3s ease;">
    {fig_html}  <!-- Insert Plotly figure -->
    <h3 style="text-align: center; margin-top: 10px; font-size: 18px;">Total CO2 Offset: {current_offset:.2f} tons</h3>
</div>

<script>
document.addEventListener('DOMContentLoaded', (event) => {{
  const card = document.querySelector('.card');
  card.addEventListener('mouseenter', () => {{
    card.style.transform = 'scale(1.03)';
    card.style.boxShadow = '0 6px 20px rgba(0,0,0,0.15)';
  }});
  card.addEventListener('mouseleave', () => {{
    card.style.transform = 'scale(1)';
    card.style.boxShadow = '3px 3px 10px rgba(0,0,0,0.1)';
  }});
}});
</script>
"""



# Use Streamlit components to display the card
with col1:
    components.html(card_html, height=300)

# Refresh 
with st.sidebar:
    if st.button('Refresh CO2 Offset'):
        st.session_state.start_time = time.time()  # Reset the start time for the offset calculation

with st.sidebar:
    st.write('___')    
    

#-----Investments Managed------#
# Total cumulative investment and max value for the gauge
total_investment = 289.3  # in million USD
max_gauge_value = 500.0  # Max value of the gauge in million USD

# Custom HTML and JavaScript for the modified gauge chart
gauge_chart_html = f"""
<html>
<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script src="https://bernii.github.io/gauge.js/dist/gauge.min.js"></script>
<style>
/* Card container */
.card {{
  border: 1px solid #dfdfdf;
  border-radius: 7px;
  padding: 15px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.3s ease-in-out;
  font-family: Arial, sans-serif;
}}
.card:hover {{
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
}}

/* Gauge container */
#gauge-container {{
  position: relative;
  width: auto; /* Adjust as needed */
  height: auto; /* Adjust as needed */
  text-align: center; /* Center the canvas */
}}

/* Investment text beneath the gauge */
#investment-text {{
  font-size: 18px;
  margin-top: 15px; /* Space above the text */
  color: #333;
  text-align:center;
}}

/* Hover effect for gauge needle */
#gauge canvas {{
  cursor: pointer;
}}
#gauge canvas:hover {{
  opacity: 0.8;
}}

</style>
</head>
<body>

<div class="card">
  <div id="gauge-container">
    <canvas id="gauge" width="400" height="200"></canvas>
  </div>
  <div id="investment-text">Total Investments Managed: ${total_investment}M</div>
</div>

<script>
// JavaScript to initialize the gauge and handle hover effect
var gaugeValue = {total_investment}; // The value to display on the gauge

var opts = {{
  angle: 0, // The span of the gauge arc
  lineWidth: 0.2, // The line thickness, reduced from 0.44 to 0.2
  radiusScale: 1, // Relative radius
  pointer: {{
    length: 0.6, // Relative to gauge radius
    strokeWidth: 0.035, // The thickness
    color: '#000000' // Fill color
  }},
  limitMax: false,     // If false, max value will be higher if needed
  limitMin: false,     // If true, min value will be 0
  colorStart: '#6FADCF',   // Colors
  colorStop: '#8FC0DA',    // Just experiment with them
  strokeColor: '#E0E0E0',  // To see which ones work best for you
  generateGradient: true,
  highDpiSupport: true,     // High resolution support
staticZones: [
     {{strokeStyle: "#F03E3E", min: 0, max: {max_gauge_value} * 0.25}}, // Red from 0 to 25%
     {{strokeStyle: "#FFDD00", min: {max_gauge_value} * 0.25, max: {max_gauge_value} * 0.75}}, // Yellow from 25% to 75%
     {{strokeStyle: "#30B32D", min: {max_gauge_value} * 0.75, max: {max_gauge_value}}}, // Green from 75% to 100%
  ],
  staticLabels: {{
    font: "10px sans-serif",  // Specifies font
    labels: [0, {max_gauge_value} * 0.25, {max_gauge_value} * 0.5, {max_gauge_value} * 0.75, {max_gauge_value}],  // Print labels at these values
    labelsCount: 5,
    color: "#000000",  // Optional: Label text color
    fractionDigits: 0  // Optional: Numerical precision. 0=round off.
  }},
}};


var target = document.getElementById('gauge');
var gauge = new Gauge(target).setOptions(opts); // Create gauge
gauge.maxValue = 500; // Max value for the gauge
gauge.setMinValue(0);  // Min value for the gauge
gauge.animationSpeed = 32; // Animation speed
gauge.set(gaugeValue); // Set the current value
</script>
</body>
</html>
"""

# Use Streamlit components to embed the HTML/JavaScript in the app
with col2:
    components.html(gauge_chart_html, height=300)
    

#------End of Impact Section------#

#--------Projects Done Map------#
projectmap_intro=f"""Spanning the globe from the bustling streets of India to the expansive landscapes of Australia and beyond,
 my portfolio illuminates the breadth of my solar energy projects. With over 200MW managed in Tamilnadu, 
 a 140MW design in Iran, and innovative community projects in Nepal, 
 the map traces a story of sustainable impact and technical prowess in renewable energy solutions.

"""
components.html(app_css + create_section_header("Global Project Portfolio"), height=100)
components.html(intro_css + create_section_intro(projectmap_intro)
                                                 , height=150)




# Sample data with an additional 'brief' column for the tooltip
data = {
    "latitude": [
        22.3511148, 36.7014631, 27.7567667, 31.2638905, 13.4499943, -31.8759835, 24.638916, 24.0002488, 
        23.5882019, 23.7644025, -26.205, 9.6000359, -2.9814344, -1.9646631, 11.8145966, 32.6707877, 
        -10.3333333, 13.1500331, 10.9094334, 23.8143419, 26.8105777, 22.3850051, 22.9964948, 23.4559809, 
        15.9240905, 10.3528744, 14.5203896, 27.1303344, 18.9068356, 31.2496266
    ],
    "longitude": [
        78.6677428, -118.755997, -81.4639835, -98.5456116, 144.7651677, 147.2869493, 46.7160104, 53.9994829, 
        58.3829448, 90.389015, 28.049722, 7.9999721, 23.8222636, 30.0644358, 42.8453061, 51.6650002, 
        -53.2, -59.5250305, 78.3665347, 77.5340719, 73.7684549, 71.745261, 87.6855882, 85.2557301, 
        80.1863809, 76.5120396, 75.7223521, 80.859666, 75.6741579, 73.6632218
    ],
    "location": [
        "India", "California, USA", "Florida, USA", "Texas, USA", "Guam, USA", "NSW, Australia", 
        "Saudi Arabia", "UAE", "Oman", "Bangladesh", "South africa", "Nigeria", "congo", "rwanda", 
        "djibouti", "isfahan, iran", "brazil", "Barbados", "Tamilnadu", "Madhya Pradesh", 
        "Rajasthan", "Gujarat", "West Bengal", "Jharkhand", "Andhra Pradesh", "Kerala", "Karnataka", 
        "Uttar pradesh", "Maharastra", "Nepal"
    ],
    "brief": [
        "4MW,Consulted & Managed", "2MW,Consulted", "10MW+,Designed", "2MW,Designed & Consulted", 
        "3MW+,Designed", "1MW+,Consulted", "~0.5MW,Designed & Consulted", "~0.5MW,Designed & Consulted", 
        "10MW+,Managed", "1MW,Consulted", "40MW,Designed & Consulted", "PV MFG,Consulted", ",Consulted", 
        "1MW+,Consulted", "50MW+,Designed & Consulted", "140MW,Designed & Consulted", 
        "~0.5MW,Designed & Consulted", "~0.5MW,Designed & Consulted", "200MW+,Managed", 
        "75MW,Managed & Consulted", "100MW+,Managed & Consulted", "20MW,Designed & Consulted", 
        "~1MW,Managed", "MiniGrid Project,Managed", "20MW,Managed", "20MW,Designed & Consulted", 
        "~25MW,Managed", "2MW,Managed & Consulted", "~80MW,Managed & Consulted", "Pilot Community project,Consulted"
    ]
}

df = pd.DataFrame(data)



# Assuming df is your DataFrame with the latitude and longitude
coords = df[['latitude', 'longitude']]

# Use Kernel Density Estimation to estimate the density at each point
kde = KernelDensity(bandwidth=1.0, metric='haversine')
kde.fit(np.radians(coords))

# Evaluate the densities on the same points
scores = np.exp(kde.score_samples(np.radians(coords)))

# Normalize the scores to a scale that makes sense for your dot sizes
# We invert the scores because a high density should give a smaller size
max_radius = 500000  # adjust this to your needs
min_radius = 200000  # adjust this to your needs
df['radius'] = max_radius - scores / max(scores) * (max_radius - min_radius)


# Define the tooltip text
tooltip = {
    "html": "<b>{location}</b><br><b>{brief}</b>",
    "style": {
        "backgroundColor": "steelblue",
        "color": "white"
    }
}

# Set the viewport location
view_state = pdk.ViewState(latitude=df["latitude"].mean(), longitude=df["longitude"].mean(), zoom=1, pitch=0)

# Use the radius column for the 'get_radius' attribute in your pydeck layer
layer = pdk.Layer(
    "ScatterplotLayer",
    df,
    get_position=["longitude", "latitude"],
    get_color="[180, 0, 200, 140]",  # Custom color
    get_radius="radius",  # Use the new radius column
    pickable=True  # Needed for the tooltip to work
)

# Render the map with the custom style
col1,col2,col3=st.columns([0.25,2.50,0.25])
col2.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/dark-v9',  # Here you can choose other styles like 'light-v9' or 'outdoors-v11'
    layers=[layer],
    initial_view_state=view_state,
    tooltip=tooltip  # Adding the tooltip here
))

#------End of Project Map-------#

#----Work Experience Timeline------#

workexp_intro=f"""Throughout my career in solar energy, I've transitioned from co-founding a startup to 
leading major solar projects, consistently driving innovation and sustainability. 
My diverse roles have deepened my expertise in solar technology, 
emphasizing my commitment to renewable energy advancements.

"""
components.html(app_css + create_section_header("Work Experience"), height=100)
components.html(intro_css + create_section_intro(workexp_intro)
                                                 , height=150)


# Custom styles for the timeline
timeline_style = """
<style>
/* Timeline setup */
.timeline {
    position: relative;
    max-width: 960px; /* Adjust the max-width of the timeline */
    margin: 0 auto;
}

/* Timeline central line */
.timeline::after {
    content: '';
    position: absolute;
    width: 2px; /* Width of the central line */
    background-color: #bdbdbd; /* Color of the central line */
    top: 0;
    bottom: 0;
    left: 50%;
    margin-left: -1px;
}

/* Container for each timeline item */
.container {
    padding: 10px 10px;
    position: relative;
    width: 100%;
    display: flex;
    justify-content: flex-end; /* Align containers to the center line */
}

/* Container positioned on the left */
.left {
    justify-content: flex-start;
}

/* Content within each container */
.content {
    padding: 20px;
    background-color: white;
    position: relative;
    border-radius: 6px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    width: calc(50% - 40px); /* Half width minus padding */
    margin: 10px 0;
}

/* Position the circles on the timeline */
.container::after {
    content: '';
    position: absolute;
    width: 20px;
    height: 20px;
    background-color: #FF9F55; /* Circle color */
    border: 3px solid #FFFFFF; /* Circle border color */
    border-radius: 50%;
    top: 50%;
    transform: translateY(-50%);
    right: calc(50% - 10px);
    z-index: 1;
}

/* Arrows for the left items */
.left::before {
    content: " ";
    height: 0;
    position: absolute;
    top: 50%;
    width: 0;
    z-index: 1;
    border: medium solid white;
    border-width: 10px 0 10px 10px;
    border-color: transparent transparent transparent white;
    right: calc(50% + 5px);
    transform: translateY(-50%);
}

/* Arrows for the right items */
.right::before {
    content: " ";
    height: 0;
    position: absolute;
    top: 50%;
    width: 0;
    z-index: 1;
    border: medium solid white;
    border-width: 10px 10px 10px 0;
    border-color: transparent white transparent transparent;
    left: calc(50% + 5px);
    transform: translateY(-50%);
}

/* Add hover effect for the content */
.content:hover {
    transform: scale(1.03); /* Slightly increase the size */
    box-shadow: 0 8px 16px rgba(0,0,0,0.2); /* Make the shadow deeper */
    transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out; /* Smooth transition for the effect */
}

@media screen and (max-width: 600px) {
    /* Adjust styles for mobile */
    .content {
        width: calc(100% - 80px); /* Full width minus padding on mobile */
        padding: 20px;
    }
    .container::before, .container::after {
        left: 20px;
        right: auto;
    }
    .left, .right {
        justify-content: flex-start;
    }
    .left::before, .right::before {
        display: none;
    }
}
</style>
"""

st.markdown(timeline_style, unsafe_allow_html=True)



# Create the timeline entries
def timeline_entry(position, date, title, company, description):
    col1, col2, col3 = st.columns([1, 8, 1])
    with col1:
        st.write("")  # For left alignment
    with col2:
        html = f"""
        <div class="timeline">
            <div class="container {position}">
                <div class="content">
                    <h3>{date}</h3>
                    <h5>{title}<br> <span>{company}</span></h5>
                    <p>{description}</p>
                </div>
            </div>
        </div>
        """
        st.markdown(html, unsafe_allow_html=True)
    with col3:
        st.write("")  # For right alignment

# Example entries
timeline_entry("left", "Jan, 2020 - Present", "Key Accounts Manager", "HTC, Muscat Oman", "Driving Solar PV Engineering Excellence")
timeline_entry("right", "Oct, 2016 - Jan, 2020",
               "Assistant Manager - Design", "AMPL Cleantech Pvt Ltd<br> Kolkata India", "Facilitated 1GW+ Solar PV Developments")
timeline_entry("left", "Mar, 2016 - Oct, 2016", "Engineering Lead",
               "Kirti Solar Limited, Kolkata, India", "Managed Solar PV Engineering & Rollout team.")
timeline_entry("right", "Dec, 2015 - Mar, 2016", "Senior Design Engineer",
               "O3 Energy LLC, Chandigarh, India", "Engineered Major PV Designs")
timeline_entry("left", "May, 2014 - Nov, 2015", "Co-Founder Senior Consultant",
               "OhmSolar & Technologies<br> Burdwan, India", "Crafted Strategic PV Blueprints for Solar Businesses - Globally")
timeline_entry("right", "Dec, 2013 - Apr, 2014", "Project Engineer",
               "Annapurna Export, Kolkata, India", "Executed Diverse Key Solar Operations")
timeline_entry("left", "Aug, 2013 - Nov, 2014", "Project Coordinator",
               "ONergy, Kolkata, India", "Coordinated Rural Solar Initiatives")

st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')



#-------Detailed Work Experience-------#


import hashlib

def create_card(title, position, points, header_color="#007BFF"):  # Default color is set to blue
    # Create a unique class name for the card header based on the title
    unique_class_name = "header-" + hashlib.md5(title.encode()).hexdigest()

    st.markdown(f"""
    <style>
        .card {{
            border: 1px solid #ddd;
            border-radius: 10px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
            font-family: 'Open Sans', sans-serif;
            transition: transform 0.3s ease;
        }}

        .card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        }}

        .{unique_class_name} {{
            background-color: {header_color};
            color: #fff;
            padding: 10px 15px;
            border-top-left-radius: 10px;
            border-top-right-radius: 10px;
        }}

        .card-content {{
            padding: 15px;
        }}

        .card-content h5, ul, li {{
            color: #666;
        }}
    </style>
    <div class="card">
        <div class="{unique_class_name}">{title}</div>
        <div class="card-content">
            <h5>Position: {position}</h5>
            <ul>
                {"".join([f"<li>{point}</li>" for point in points])}
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)




#----St.expander content design functions-----#

def generate_expander_html(sections):
    html_content = """
    <style>
        .details-container {
            font-family: 'Arial', sans-serif;
            color: #444;
        }
        .section-header {
            color: #007BFF;
            font-weight: bold;
            margin-bottom: 5px;
        }
        .sub-header {
            color: #28A745; /* Green color for sub-headers */
            font-size: 14px;
            font-weight: bold;
            margin-top: 10px;
        }
        .content {
            margin-left: 5px;
            font-size: 14px;
            line-height: 1.6;
        }
        ul {
            margin-top: 5px;
            list-style-type: square;
        }
        li {
            margin-bottom: 5px;
        }
    </style>
    <div class="details-container">
    """

    for header, items in sections.items():
        html_content += f"<div class='section-header'>{header}:</div>"
        if isinstance(items, dict):
            for subheader, subitems in items.items():
                html_content += f"<div class='sub-header'>{subheader}</div><ul class='content'>"
                for item in subitems:
                    html_content += f"<li>{item}</li>"
                html_content += "</ul>"
        elif isinstance(items, list):
            html_content += "<ul class='content'>"
            for item in items:
                html_content += f"<li>{item}</li>"
            html_content += "</ul>"
        else:
            html_content += f"<div class='content'>{items}</div>"

    html_content += "</div>"
    return html_content


#-------#


# Example usage
col1,col2= st.columns(2)
with col1:
    
    create_card("Hussam Technology Company, Oman (HTC)", "Design Engineering Manager", 
            ["Led diverse PV projects, scaling residential to commercial.",
             "Managed a 3-engineers' team, enhancing project delivery.",
             "Pioneered BESS and EV charging infra, boosting HTC's tech edge.",
             "Steered PDO's 5MW Smart City, MAF's mall rooftops, and PDO Noor's 1000 Villas project."], header_color="#007BFF")


    st.write('\n')
    st.write('\n')    
    # Expander for additional details
    with st.expander("See more about my role at HTC"):
        htc_sections = {
    "Job Role and Responsibilities": [
        "Solar Design Engineering Manager at HTC.",
        " Oversee the engineering of diverse solar projects, including rooftop, carpark, and ground-mounted systems.",
        "Manage a team of 3 engineers focused on plant layout, electrical diagrams, structural designs, and 3D modeling."
        ],
    "Key Projects and Clients": [
        "Managed a range of projects from residential 10kW installations to 3MW commercial setups for clients like Al Zain LLC.",
        "Directed the engineering process for PDO's 5MW Smart City project, MAF's 4MW+ mall rooftop projects, and a 1MW tracker project.",
        "Supervised the PDO Noor project, targeting Solar PV installations in 1000 Omani Villas."
    ],
    "Achievements": [
        "Streamlined pre-sales and post-award engineering processes.",
        "Developed innovative web applications to facilitate engineering calculations and financial analyses.",
        "Ensured design optimization and project delivery through effective coordination with procurement and rollout teams."
    ],
    "Skills and Expertise": {
        "Technical Skills": [
            "Proficient in PVsyst, Helioscope, AutoCAD, and SketchUp.",
            "Conducted detailed BoP, BOQ, and energy modeling.",
            "Performed cable sizing, circuit breaker sizing, and earthing calculations.",
            "Developed web apps for DC/AC cable sizing, system earthing, and financial projections."
        ],
        "Managerial Skills": [
            "Team leadership and project management.",
            "Cross-functional coordination between design, procurement, and execution teams.",
            "Vendor assessment and relationship management for procurement of major components."
        ]
    },
    "Tools and Technologies": [
        "Mastery in solar energy software and CAD tools.",
        "Use of Excel for custom engineering calculations.",
        "Project tracking and management via Monday.com.",
        "Application of Python, machine learning, AI, and data science for tool development."
    ],
    "Vendor Relations and Procurement": [
        "Responsibility for comparing and finalizing vendor contracts.",
        "Conducting technical due diligence and assessments for supplier selection.",
        "Facilitating meetings with vendors to foster long-term business relationships."
    ]
}

        htc_html = generate_expander_html(htc_sections)
        components.html(htc_html, height=1200)


with col2:
    create_card("AMPL Cleantech Pvt Ltd, India", "Assistant Manager - Design", 
            ["Directed solar project designs, assessments, and technical reports.",
             "Drove team performance in project execution and tendering.",
             "Facilitated a $140M equity raise for a 214MWp PV project.",
             "Managed 10MW to 500MW projects with top contractors."], header_color="#28A745")

    st.write('\n')
    st.write('\n')    
    # Expander for additional details
    with st.expander("See more about my role at AMPL Cleantech"):
        ampl_sections = {
    "Job Role and Responsibilities": [
        "Managed solar project feasibility, design reviews, and energy yield modeling.",
        "Key in vendor assessment, RFP preparation, and techno-commercial reporting.",
        "Reviewed and finalized EPC contractors and equipment suppliers.",
        "Implemented evaluation metrics for utility PV plant sites and conducted Plant Acceptance Tests.",
        "Collaborated with finance for project profitability & vialbility analysis."
    ],
    "Key Projects and Achievements": [
        "Integral in 10MW to 500MW projects, collaborating with top contractors like L&T ECC, Sterling & Wilson, and TATA Power.",
        "Managed 1GW+ of solar projects, enhancing each phase from pre-tender to post-tender.",
        "Led 190MW PV projects' asset management, innovating for increased revenue and efficiency.",
        "Implemented drone thermography, saving $2.5M annually over 20 years in 25MWp assets."
    ],
    "Skills and Expertise": {
        "Technical Skills": [
            "Expert in PVSyst, Helioscope, SolarGIS for energy modeling and design.",
            "Advanced monitoring and predictive energy yield analysis skills.",
            "Comprehensive technical evaluations for optimal equipment selection."
        ],
        "Managerial and Leadership Experience": [
            "Led a team of engineers, promoting technical excellence and efficiency.",
            "Directed technical inspections and quality assurance in solar module manufacturing."
        ]
    },
    "Innovation and Strategic Initiatives": [
        "Pioneered in Solar-BESS projects, focusing on Round The Clock Mechanism.",
        "Evaluated top battery and inverter technologies for major 100MW Solar PV with 100MWh Energy storage project.",
        "Assessed industry-leading products for solar technology advancements."
    ],
    "Financial Acumen and Stakeholder Interaction": [
        "Engaged in technical due diligence for significant fundraising, securing substantial equity.",
        "Played a pivotal role in stakeholder interactions for financial project viability.",
        "Engaged with major Leading financial agencies from India."
    ]
}

        ampl_html = generate_expander_html(ampl_sections)
        components.html(ampl_html, height=1200)
        

with col1:
    create_card("Kirti Solar Limited", "Technical Lead", 
            ["Managed PV project designs and simulations.",
             "Oversaw a junior engineer duo for project and tender execution.",
             "Commissioned a 1MWp solar rooftop at Sharda University.",
             "Implemented small to medium off-grid and hybrid solar projects."],header_color="#3CB371")

    st.write('\n')
    st.write('\n') 
    
    with st.expander("See more about my role at KSL"):
        ksl_sections = {
    "Job Role and Responsibilities": [
        "Managed design engineering, energy analysis & project rollout",
        "Oversaw site layout planning and tender document preparation.",
        "Conducted client and stakeholder meetings for project alignment.",
        "Supervised two junior engineers in project execution and tender processes."
    ],
    "Key Projects": [
        "Led a 1MWp solar rooftop system design and commissioning at Sharda University, Delhi NCR.",
        "Developed a 100kW rooftop PV system for a Community Center in New Town, Kolkata.",
        "Executed small to medium-scale commercial off-grid and hybrid solar projects, including a 35kW-100kWh Solar BES project."
    ],
    "Achievements": [
        "Managed end-to-end processes for high-profile and diverse solar installations.",
        "Enhanced company's project execution capabilities and team leadership.",
        "Diversified project portfolio with hybrid and off-grid solar solutions."
    ],
    "Skills Utilized": {
        "Technical Skills": [
            "Proficiency in PVsyst, Helioscope, and SAM for energy modeling and design.",
            "Expertise in efficient solar power system design for grid-connected and off-grid projects."
        ],
        "Managerial Skills": [
            "Effective team management and project execution oversight.",
            "Strong communication skills for client and stakeholder engagement."
        ]
    },
    "Learnings and Development": [
        "Gained practical experience in solar PV project execution.",
        "Developed a deep understanding of solar technologies across various project environments."
    ]
}

        ksl_html = generate_expander_html(ksl_sections)
        components.html(ksl_html, height=900)
        
with col2:
    create_card("O3 Energy Solutions LLC", "Senior Design Engineer", 
            ["Prepared design permit packages for solar PV projects.",
             "Specialized in 100kW to 3MW rooftop and carpark solar installations.",
             "Facilitated design updates across projects in Dallas, Florida, and Guam.",
             "Ensured design compliance and project approval readiness."], header_color="#FF5733")
    st.write('\n')
    st.write('\n') 
    
    with st.expander("See more about my role at O3 Energy"):
        o3_sections = {
    "Job Role and Responsibilities": [
        "Senior Design Engineer, focused on creating Design Permit Packages for solar PV projects in USA Mainland and US territories.",
        "Specialized in 100kW to 3MW commercial rooftop and carpark solar project designs.",
        "Coordinated with the US team for design updates and project modifications."
    ],
    "Key Projects": [
        "Worked on various projects across Dallas, Florida, and Guam, contributing to the commercial solar portfolio.",
        "Expertise in site layouts, system 3-line diagrams, structural drawings, and electrical system sizing."
    ],
    "Technical Contributions": [
        "Crafted PVsyst-based system designs for comprehensive techno-economic analysis.",
        "Ensured design compliance and readiness for permit package approvals."
    ],
    "Collaborative Work": [
        "Collaborated with offshore office in Chandigarh, India, aligning with the US team.",
        "Managed cross-continental communication and design updates."
    ],
    "Short Tenure Achievements": [
        "Significantly enhanced project design and execution efficiency in a brief tenure.",
        "Quickly adapted to company workflows, delivering high-quality designs for multiple projects."
    ]
}
        
        o3_html = generate_expander_html(o3_sections)
        components.html(o3_html, height=900)


with col1:
    create_card("OhmSolar & Technologies", "Co-founder and Sr Consultant", 
            ["Launched tech consultancy with a user-friendly Solar Design App.",
             "Guided design engineering for global projects up to 140MW.",
             "Achieved 'Best 40 Startups of the Year' in West Bengal, India.",
             "Expanded consulting to 18 countries, fostering solar development."], header_color="#FFC107")


    st.write('\n')
    st.write('\n') 
    
    with st.expander("See more about my role at OhmSolar & Technologies"):
        ohm_sections = {
    "Job Role and Responsibilities": [
        "Co-founded OhmSolar & Technologies, serving as Senior Consultant.",
        "Developed a user-friendly Solar Design Engineering App for technology consulting.",
        "Led design engineering for 1MW to 140MW projects globally, focusing on project feasibility and techno-economic analysis.",
        "Managed client consultations and decision-making guidance."
    ],
    "Key Projects and Consultation": [
        "Consulted on a 140MW utility-scale project in Isfahan, Iran, and projects in South Africa, Nigeria, Rwanda, and India.",
        "Addressed needs of diverse projects, from small installations to large utility projects.",
        "Created Detailed Project Reports and selected appropriate technology solutions."
    ],
    "Achievements": [
        "Guided startup to win 'Best 40 Startups of the Year' in West Bengal, India, for 2014-2015.",
        "Expanded consulting services across 18 countries, enhancing global solar project development.",
        "Initiated development of a SAAS-based platform for automating solar PV design."
    ],
    "Skills Utilized": {
        "Technical Skills": [
            "Expertise in PVsyst for pre-feasibility studies and solar project planning.",
            "Proficiency in BOQ preparation and selecting optimal project equipment."
        ],
        "Managerial Skills": [
            "Led a team of engineers and interns, enhancing project communication and stakeholder management."
        ]
    },
    "Entrepreneurial Journey and Learnings": [
        "Navigated startup management and software development challenges in the solar industry.",
        "Acquired insights into market demands and technological solutions globally."
    ],
    "Exit and Transition": [
        "Successfully exited the company, contributing significantly to its growth and technological advancement."
    ]
}

        ohm_html = generate_expander_html(ohm_sections)
        components.html(ohm_html, height=900)
        
        
with col2:
    create_card("Annapurna Export", "Project Engineer", 
            ["Managed PV projects and solar-powered off-gird installations.",
             "Deployed project teams, for efficient delivery across India.",
             "Led system designs and quality checks for government and residential projects.",
             "Boosted the company's execution capabilities in the solar sector."], header_color="#17A2B8")



    st.write('\n')
    st.write('\n') 
    
    with st.expander("See more about my role at Annapurna Export"):
        apex_sections = {
    "Job Role and Responsibilities": [
        "Project Engineer at Annapurna Export, focusing on small-scale PV projects and government solar initiatives.",
        "Handled BOQ preparation, project cost estimation, and vendor assessments.",
        "Managed and deployed project teams across Eastern India for solar installations."
    ],
    "Project Management and Execution": [
        "Coordinated with onsite and office teams for timely project delivery.",
        "Oversaw system design, drawing preparation, and quality assurance.",
        "Engaged with government agencies and consultants to ensure project compliance."
    ],
    "Support and Coordination": [
        "Supported the sales team in bidding and pre-sales engineering.",
        "Facilitated communication between clients, consultants, and internal teams."
    ],
    "Achievements and Contributions": [
        "Instrumental in the execution of several small-scale solar projects.",
        "Enhanced the company's capabilities in solar project management and execution."
    ]
}

        apex_html = generate_expander_html(apex_sections)
        components.html(apex_html, height=700)
        
col1,col2,col3=st.columns([0.75,1.5,0.75])
with col2:
    create_card("ONergy", "Project Coordinator", 
            ["Coordinated solar PV system designs and on-site execution.",
             "Implemented solar mini-grids in rural villages, enhancing community living.",
             "Installed solar-powered water irrigation in West Bengal.",
             "Facilitated Solar energy projects with TERI and the World Bank."], header_color="#6f42c1")
    st.write('\n')
    st.write('\n') 
    
    with st.expander("See more about my role at ONergy"):
        onergy_sections = {
    "Job Role and Responsibilities": [
        "Project Coordinator at ONergy, focusing on system design, BOQ preparation, and vendor assessment.",
        "Managed coordination between project sites and office teams for project progression.",
        "Regularly deputed on-site for direct project execution."
    ],
    "Key Projects and Implementation": [
        "Specialized in small-scale solar PV installations for government and private sectors.",
        "Established PV mini-grid systems in three remote villages in Jharkhand, impacting 25-30 houses per village.",
        "Designed and installed solar PV systems with battery storage, and commissioned a solar-powered water irrigation system in West Bengal."
    ],
    "Collaborative Efforts and Contributions": [
        "Collaborated with TERI and the World Bank to enhance rural and remote village lifestyles.",
        "Integral in integrating sustainable energy solutions in underserved communities."
    ],
    "Professional Growth and Learning": [
        "Gained hands-on experience in solar project execution and coordination.",
        "Developed a comprehensive understanding of rural solar energy challenges and applications."
    ]
}


        onergy_html = generate_expander_html(onergy_sections)
        components.html(onergy_html, height=700)
        
st.write('\n')
st.write('\n')     
st.write('\n')
st.write('\n')
st.write('\n')



#-----Academic Qualification-----------#

edu_intro=f"""Welcome to my professional profile! I'm an Electrical Engineering graduate from MAKAUT with a lifelong commitment to learning.
 My postgraduate endeavors and certifications include advanced solar energy studies from TU Delft,
 business management from IIM Bangalore, financial modeling from Wharton, and data science from Harvard X. 
 These courses have equipped me with a robust foundation to excel in the renewable energy sector.
"""
components.html(app_css + create_section_header("Academic Qualification & Certifications"), height=100)
components.html(intro_css + create_section_intro(edu_intro)
                                                 , height=150)

education_html = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

.education-section {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    margin-bottom: 20px;
}

.education-card {
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    margin: 10px;
    overflow: hidden;
    width: 300px; /* Width of the card */
    display: flex; /* Added for flexbox layout */
    flex-direction: column; /* Stack children vertically */
    align-items: center; /* Center children horizontally */
    text-align: center; /* Center text */
    font-family: 'Roboto', sans-serif;
}

    .education-card img {
    max-width: calc(150px - 20px); /* Subtracting the total padding from the width */
    height: 150px; /* Maintain aspect ratio */
    object-fit: contain;
    padding: 10px; /* Padding around the image */
    }
    
    .card-content {
    padding: 15px;
    }
    
    .card-content h4 {
    margin-top: 0;
    color: #333;
    font-weight: 700; /* Roboto bold for headers */
    }
    
    .card-content p {
    color: #666;
    font-weight: 400; /* Roboto regular for paragraphs */
    }
    </style>
    
    <div class="education-section">
        <div class="education-card">
            <img src="https://i.imgur.com/8oLnZZt.png" alt="College Image">
            <div class="card-content">
                <h4>B.Tech in Electrical Engineering</h4>
                <p>West Bengal University of Technology, 2009-2013</p>
            </div>
        </div>
        <div class="
    education-card">
    <img src="https://i.imgur.com/o2BAJZl.png" alt="Certification Image">
    <div class="card-content">
    <h4>Certificate-Advanced Solar Energy</h4>
    <p>TU Delft (Online), 2013</p>
    </div>
    </div>
    
    <div class="
    education-card">
    <img src="https://i.imgur.com/o1Nu9QD.png" alt="Certification Image">
    <div class="card-content">
    <h4>Micro Masters in General Business Management</h4>
    <p>IIM Bangalore, 2017 - 2018</p>
    </div>
    </div>
    
    <div class="
    education-card">
    <img src="https://i.imgur.com/WzpTJib.jpg" alt="Certification Image">
    <div class="card-content">
    <h4>Certificate in Financial Modelling</h4>
    <p>Wharton Business School, 2017 - 2018</p>
    </div>
    </div>
    
    <div class="
    education-card">
    <img src="https://i.imgur.com/o7DVF65.png" alt="Certification Image">
    <div class="card-content">
    <h4>Certificate- Data Science using R</h4>
    <p>Harvard T. Chan School of Public Health, 2018</p>
    </div>
    </div>
    
    <div class="
    education-card">
    <img src="https://i.imgur.com/W8Hu1iN.jpg" alt="Certification Image">
    <div class="card-content">
    <h4>Certificate-Data Analysis & Visualization</h4>
    <p>PwC Academy (Online), 2017-2018</p>
    </div>
    </div>
    
    <!-- Add more cards as needed -->
    
    </div>
"""


# Render the custom HTML/CSS in the Streamlit app
components.html(education_html, height=800)

#------software skills-------#
sw_intro=f""" Below are visual representations of my skills across various technical tools, 
illustrated through a horizontal bar chart and a radar chart. 
These charts reflect my expertise and proficiency levels in essential software tools like 
PVsyst, AutoCAD, SketchUp, and more, highlighting my comprehensive skill set in the Solar energy sector.
"""
components.html(app_css + create_section_header("Software Skills Proficiency"), height=100)
components.html(intro_css + create_section_intro(sw_intro)
                                                 , height=120)
#----radar chart w/o prfecieny level and with logos------#



# Function to encode image file to base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Skills to display and their corresponding image file names
skills = ['PVsyst', 'AutoCAD', 'SketchUp', 'Helioscope', 'Python', 'pvlib']
# Assume the image names are the same as the skill names
image_folder = 'images'

# Create the radar chart
fig = go.Figure()

# Add radar chart trace
fig.add_trace(go.Scatterpolar(
    r=[1] * len(skills),  # Set a fixed radius for all skills
    theta=skills,
    fill='toself',
    fillcolor='rgba(135, 206, 250, 0.7)',  # Light blue with 70% opacity
    line_color='blue',  # Solid blue line color
    showlegend=False
))

# Calculate angle and radius for logo placement
angles = np.linspace(0, 2 * np.pi, len(skills), endpoint=False).tolist()  # Divide the circle into equal parts
angles += angles[:1]  # Ensure the list is cyclic
radius = 1.1  # Radius where logos will be placed

# Add logos as annotations
for skill, angle in zip(skills, angles):
    logo_path = os.path.join(image_folder, skill + '.png')
    if os.path.isfile(logo_path):
        encoded_image = encode_image(logo_path)
        fig.add_layout_image(
            dict(
                source=f"data:image/png;base64,{encoded_image}",
                xref="paper", yref="paper",
                x=0.5 + radius * np.cos(angle) / 3,
                y=0.5 + radius * np.sin(angle) / 2,
                sizex=0.2,  # Adjust based on the chart size and image resolution
                sizey=0.2,  # Adjust based on the chart size and image resolution
                xanchor="center",
                yanchor="middle",
                layer="above"
            )
        )
    else:
        st.error(f"Image for {skill} not found at path: {logo_path}")

# Update the layout to show the radial axis
fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,  # Show the radial axis
            range=[0, 1],  # The range of your scale
        ),
        angularaxis=dict(
            tickfont=dict(
                color='white'  # Set the text color for software names to white
            ),
        )
    ),
    title=" ",
)

# Display the radar chart in Streamlit
col1, col2=st.columns(2)
col1.plotly_chart(fig, use_container_width=True)

#----------#

import plotly.express as px

# Define your skills and proficiency levels
skills_data = {
    'skills': ['PVsyst', 'AutoCAD', 'SketchUp', 'Helioscope', 'Python', 'PVlib'],
    'proficiency': [90, 80, 85, 95, 75, 65]  # Proficiency levels out of 100
}

# Create a DataFrame
df_skills = pd.DataFrame(skills_data)

# Define a list of colors for the bars
colors = ['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3']

# Create a horizontal bar chart with different colors
fig = px.bar(df_skills, x='proficiency', y='skills', orientation='h',
             color='skills', color_discrete_sequence=colors)
fig.update_layout(
    autosize=True,
width=None, # It will be set automatically to page width
xaxis=dict(
title='Proficiency Level',
range=[0, 100] # Define the range of proficiency levels
    ),
    yaxis=dict(
        title='Skills'
    ),
    title=" ", showlegend=False
)

# Display the horizontal bar chart in Streamlit
col2.plotly_chart(fig, use_container_width=True)

#----------#

#-----Technologies Worked With-----#


components.html(app_css + create_section_header("Technological Experience"), height=100)




def create_flip_card(image_url, tech_names, title="My Technologies"):
    flip_card_html = f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

    .flip-card {{
      background-color: transparent;
      width: 200px;
      height: 200px;
      perspective: 1000px;
    }}

    .flip-card-inner {{
      position: relative;
      width: 100%;
      height: 100%;
      text-align: center;
      transition: transform 0.6s;
      transform-style: preserve-3d;
      box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
    }}

    .flip-card:hover .flip-card-inner {{
      transform: rotateY(180deg);
    }}

    .flip-card-front, .flip-card-back {{
      position: absolute;
      width: 100%;
      height: 100%;
      -webkit-backface-visibility: hidden;
      backface-visibility: hidden;
    }}

    .flip-card-front {{
      background-color: #bbb;
      color: black;
      z-index: 2;
    }}

    .flip-card-back {{
      background-color: #2980b9;
      color: white;
      transform: rotateY(180deg);
      z-index: 1;
      font-family: 'Roboto', sans-serif;
      padding-top: 15px; /* Padding at the top for the title */
    }}

    .flip-card-back h2 {{
      font-size: 18px;
      margin: 10px; /* Remove default margin */
    }}

    .flip-card-back ul {{
      list-style-type: circle; /* Bullet point style */
      padding: 10px;
      margin: 10px 0 0 0; /* Reduced gap between title and bullets */
    }}

    .flip-card-back li {{
      font-size: 16px;
      text-align: center; /* Align text to the left */
      padding-left: 0px; /* Padding for bullet points */
      margin: 5px 0; /* Reduced gap between bullet points */
    }}
    </style>

    <div class="flip-card">
      <div class="flip-card-inner">
        <div class="flip-card-front">
          <img src="{image_url}" alt="Avatar" style="width:200px;height:200px;">
        </div>
        <div class="flip-card-back">
<h2>{title}</h2>
<ul>
"""


    for tech in tech_names:
        flip_card_html += f"<li>{tech}</li>"

    flip_card_html += """
          </ul>
        </div>
      </div>
    </div>
    """
    
    return flip_card_html



# Example usage
flip_card1 = create_flip_card("https://i.imgur.com/P3NPpMd.png", ["Mono-Si N type","Poly & Mono Si", "Mono PERC", "Thin-Film"], "Solar PV Module")
flip_card2 = create_flip_card("https://i.imgur.com/ujokNtd.jpg", ["Central", "String", "Optimizers","Hybrid"], "Solar Inverters")
flip_card3 = create_flip_card("https://i.imgur.com/JW510fO.jpg", ["LiFeO4", "Lead-Acid", "Ni-Cd"], "Energy Storage")
flip_card4 = create_flip_card("https://i.imgur.com/pAUYH37.png", ["Ground-Mount", "Sheds", "Flat Roofs","Carparks"], "Type of Instllations")
flip_card5 = create_flip_card("https://i.imgur.com/w0hO6qa.png", ["Utility Scale", "Commercial Captive", "Residential"], "Type of Utilization")
flip_card6 = create_flip_card("https://i.imgur.com/2hZNL7Y.png", ["Grid-Connected", "StandAlone", "DG Hybrid", "BESS"], "Type of Connectivity")

# Render the flip cards in the Streamlit app

col1,col2, col3=st.columns(3)

with col1:
    components.html(flip_card1, height=300)
    
with col2:
    components.html(flip_card2, height=300)
    
with col3:
    components.html(flip_card3, height=300)
    
with col1:
    components.html(flip_card4, height=300)
    
with col2:
    components.html(flip_card5, height=300)
    
with col3:
    components.html(flip_card6, height=300)
    
    
#-------Brands Cards------#

components.html(app_css + create_section_header("Tier-1 Brands I have Worked With"), height=100)


# HTML and CSS structure for the brand showcase with flip card effect and two rows of cards
brand_showcase_html = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

.grid-container {
  display: grid;
  grid-template-columns: repeat(2, 1fr); /* 2 columns */
  grid-gap: 10px; /* Gap between cards */
  padding: 10px;
}

.flip-card {
  background-color: transparent;
  width: 200px; /* Width of the card */
  height: 200px; /* Height of the card */
  perspective: 1000px;
  margin: 10px auto; /* Center card in the grid cell */
}

.flip-card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  text-align: center;
  transition: transform 0.6s;
  transform-style: preserve-3d;
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.flip-card:hover .flip-card-inner {
  transform: rotateY(180deg);
}

.flip-card-front, .flip-card-back {
  position: absolute;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'Roboto', sans-serif;
}

.flip-card-front {
  background-color: #f3f3f3;
  color: black;
}

.flip-card-back {
  background-color: #007BFF;
  color: white;
  transform: rotateY(180deg);
}

.brand-list {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

.brand-item {
  background: #fff;
  margin: 5px;
  padding: 5px;
  border-radius: 4px;
  color: red; /* Brand text in red */
}
</style>

<div class="grid-container">
  <!-- First row of cards -->
  <div class="flip-card">
    <div class="flip-card-inner">
      <div class="flip-card-front">
        <h3>Solar Panels</h3>
      </div>
      <div class="flip-card-back">
        <ul class="brand-list">
          <li class="brand-item">Longi Solar</li>
          <li class="brand-item">Jinko Solar</li>
          <li class="brand-item">Canadian Solar</li>
          <li class="brand-item">Vikram Solar</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="flip-card">
    <div class="flip-card-inner">
      <div class="flip-card-front">
        <h3>Solar Inverters</h3>
      </div>
      <div class="flip-card-back">
        <ul class="brand-list">
          <li class="brand-item">Sungrow</li>
          <li class="brand-item">ABB</li>
          <li class="brand-item">SMA</li>
          <li class="brand-item">Fronious</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- Second row of cards -->
  <!-- Repeat the structure for additional cards, modify titles and brands as needed -->
  <!-- ... -->
  <div class="flip-card">
    <div class="flip-card-inner">
      <div class="flip-card-front">
        <h3>Solar Energy Storage</h3>
      </div>
      <div class="flip-card-back">
        <ul class="brand-list">
          <li class="brand-item">Sungrow</li>
          <li class="brand-item">Panasonic</li>
          <li class="brand-item">LG Chem</li>
          <li class="brand-item">Alpha ESS</li>
        </ul>
      </div>
    </div>
  </div>

    <div class="flip-card">
      <div class="flip-card-inner">
        <div class="flip-card-front">
          <h3>Solar Contractors</h3>
        </div>
        <div class="flip-card-back">
          <ul class="brand-list">
            <li class="brand-item">TATA Solar</li>
            <li class="brand-item">L&T ECC</li>
            <li class="brand-item">Sterlin Wilson Solar</li>
            <li class="brand-item">GE Gamesa</li>
          </ul>
        </div>
      </div>
    </div>


</div>
"""

# Rendering the HTML structure in Streamlit
components.html(brand_showcase_html, height=600) # Adjust height as necessary


#----AI SKillset------#

ai_intro=f""" Skilled in AI, I specialize in crafting advanced machine learning solutions,
focusing on predictive analytics and natural language processing, 
and turning complex challenges into practical, impactful applications.
"""
components.html(app_css + create_section_header("Data Science and AI Skills Proficiency"), height=100)
components.html(intro_css + create_section_intro(ai_intro)
                                                 , height=120)


#----AI Skillset----#
col1,col2,col3=st.columns(3)
col2.button('Click the Brain')
# HTML and CSS structure for the interactive skill set
skillset_html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  position: relative;
}

.circle {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  position: absolute;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s ease;
}

.circle img {
  width: 80%;
  height: auto;
  border-radius: 50%;
}

.main-circle {
  z-index: 2;
}

.hidden-circle {
  visibility: hidden;
  opacity: 0;
  transform: scale(0);
}

.show {
  visibility: visible;
  opacity: 1;
  transform: scale(1);
}

/* Correct the positioning for each skill circle */
.skill1 { top: 50%; left: 50%; transform: translate(-150%, -150%) scale(1); }
.skill2 { top: 50%; left: 50%; transform: translate(150%, -150%) scale(1); }
.skill3 { top: 50%; left: 50%; transform: translate(-150%, 150%) scale(1); }
.skill4 { top: 50%; left: 50%; transform: translate(150%, 150%) scale(1); }
.skill5 { top: 50%; left: 50%; transform: translate(-250%, 0) scale(1); }
.skill6 { top: 50%; left: 50%; transform: translate(250%, 0) scale(1); }
</style>
</head>
<body>

<div class="container">
  <div class="circle main-circle" id="ai-skills">
    <img src="https://i.imgur.com/wVq6heI.png alt="AI Skills">
  </div>
  <div class="circle hidden-circle skill1">
    <img src="https://i.imgur.com/AupELFG.png" alt="ChatGPT">
  </div>
  <div class="circle hidden-circle skill2">
    <img src="https://i.imgur.com/qtfzb0U.png" alt="Jasper AI">
  </div>
  <div class="circle hidden-circle skill3">
    <img src="https://i.imgur.com/5j1BBsP.png" alt="Midjourney">
  </div>
  <div class="circle hidden-circle skill4">
    <img src="https://i.imgur.com/Za20gJf.png" alt="Stable Diffision">
  </div>
  <div class="circle hidden-circle skill5">
   <img src="https://i.imgur.com/99SGiRM.png" alt="Sembly AI">
  </div>
  <div class="circle hidden-circle skill6">
    <img src="https://i.imgur.com/fUcnsRq.png" alt="Bard AI">
  </div>
  <!-- Add other skill circles with images here -->
</div>

<script>
const mainCircle = document.querySelector('#ai-skills');
const hiddenCircles = document.querySelectorAll('.hidden-circle');

mainCircle.addEventListener('click', () => {
  hiddenCircles.forEach(circle => {
    circle.classList.toggle('show');
  });
});
</script>

</body>
</html>

"""

# Display the skill set in Streamlit
components.html(skillset_html, height=500)

components.html(app_css + create_section_header("My Web App Portfolio"), height=100)

# Define your apps
apps = [
    {"name": "Solar Energy Estimator", "url": "https://solarenergyestimatorv01.streamlit.app/",
     "thumbnail": "https://i.imgur.com/i76savr.png", "description": "Solar Yield and Financial Analysis with Streamlit & PVLib"},
    
    {"name": "Sub-Hourly Irradiance Forecast", "url": "https://amritpvre-hourly-ghi-sub-hourly-ghi-gii-forecast-app-v01-ubmari.streamlit.app/",
     "thumbnail": "https://i.imgur.com/075avwK.png", "description": "Detailed Solar Forecasting, Sub-Hourly Accuracy"},
    
    {"name": "Solar Energy EDA Dashboard", "url": "https://amritpvre-kpviz--v-01-2-main-app-jkg9wr.streamlit.app/",
     "thumbnail": "https://i.imgur.com/fkrSjYa.png?1", "description": "Comprehensive Solar 8760 Data Analytical Insight"},
    
    {"name": "LinkCRaft V.01", "url": "https://linkcraft-v01.streamlit.app/",
     "thumbnail": "https://i.imgur.com/co2sQH6.png?1", "description": "AI-Driven LinkedIn Content Creation Tool."},
    
    {"name": "Yahoo Finance NSE Tracker", "url": "https://yflivetracker-nse.streamlit.app/",
     "thumbnail": "https://i.imgur.com/RRSwz4c.png?1", "description": "Real-Time NSE Stock Data Visualization."},
    
    {"name": "Solar Project Enquery App V.01", "url": "https://amritpvre-solar-query-form-solar-inquery-v02-w0jlqr.streamlit.app/",
     "thumbnail": "https://i.imgur.com/ljSjdtq.png", "description": "Streamlined Solar Project Information Collection."},
    
]

# HTML and CSS for the card layout
html = """
<link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600&display=swap" rel="stylesheet">
<style>
.grid-container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  background-color: #F5F5F5; /* Light gray background */
  padding: 30px;
}

.card {
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
  transition: 0.3s;
  border-radius: 5px;
  text-align: center;
  background-color: #fff;
  font-family: 'Open Sans', sans-serif; /* Apply the font */
}

.card:hover {
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
}

.card img {
  border-radius: 5px 5px 0 0;
  width: 316px;
  height: 316px;
  object-fit: cover; /* Adjust as needed */
}

.container {
  padding: 2px 16px;
}

.card-title {
  font-size: 1.1em;
  margin-bottom: 5px;
}

.card-description {
  font-size: 0.9em;
  color: #555;
  margin-bottom: 10px
}
</style>
<div class="grid-container">
"""

# Add a card for each app
for app in apps:
    html += f"""
    <div class="card" onclick="window.open('{app['url']}');">
      <img src="{app['thumbnail']}" alt="{app['name']}">
      <div class="container">
        <div class="card-title"><b>{app['name']}</b></div>
        <div class="card-description">{app['description']}</div>
      </div>
    </div>
    """

# Close the grid container div
html += "</div>"

# Use Streamlit's components.html to render the card layout
components.html(html, height=900)

#---------#

#-------Wordcloud Matplotlib-------#
components.html(app_css + create_section_header("Managerial Skillset"), height=100)


# List of managerial skills, you can add more words or increase the frequency of the words to emphasize them
managerial_skills = [
    "Leadership", "Teamwork", "Communication", "Strategic Planning",
    "Project Management", "Budgeting", "Negotiation", "Conflict Resolution",
    "Decision Making", "Risk Management", "Time Management", "Adaptability",
    "Problem Solving", "Motivation", "Coaching", "Mentoring",
    "Crisis Management", "Organization", "Delegation", "Innovation"
]

# Generate the word cloud text as repeated instances of the skills
text = ' '.join(managerial_skills)

# Create the word cloud object
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Display the generated image:
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
st.pyplot(plt)


def display_skill_info(skill_name, description):
    # Toggle button to show/hide skill information
    if st.button(skill_name, key=skill_name):
        st.info(description)

# Styling for the cards
st.markdown("""
    <style>
        .css-2trqyj {
            background-color: #f1f1f1;  /* Light grey background */
            border-radius: 10px;
            padding: 10px;
            margin: 5px 0;
        }
        .stButton>button {
            width: 100%;
            height: 3em;
            font-size: 16px;
            font-weight: bold;
            border-radius: 10px;
            border: 1px solid #007BFF;
            color: #007BFF;
        }
    </style>
""", unsafe_allow_html=True)

# Display each skill as a clickable card
col1,col2=st.columns(2)

with col1:
    display_skill_info("Leadership", "Spearheaded diverse solar projects, leading a team of engineers through the successful completion of the groundbreaking PDO Noor project.")
with col2:
    display_skill_info("Project Management", "Expertly managed large-scale solar installations including a 5MW Smart City project for PDO.")
with col1:
    display_skill_info("Strategic Planning", "Devised and implemented strategic plans for the deployment of innovative solar solutions, notably in the 4MW+ mall rooftop projects for MAF.")
with col2:
    display_skill_info("Decision Making", "Efficiently made key decisions during the development of Battery Energy Storage Systems and electric vehicle charging infrastructures.")
with col1:
    display_skill_info("Risk Management", "Identified and mitigated project risks in high-stakes environments, ensuring the seamless execution of complex solar projects.")
with col2:  
    display_skill_info("Time Management", "Expertly managed project timelines, ensuring timely completion of solar installations like the 5MW Smart City project for PDO.")

#--------#

#------AI Chatbot-------#

#-----preloaded pdf chatbot-------#



openai.api_key = 'openai_api'

# Assuming the PDF file is named 'example.pdf' and is in the root directory of the app
pdf_filename = 'About_me.pdf'

def extract_text_from_pdf(pdf_filename):
    with pdfplumber.open(pdf_filename) as pdf:
        text = ''.join(page.extract_text() for page in pdf.pages)
    return text

def query_model(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-1106",
        messages=messages
    )
    return response.choices[0].message['content']

# Load and display the PDF content
context = extract_text_from_pdf(pdf_filename)

# Streamlit interface
with st.sidebar: 
    st.title('Ask a Question About Me')
    
    # Display the context in the app for user reference (optional)
    #st.text_area("Content of the PDF", context, height=300)
    
    # User query input
    user_query = st.text_input("Ask a question based on my professional journey")
    
    # Displaying response
    if user_query:
        # Prepare messages for the chat history
        messages = [{"role": "system", "content": context}, {"role": "user", "content": user_query}]
        answer = query_model(messages)
        st.write(answer)
