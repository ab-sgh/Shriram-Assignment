
# Predicting Housing Prices using Structured Dataset

'Model.ipynb' contains the code for prediction the housing prices using the dataset.

# Deploy the model

In 'app.py' Flask has been used to  create an API that accepts user inputs and returns predictions.

## Instructions for running the API are as follows:

- Create a virtual environment
  - python -m venv venv

- Activate the virtual environment
  - On Windows: venv\Scripts\activate
  - On macOS/Linux: source venv/bin/activate

- run 'pip install -r requirements.txt'

- Start the flask server

  - run 'python app.py'

- Test the API

  - run 'python test_api.py'
