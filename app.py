import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Judul aplikasi
st.title("Student Dropout Prediction")

st.write(
    "This prototype predicts whether a student is at risk of dropping out "
    "based on several academic and financial factors."
)

# Input dari user
age = st.number_input(
    "Age at Enrollment",
    min_value=15,
    max_value=70,
    value=18
)

admission_grade = st.number_input(
    "Admission Grade",
    min_value=0.0,
    max_value=200.0,
    value=120.0
)

scholarship = st.selectbox(
    "Scholarship Holder",
    ["No", "Yes"]
)

tuition = st.selectbox(
    "Tuition Fees Up To Date",
    ["No", "Yes"]
)

# Konversi ke angka
scholarship = 1 if scholarship == "Yes" else 0
tuition = 1 if tuition == "Yes" else 0


# Tombol prediksi
if st.button("Predict"):

    # Membuat input array sesuai model
    input_data = np.array([[age, admission_grade, scholarship, tuition]])

    # Prediksi
    prediction = model.predict(input_data)

    # Output hasil
    if prediction[0] == 1:
        st.error("⚠️ Student at Risk of Dropout")
    else:
        st.success("✅ Student Not Likely to Dropout")