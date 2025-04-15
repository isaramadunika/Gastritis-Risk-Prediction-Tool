import pandas as pd
import numpy as np
import os
import joblib

def predict_gastritis_probability(model, user_data):
    """
    Predict whether a person has gastritis based on their inputs.
    
    Parameters:
    model: Trained model
    user_data (dict): Dictionary containing user inputs for prediction
    
    Returns:
    dict: {'prediction': 'Yes'/'No', 'probability': float}
    """
    # Convert input to DataFrame
    user_df = pd.DataFrame([user_data])
    
    # Make prediction
    try:
        # Get probability of class 1 (Gastritis = Yes)
        pred_proba = model.predict_proba(user_df)[0][1]
        prediction = 'Yes' if pred_proba >= 0.5 else 'No'
        
        return {
            'prediction': prediction,
            'probability': round(pred_proba * 100, 2)  # Convert to percentage
        }
    except Exception as e:
        print(f"Error making prediction: {e}")
        return {
            'prediction': 'Error',
            'probability': 0
        }

def load_model():
    """Load the trained model if it exists, or train a new one"""
    model_path = 'model/gastritis_model.pkl'
    
    if os.path.exists(model_path):
        return joblib.load(model_path)
    else:
        # Train a new model if one doesn't exist
        from train_model import train_and_save_model
        return train_and_save_model()