import joblib
import pandas as pd
import streamlit as st

# Load the trained model pipeline (Ensure the pipeline file is in the same directory)
model_pipeline = joblib.load('ipl_model_pipeline.pkl')

# Function to predict the winning bid and player name
def predict_winning_bid(player_name, base_price, bid_to_base_ratio, team_name):
    input_data = {
        'Base Price': base_price,
        'Bid-to-Base Ratio': bid_to_base_ratio,
        'team_name': team_name
    }
    
    # Convert to DataFrame
    input_df = pd.DataFrame([input_data])

    # Make the prediction using the model pipeline (includes preprocessing)
    prediction = model_pipeline.predict(input_df)
    return player_name, prediction[0]

# Streamlit app UI
st.title("IPL Winning Bid Prediction")

# Input fields for prediction
player_name = st.text_input('Player Name', 'Rahul Tripathi')  # Default player name
base_price = st.number_input('Base Price (in INR)', min_value=3000000, max_value=200000000, value=3000000)
bid_to_base_ratio = st.number_input('Bid-to-Base Ratio', min_value=0.0, max_value=10.0, value=1.0)
team_name = st.selectbox("Select Player's Team", ['DC', 'GT', 'KKR', 'LSG', 'MI', 'PBKS', 'RCB', 'RR', 'SRH'])

# Button to trigger prediction
if st.button('Predict Winning Bid'):
    try:
        # Call the function and get player name along with predicted bid
        player_name, predicted_bid = predict_winning_bid(player_name, base_price, bid_to_base_ratio, team_name)
        
        # Display the prediction
        st.write(f"The predicted winning bid for {player_name} is INR {predicted_bid:,.2f}")
    except Exception as e:
        st.error(f"Error: {str(e)}")
