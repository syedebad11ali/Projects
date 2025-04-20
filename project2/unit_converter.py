import streamlit as st
st.title("Unit Convertor")
if "lenght" not in st.session_state:
    st.session_state.lenght=[]
if "weight" not in st.session_state:
    st.session_state.lenght=[]
st.header("Unit Convertor For Length And Weight")
lenght= {
    "meter": 1,
    "kilometer": 1000,
    "centimeter": 0.01,
    "millimeter": 0.001}
def length_converter(value, from_unit, to_unit):
    # Convert the input value from the 'from_unit' to meters, then from meters to the 'to_unit'
    base_value = value * lenght[from_unit]
    converted_value = base_value / lenght[to_unit]
    return converted_value

# Length conversion section
st.subheader("Length Conversion")
value = st.number_input("Enter value", value=1.0)
from_unit = st.selectbox("Convert from", list(lenght.keys()))
to_unit = st.selectbox("Convert to", list(lenght.keys()))

if st.button("Convert Length"):
    result = length_converter(value, from_unit, to_unit)
    st.success(f"{value} {from_unit} equals {result} {to_unit}")
    # st.divider()
# temprature={
#     ""
#     ""
#     ""

#     }

weight={
    "kilogram": 1,
    "gram": 0.001,       
    "pound": 0.453592,   
    "ounce": 0.0283495
    }
def weight_converter(val, from_unit1, to_unit1):
    # Convert the input value from the 'from_unit' to meters, then from meters to the 'to_unit'
    base_val = val * weight[from_unit1]
    converted_val = base_val / weight[to_unit1]
    return converted_val

# Length conversion section
st.subheader("Weight Conversion")
weight_value = st.number_input("Enter value for weight conversion", value=1.0, key="weight_value")
from_unit1 = st.selectbox("Convert from (weight)", list(weight.keys()), key="weight_from")
to_unit1 = st.selectbox("Convert to (weight)", list(weight.keys()), key="weight_to")

if st.button("Convert Weight"):
    result1 = weight_converter(weight_value, from_unit1, to_unit1)
    st.success(f"{weight_value} {from_unit1} equals {result1} {to_unit1}")
