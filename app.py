
from flask import Flask, render_template, request
from utilities.model import load_model
from utilities.feature_extractor import extract_features

app = Flask(__name__)

model = load_model()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    url = request.form['url']

    features = [extract_features(url)]

    prediction = model.predict(features)[0]

    result = "Phishing Website" if prediction == 1 else "Legitimate Website"

    return render_template(
        'result.html',
        url=url,
        prediction=result
    )

if __name__ == '__main__':
    app.run(debug=True)
