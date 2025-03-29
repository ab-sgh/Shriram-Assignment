from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))
le = pickle.load(open('encoder.pkl', 'rb'))

expected_columns = [
    'Size_sqft', 'Location', 'Bedrooms', 'House_Age', 'Bathrooms', 'Garage', 'Pool', 'Distance_to_City_Center_miles'
]

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        input_df = pd.DataFrame({
            'Size_sqft': [float(data['Size_sqft'])],
            'Location': [data['Location']],
            'Bedrooms': [int(data['Bedrooms'])],
            'House_Age': [int(data['House_Age'])],
            'Bathrooms': [int(data['Bathrooms'])],
            'Garage': [int(data['Garage'])],
            'Pool': [int(data['Pool'])],
            'Distance_to_City_Center_miles': [float(data['Distance_to_City_Center_miles'])],
        })

        location = data['Location']
        if location in le.classes_:
            input_df['Location'] = le.transform([location])
        else:
            return jsonify({
                'status': 'error',
                'message': f'Available locations are: {list(le.classes_)}'
            }), 400

        # Ensure the order of columns matches the training set
        input_df = input_df[expected_columns]

        input_standardized = scaler.transform(input_df)

        prediction = model.predict(input_standardized)[0]

        return jsonify({
            'status': 'success',
            'predicted_price': float(prediction),
            'message': 'Prediction successful'
        })

    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/', methods=['GET'])
def home():
    return """
    <h1>House Price Prediction API</h1>
    <p>Send POST requests to /predict with the following JSON structure:</p>
    <pre>
    {
        "Size_sqft": 2500,
        "Location": "",  # Enter a valid Location
        "Bedrooms": 3,
        "House_Age": 15,
        "Bathrooms": 2,
        "Garage": 1,
        "Pool": 0,
        "Distance_to_City_Center_miles": 5.2
    }
    </pre>
    """

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
