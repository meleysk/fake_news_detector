# Serve model as a flask application
from fake_news.pre_processing import normalize_corpus
import pickle
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify

model = None
cv = None
app = Flask(__name__)


def load_model():
    global model
    global cv

    # model variable refers to the global variable
    with open('svm_trained_model.pkl', 'rb') as f:
        model = pickle.load(f)

    with open('vectorizer.pkl', 'rb') as f:
        cv = pickle.load(f)


@app.route('/')
def home_endpoint():
    return 'Fake news detector'


@app.route('/predict', methods=['POST'])
def get_prediction():
    global model
    global cv
    # Works only for a single sample
    if request.method == 'POST':
        data = request.get_json()  # Get data

        if type(data) == dict:
            df = pd.DataFrame(data)
            # Drop possible null values
            df.dropna(inplace=True)
        else:
            df = data

        # Normalize data
        df_clean = normalize_corpus(df)

        # Vectorize
        cv_df = cv.transform(df_clean)

        # Predict
        prediction = model.predict(cv_df)

        response = {
            'predictions': list(prediction)
        }
    return jsonify(response)


if __name__ == '__main__':

    load_model()  # load model once
    app.run(host='0.0.0.0', port=8080)
