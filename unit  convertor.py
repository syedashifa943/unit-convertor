#Project 01: Unit Convertor
#Build a Google Unit Convertor using Python and Streamlit:

import streamlit as st
st.markdown(
    """
    <style>
    body {
        background-color: #1e1e2f;
        color: white;
    }
    .stApp{
        background:linear_gradient(135deg,  #bcbcbc,  #cfe2f3);
        padding:30px;
        border-radius:15px
        box-shadow:0px 10px 30px rgba(0,0,0,0.3)
    }
    h1 {
        text-align:center;
        font-size:36px;
        color;white;
    }
    .stButton>button{
        background:linear-gradient(45deg, #0b5394, #351c75);
        color: white;
        font-size: 18px
        paddingL 10px 20px;
        border-radius: 10px
        transition: 0.3s;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.4)
    }
    .stButton>button:hover{
        transform: scale(1.05)
        background:linear-gradient(45deg, #92fe9d, #00c9ff)
        color: black
    }
    .result-box {
        font-size: 20px;
        font-weight: bold;
        text-align: center:
        background: rgba(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 10px;
        marging-top: 20px;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.3);
    }
    .footer{
        text-align: center
        marging-top: 50px;
        font-size: 14px;
        color: black
    }
    </style>
    """,
    unsafe_allow_html=True 
)

#title and discription:
st.markdown("<h1> Unit Convertor using Python and Streamlit </h1>", unsafe_allow_html=True)
st.write("Easily converts between different units of length, weight, and temperature.")

#sidebar menu"
conversion_type = st.sidebar.selectbox("Choose Conversion Type", ["Length", "Weight", "Temperature"])
value = st.number_input("Enter Value", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Kilograms", "Centimeters", "Milimeters", "Miles", "Feet", "Yards", "Inches"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Kilograms", "Centimeters", "Milimeters", "Miles", "Feet", "Yards", "Inches"])
elif conversion_type == "Weight":
    with col1:
        to_unit = st.selectbox("From", ["Kilometer", "Grams", "Pounds", "Ounces", "   Miligrams"])
    with col2:
        to_unit = st.selectbox("To", ["Kilometer", "Grams", "Pounds", "Ounces", "Miligrams"])
elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])

#converter function
#converted function
def lenght_converter(value, from_unit, to_unit):
    lenght_units = {
        "Meters": 1, "Kilometers": 0.001, "Centimeters": 100, "Milimeters": 1000, 
        "Miles": 0.000621371, "Feet": 3.28, "Yards": 1.09361, "Inches": 39.37
    }
    return (value / lenght_units[from_unit]) * lenght_units[to_unit]

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        "Kilograms": 1, "Grams": 1000, "Pounds": 2.20462, "Ounces": 35.274, "Miligrams": 1000000
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]

def temperature_converter(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit" :  
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
            return value

#button for conversion
if st.button("Convert"):
    if conversion_type == "Length":
        result = lenght_converter(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_converter(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temperature_converter(value, from_unit, to_unit)
    st.markdown(f"<div class='result-box'>{value} {from_unit} is equal to {result:.4f} {to_unit}</div>", unsafe_allow_html=True)

st.markdown("<div class='footer'>Developed by [syeda shifa]<div>", unsafe_allow_html=True)
