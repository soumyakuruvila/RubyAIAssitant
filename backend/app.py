from flask import Flask, request
from flask_cors import CORS
import pandas as pd
from email_generator import generate_emails
import json


app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    data = pd.read_csv(file,encoding='latin-1')
    data = data.to_json(orient = "records") 

    onboarding_data = json.load(open('onboarding.json'))
    result = generate_emails(onboarding_data, data)
    
    return json.dumps(result)

@app.route('/onboardingSubmit', methods=['POST'])
def onboarding_submit():
    onboarding_data = request.get_json()

    with open('onboarding.json', 'w') as f:
        json.dump(onboarding_data, f)

    return onboarding_data

if __name__ == '__main__':
    app.run()