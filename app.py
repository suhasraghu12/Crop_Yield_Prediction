import pandas as pd
from flask import Flask, request, jsonify, render_template
from crop_yield_predictor import CropYieldPredictor

app = Flask(__name__)
predictor = CropYieldPredictor()

# Load and train the model
predictor.run_pipeline('indian_agricultural_dataset.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        input_df = pd.DataFrame([data])
        prediction = predictor.predict_yield(input_df)
        if prediction is not None:
            return jsonify({'prediction': float(prediction[0])})
        return jsonify({'error': 'Prediction failed'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)