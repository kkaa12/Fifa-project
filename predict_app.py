import streamlit as st
import pandas as pd
import joblib

# Load the trained model (Ensure the model path is correct)
model = joblib.load('random_forest_model.joblib')

# Streamlit page configuration
st.title('FIFA Player Overall Rating Predictor')
st.write("This app predicts the FIFA overall rating based on comprehensive player attributes.")

# Input fields for the prediction
age = st.number_input('Age', min_value=16, max_value=40, value=25, step=1)
movement_reactions = st.slider('Movement Reactions', min_value=0, max_value=100, value=50)
value_eur = st.number_input('Market Value (€)', min_value=0, value=1000000, step=10000)
wage_eur = st.number_input('Wage (€)', min_value=0, value=10000, step=500)
mentality_composure = st.slider('Mentality Composure', min_value=0, max_value=100, value=50)
potential = st.slider('Potential', min_value=0, max_value=100, value=75)
pace = st.slider('Pace', min_value=0, max_value=100, value=60)
shooting = st.slider('Shooting', min_value=0, max_value=100, value=60)
passing = st.slider('Passing', min_value=0, max_value=100, value=60)
dribbling = st.slider('Dribbling', min_value=0, max_value=100, value=60)
defending = st.slider('Defending', min_value=0, max_value=100, value=60)
physic = st.slider('Physic', min_value=0, max_value=100, value=60)

# Button to make prediction
if st.button('Predict Overall Rating'):
    # Prepare the input data
    input_data = pd.DataFrame({
        'age': [age],
        'movement_reactions': [movement_reactions],
        'value_eur': [value_eur],
        'wage_eur': [wage_eur],
        'mentality_composure': [mentality_composure],
        'potential': [potential],
        'pace': [pace],
        'shooting': [shooting],
        'passing': [passing],
        'dribbling': [dribbling],
        'defending': [defending],
        'physic': [physic]
    })

    # Make prediction
    prediction = model.predict(input_data)
    st.write(f'Predicted Overall Rating: {prediction[0]:.2f}')

# Optional: Information or instructions
st.sidebar.write("Instructions")
st.sidebar.write("Adjust the sliders and inputs to match the player attributes and click 'Predict Overall Rating' to see the predicted FIFA overall rating.")
