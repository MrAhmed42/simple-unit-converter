import streamlit as st

length_units = {'Meter':1 , 'Kilometer': 0.001 , 'Mile': 0.000621371}
weight_units = {'Kilogram':1 , 'Gram':1000 , 'Pound': 2.20462}
temperature_units = ['Celsius', 'Fahrenheit', 'Kelvin']
time_unit = {'Second':1 , 'Minute':1/60 , 'Hour':1/3600}

def convert_temperature(value,from_unit,to_unit):
    if from_unit == to_unit:
        return value
    
    if from_unit == "Celsius" :
        return(value * 9/5) + 32 if to_unit == "Fahrenheit" else value + 273.15
    
    if from_unit == "Fahrenheit" : 
        return(value - 32) * 5/9 if to_unit == "Celsius" else ((value - 32) * 5/9) + 273.15 
    
    if from_unit == "Kelvin" :
        return value - 273.15 if to_unit == "Celsius" else ((value - 273.15) * (9/5)) +32
    
st.title("Unit Converter")
unit_type = st.selectbox("Select Unit Type",["Length","Weight","Temperature","Time"])

if unit_type == "Length":
    units = length_units
elif unit_type == "Weight":
    units = weight_units
elif unit_type == "Temperature":
    units = temperature_units
elif unit_type == "Time":
    units = time_unit

from_unit = st.selectbox("From Unit",list(units))
to_unit = st.selectbox("To Unit",list(units))

value = st.number_input("Enter Value",min_value=0.0, format="%.2f")

if st.button("Convert") :
    if unit_type == "Temperature" :
        result = convert_temperature(value,from_unit,to_unit)

    else:
        result = value * (units[to_unit] / units[from_unit]) 

    st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")       


