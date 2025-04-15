# Gastritis Risk Prediction Tool

## Overview

The **Gastritis Risk Prediction Tool** is a web-based application built using **Flask** and **Machine Learning** techniques to predict the likelihood of an individual developing gastritis. The tool gathers user input through a Google Form, processes the data, and provides predictions based on lifestyle and health information. The app uses a trained machine learning model to estimate the gastritis risk and suggest further actions.

## Features

- **Data Collection**: Gathers real-life health data via a **Google Form**.
- **Prediction Model**: Utilizes a **machine learning model** to assess gastritis risk based on user input.
- **Flask Web App**: A user-friendly interface that guides users through the input process.
- **Risk Prediction**: Provides personalized gastritis risk probabilities and health advice.
- **Treatment Suggestions**: Integrates web scraping from trusted medical websites to suggest treatments.

## Tech Stack

- **Backend**: Python, Flask
- **Machine Learning**: scikit-learn, Joblib (for saving and loading models)
- **Frontend**: HTML, CSS, JavaScript
- **Data Collection**: Google Forms
- **Web Scraping**: BeautifulSoup (for fetching treatment suggestions)

## Setup and Installation

### Prerequisites

Before running the project, ensure that you have the following software installed:

- Python 3.x
- pip (Python package manager)

### Installing Dependencies

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/gastritis-risk-prediction.git
    cd gastritis-risk-prediction
    ```

2. Install the required Python libraries:

    ```bash
    pip install -r requirements.txt
    ```

    Make sure the `requirements.txt` includes the following dependencies:

    ```
    Flask==2.0.3
    joblib==1.1.0
    scikit-learn==0.24.2
    numpy==1.21.2
    pandas==1.3.3
    beautifulsoup4==4.10.0
    requests==2.26.0
    ```

### Running the App

To run the application locally:

1. Navigate to the project folder and start the Flask app:

    ```bash
    python app.py
    ```

2. Open your browser and go to `http://127.0.0.1:5000/` to view the app.

### Using the App

1. **Fill out the Google Form** to provide health and lifestyle data.
2. The Flask app will prompt you with questions based on your data.
3. After completing the form, the app will predict your gastritis risk and provide recommendations.
4. Optionally, you can download the result for future reference.

## How the Model Works

The model was trained using a dataset containing real-world health data (e.g., dietary habits, stress levels, age, etc.). It predicts the probability of gastritis risk based on the user’s responses.

1. **Data Preprocessing**: Input data is cleaned and transformed for model compatibility.
2. **Model**: A **Random Forest Classifier** (or any other model you've chosen) is used for classification.
3. **Prediction**: Once the user fills out the form, the data is passed to the model for prediction.
4. **Results**: The model returns a risk probability (e.g., low, medium, high).

## Web Scraping for Treatment Suggestions

Once the prediction is made, the app scrapes trusted medical websites for **treatment suggestions** based on the user’s risk level.

## Contributing

Feel free to fork this project and submit pull requests. Any contributions are welcome, whether it's bug fixes, new features, or improving the documentation.

To contribute:

1. Fork the repo.
2. Create a new branch (`git checkout -b feature-name`).
3. Make changes and commit (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- The model training is based on scikit-learn and other machine learning libraries.
- Web scraping for treatment suggestions uses **BeautifulSoup** and **requests** libraries.

