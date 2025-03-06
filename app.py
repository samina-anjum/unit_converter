import streamlit as st

# App Title
st.title("Unit Converter")

# Conversion Types
conversion_types = ["Length", "Weight", "Temperature"]

# User input for conversion type
conversion_choice = st.selectbox("Choose conversion type", conversion_types)

# Length Conversion
if conversion_choice == "Length":
    length_units = ["meters", "kilometers", "feet", "inches", "centimeters"]
    
    input_value = st.number_input("Enter length value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("Choose from unit", length_units)
    to_unit = st.selectbox("Choose to unit", length_units)

    # Conversion Dictionary
    length_conversion = {
        "meters": 1,
        "kilometers": 1000,
        "feet": 0.3048,
        "inches": 0.0254,
        "centimeters": 0.01
    }

    # Conversion Logic
    if st.button("Convert"):
        result = input_value * (length_conversion[from_unit] / length_conversion[to_unit])
        st.success(f"{input_value} {from_unit} is equal to {result:.2f} {to_unit}")

# Weight Conversion
elif conversion_choice == "Weight":
    weight_units = ["kilograms", "pounds", "ounces", "grams", "milligrams"]
    
    input_value = st.number_input("Enter weight value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("Choose from unit", weight_units)
    to_unit = st.selectbox("Choose to unit", weight_units)

    # Weight Conversion Dictionary
    weight_conversion = {
        "kilograms": 1,
        "pounds": 0.453592,
        "ounces": 0.0283495,
        "grams": 0.001,
        "milligrams": 0.000001
    }

    # Conversion Logic
    if st.button("Convert"):
        result = input_value * (weight_conversion[from_unit] / weight_conversion[to_unit])
        st.success(f"{input_value} {from_unit} is equal to {result:.2f} {to_unit}")

# Temperature Conversion
elif conversion_choice == "Temperature":
    temp_units = ["Celsius", "Fahrenheit", "Kelvin"]

    input_value = st.number_input("Enter temperature value:", min_value=-273.15, format="%.2f")
    from_unit = st.selectbox("Choose from unit", temp_units)
    to_unit = st.selectbox("Choose to unit", temp_units)

    # Temperature Conversion Function
    def convert_temperature(value, from_unit, to_unit):
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return value * 9/5 + 32
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        else:
            return value  # If same units, return the same value

    # Conversion Logic
    if st.button("Convert"):
        result = convert_temperature(input_value, from_unit, to_unit)
        st.success(f"{input_value} {from_unit} is equal to {result:.2f} {to_unit}")
