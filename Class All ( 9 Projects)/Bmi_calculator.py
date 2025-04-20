import streamlit as st

class BmiCalculator:
    def __init__(self, weight, height_cm):
        self.weight = weight
        self.height_cm = height_cm

    def calculate_bmi(self):
        height_m = self.height_cm / 100
        bmi = self.weight / (height_m ** 2)
        return round(bmi, 2)

    def interpret_bmi(self, bmi):
        if bmi < 18.5:
            return "Underweight "
        elif 18.5 <= bmi < 24.9:
            return "Normal weight "
        elif 25 <= bmi < 29.9:
            return "Overweight "
        else:
            return "Obese "

# Streamlit UI
st.set_page_config(page_title="BMI Calculator", page_icon="")
st.title(" BMI Calculator")

st.write("Enter your weight and height to calculate your Body Mass Index (BMI).")
try:
    weight = st.number_input("Weight (kg):", min_value=1.0, max_value=300,step=0.5)
    height = st.number_input("Height (cm):", min_value=50.0, max_value=250,step=0.5)
except (ValueError,IndexError) as e:
    st.warning(f"Error:{e}")
if st.button("Calculate"):
    bmi_calc = BmiCalculator(weight, height)
    bmi = bmi_calc.calculate_bmi()
    category = bmi_calc.interpret_bmi(bmi)

    st.success(f"Your BMI is: **{bmi}**")
    st.info(f"Category: **{category}**")
