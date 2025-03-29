import requests
import json

# API endpoint URL
url = 'http://localhost:5000/predict'

# Sample input data
input_data = {
    "Size_sqft": 2500,
    "Location": "Houston", 
    "Bedrooms": 3,
    "House_Age": 15,
    "Bathrooms": 3,
    "Garage": 1,
    "Pool": 0,
    "Distance_to_City_Center_miles": 7.2
}

response = requests.post(
    url,
    headers={"Content-Type": "application/json"},
    data=json.dumps(input_data)
)

if response.status_code == 200:
    result = response.json()
    print(f"Prediction successful!")
    print(f"Predicted house price: {result['predicted_price']}")
else:
    print(f"Error: {response.text}")
