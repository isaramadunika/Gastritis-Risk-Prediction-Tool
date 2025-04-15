from flask import Flask, render_template, request, redirect, url_for
import os
import joblib
import pandas as pd

# Import our prediction module
from model.predict import predict_gastritis_probability

app = Flask(__name__)

# Check if model exists, if not, train it
model_path = 'model/gastritis_model.pkl'
if not os.path.exists(model_path):
    print("Training new model...")
    from model.train_model import train_and_save_model
    train_and_save_model()

# Load the trained model
model = joblib.load(model_path)

@app.route('/')
def index():
    """Render the home page with the input form"""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Process the form and make a prediction"""
    if request.method == 'POST':
        # Get form data
        user_data = {
            'Age Group ': request.form.get('age_group'),
            'Gender  ': request.form.get('gender'),
            'University Student': 1 if request.form.get('university_student') == 'yes' else 0,
            'Meals per day': request.form.get('meals_per_day'),
            'Spicy/Oily Food Consumption': 1 if request.form.get('spicy_food') == 'yes' else 0,
            'Caffeinated Drinks': 1 if request.form.get('caffeinated_drinks') == 'yes' else 0,
            'Alcohol': 1 if request.form.get('alcohol') == 'yes' else 0,
            'Stress (Yes/No)': 1 if request.form.get('stress') == 'yes' else 0,
            'Stress Level (1–5)': int(request.form.get('stress_level')),
            'Sleep Hours': request.form.get('sleep_hours'),
            'Exercise': 1 if request.form.get('exercise') == 'yes' else 0,
            'Dieting': 1 if request.form.get('dieting') == 'yes' else 0,
            'Instant Food Frequency': request.form.get('instant_food'),
            'Snacks between Meals': request.form.get('snacks')
        }
        
        # Make prediction
        result = predict_gastritis_probability(model, user_data)
        
        # Return result
        return render_template('result.html', 
                              prediction=result['prediction'],
                              probability=result['probability'],
                              user_data=user_data)
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)