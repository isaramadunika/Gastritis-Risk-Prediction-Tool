import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

def train_and_save_model():
    """Train the gastritis prediction model and save it to disk"""
    
    # Create model directory if it doesn't exist
    os.makedirs('model', exist_ok=True)
    
    # Load the data
    print("Loading data...")
    df = pd.read_csv('data/Gastric_Data.csv')
    
    # Data preprocessing
    print("Preprocessing data...")
    
    # For simplicity, we'll drop rows with missing values in target variable
    df = df.dropna(subset=['Gastritis (Yes/No)'])
    
    # Convert target variable to binary (0 for No, 1 for Yes)
    df['Gastritis_Binary'] = df['Gastritis (Yes/No)'].map({'Yes': 1, 'No': 0})
    
    # Select features
    features = [
        'Age Group ', 'Gender  ', 'University Student', 'Meals per day',
        'Spicy/Oily Food Consumption', 'Caffeinated Drinks', 'Alcohol',
        'Stress (Yes/No)', 'Stress Level (1–5)', 'Sleep Hours', 'Exercise',
        'Dieting', 'Instant Food Frequency', 'Snacks between Meals'
    ]
    
    # Convert categorical Yes/No features to binary
    binary_features = [
        'University Student', 'Spicy/Oily Food Consumption', 'Caffeinated Drinks',
        'Alcohol', 'Stress (Yes/No)', 'Exercise', 'Dieting'
    ]
    
    for col in binary_features:
        df[col] = df[col].map({'Yes': 1, 'No': 0})
        # If any NO appears as uppercase, also convert it
        df[col] = df[col].replace('NO', 0)
        # For any remaining non-numeric values, convert to NaN and then to 0
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
    
    # Convert 'Stress Level (1–5)' to numeric if it's not already
    df['Stress Level (1–5)'] = pd.to_numeric(df['Stress Level (1–5)'], errors='coerce')
    
    # Prepare X and y
    X = df[features]
    y = df['Gastritis_Binary']
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
    
    # Create preprocessor for numerical and categorical features
    numerical_features = [
        'Stress Level (1–5)'
    ] + binary_features
    
    categorical_features = [
        'Age Group ', 'Gender  ', 'Meals per day', 'Sleep Hours',
        'Instant Food Frequency', 'Snacks between Meals'
    ]
    
    # Define preprocessing steps
    numerical_transformer = SimpleImputer(strategy='median')
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])
    
    # Create column transformer
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numerical_transformer, numerical_features),
            ('cat', categorical_transformer, categorical_features)
        ])
    
    # Create and train the model
    print("Training model...")
    model = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
    ])
    
    model.fit(X_train, y_train)
    
    # Evaluate the model
    y_pred = model.predict(X_test)
    accuracy = (y_pred == y_test).mean()
    print(f"Model accuracy: {accuracy:.2f}")
    
    # Save the model
    print("Saving model...")
    joblib.dump(model, 'model/gastritis_model.pkl')
    
    print("Model training complete!")
    
    return model

if __name__ == "__main__":
    train_and_save_model()