import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained model and feature columns
with open('used_car_price_model.pkl', 'rb') as f:
    model, feature_columns = pickle.load(f)

# Define feature options (replace these with actual unique values from your data)
companies = [
    'MARUTI SUZUKI', 'HYUNDAI', 'TATA', 'FORD', 'MERCEDES BENZ', 'VOLKSWAGEN',
    'MAHINDRA', 'HONDA', 'RENAULT', 'NISSAN', 'JEEP', 'FIAT', 'TOYOTA', 'KIA',
    'BMW', 'DATSUN', 'SKODA', 'MG', 'AUDI', 'ISUZU', 'VOLVO', 'MITSUBISHI', 'CHEVROLET'
]

# Mapping of companies to their models (example, replace with actual data)
company_models = {
    'MARUTI SUZUKI': ['SWIFT', 'BALENO', 'ALTO', 'DZIRE', 'ERTIGA'],
    'HYUNDAI': ['i20', 'i10', 'CRETA', 'VERNA', 'SANTRO'],
    'TATA': ['NEXON', 'ALTROZ', 'TIAGO', 'HARRIER'],
    'FORD': ['ECOSPORT', 'FIGO', 'ENDEAVOUR'],
    'MERCEDES BENZ': ['C CLASS', 'E CLASS', 'GLA'],
    'VOLKSWAGEN': ['POLO', 'VENTO', 'AMAROK'],
    'MAHINDRA': ['SCORPIO', 'XUV500', 'BOLERO'],
    'HONDA': ['CITY', 'AMAZE', 'JAZZ'],
    'RENAULT': ['KWID', 'DUSTER', 'TRIBER'],
    'NISSAN': ['MICRA', 'SUNNY', 'TERRANO'],
    'JEEP': ['COMPASS', 'WRANGLER'],
    'FIAT': ['PUNTO', 'LINEA'],
    'TOYOTA': ['INNOVA', 'FORTUNER', 'ETIOS'],
    'KIA': ['SELTOS', 'SONET'],
    'BMW': ['3 SERIES', '5 SERIES'],
    'DATSUN': ['GO', 'REDI-GO'],
    'SKODA': ['OCTAVIA', 'SUPERB'],
    'MG': ['HECTOR', 'ZS EV'],
    'AUDI': ['A4', 'Q5'],
    'ISUZU': ['D-MAX'],
    'VOLVO': ['XC40', 'XC60'],
    'MITSUBISHI': ['PAJERO'],
    'CHEVROLET': ['BEAT', 'CRUZE']
}

fuel_types = ['PETROL', 'DIESEL', 'CNG', 'HYBRID', 'LPG']
transmissions = ['Manual', 'Automatic']
owners = ['1', '2', '3', '4 or more']

# Add a logo or image (optional)
# st.image("logo.png", width=120)

# Inject Google Fonts and custom CSS
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap" rel="stylesheet">
    <style>
        html, body, p, span, [class*="css"]  {
            font-family: 'Inter', sans-serif !important;
        }
        h1, h2, h3, h4, h5, h6 {
            font-family: 'Inter', sans-serif !important;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #2E86C1; font-size: 1.8em;'>🚗 Used Car Price Prediction</h1>", unsafe_allow_html=True)
st.markdown("---")

# Use columns for a cleaner input layout
col1, col2 = st.columns(2)

with col1:
    company = st.selectbox("Select Company", companies, help="Choose the car manufacturer.")
    models = company_models.get(company, [])
    model_name = st.selectbox("Select Model", models, help="Choose the car model.") if models else st.text_input("Enter Model Name", help="Type the model if not listed.")
    fuel_type = st.selectbox("Select Fuel Type", fuel_types, help="Type of fuel used by the car.")
    transmission = st.selectbox("Select Transmission Type", transmissions, help="Manual or Automatic transmission.")

with col2:
    model_year = st.number_input("Enter Model Year", min_value=1995, max_value=2025, step=1, value=2018, help="Year the car model was manufactured.")
    kilometer = st.number_input("Kilometers Driven", min_value=0, max_value=500000, step=100, value=30000, help="Total kilometers driven.")
    owner = st.selectbox("Number of Previous Owners", owners, help="How many previous owners?")

# If model expects owner as integer, convert accordingly
owner_map = {'1': 1, '2': 2, '3': 3, '4 or more': 4}
owner_num = owner_map[owner]

# --- Data Preparation for Prediction ---
input_dict = {
    'Company': company,
    'Model': model_name,
    'FuelType': fuel_type,
    'TransmissionType': transmission,
    'ModelYear': model_year,
    'Kilometer': kilometer,
    'Owner': owner_num,
}
input_df = pd.DataFrame([input_dict])

# Align input_df with training features (handle one-hot encoding)
for col in feature_columns:
    if col not in input_df.columns:
        input_df[col] = 0
input_df = input_df[feature_columns]

# Add a horizontal line before the prediction button
st.markdown("---")

if st.button("Predict Price"):
    price_pred = model.predict(input_df)[0]
    st.markdown(
        f"<div style='background-color:#006400;padding:20px;border-radius:10px;text-align:center;'>"
        f"<h2>Estimated Price &nbsp;  <span style='font-size:1em;color:#a1e637; font-weight:500'>₹ {price_pred:,.2f} lakhs</span></h2>" 
        f"</div>",
        unsafe_allow_html=True
    )

# Optional: Add a sidebar for info or instructions
st.sidebar.header("About")
st.sidebar.info(
    "This app predicts the price of a used car based on your inputs. "
    "Select the relevant details and click 'Predict Price' to see the estimated value."
)