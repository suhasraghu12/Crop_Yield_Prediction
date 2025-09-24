# Crop Yield Prediction Project

## Overview
This project provides a web-based application for predicting crop yields based on agricultural data from the `indian_agricultural_dataset.csv`. The application uses a machine learning pipeline to process input features (e.g., state, crop type, soil conditions, weather data) and predict yield per hectare. The frontend is built with HTML and Tailwind CSS, while the backend uses Flask and a custom `CropYieldPredictor` class implemented in Python with scikit-learn.

### Features
- **User Interface**: A web form with dropdowns for categorical features (State, Crop Type, Season, etc.) and input fields for numerical features (e.g., Area Planted, Soil pH).
- **Machine Learning Pipeline**: Preprocesses data using `OneHotEncoder` for categorical variables and `StandardScaler` for numerical variables, then predicts yields using a RandomForestRegressor.
- **API Integration**: A Flask backend serves the web interface and handles prediction requests via a `/predict` endpoint.
- **Responsive Design**: Styled with Tailwind CSS for a clean, user-friendly experience.

## Project Structure
```
crop-yield-prediction/
├── templates/
│   └── index.html           # Web interface with form for input
├── crop_yield_prediction.py # Machine learning pipeline (CropYieldPredictor class)
├── app.py                  # Flask application for serving UI and API
├── indian_agricultural_dataset.csv  # Dataset for training the model
└── README.md               # Project documentation
```

## Prerequisites
- **Python 3.8+**
- **Dependencies**:
  - Flask
  - Pandas
  - NumPy
  - scikit-learn
- **Web Browser**: For accessing the web interface
- **Dataset**: `indian_agricultural_dataset.csv` (must be in the project root)

## Setup Instructions
1. **Clone the Repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd crop-yield-prediction
   ```

2. **Install Dependencies**:
   Create a virtual environment and install required packages:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install flask pandas numpy scikit-learn
   ```

3. **Prepare the Dataset**:
   - Ensure `indian_agricultural_dataset.csv` is in the project root.
   - The dataset should include columns: `State`, `Crop_Type`, `Season`, `Fertilizer_Type`, `Irrigation_Type`, `Seed_Variety`, `Year`, `Area_Planted_Hectares`, `Avg_Temperature_C`, `Total_Rainfall_mm`, `Humidity_Percent`, `Soil_pH`, `Nitrogen_Content_ppm`, `Phosphorus_Content_ppm`, `Potassium_Content_ppm`, `Organic_Matter_Percent`, `Soil_Quality_Score`, `Fertilizer_Used_kg_per_hectare`, `Pesticide_Used_kg_per_hectare`, `Irrigation_Frequency_per_month`, and `Yield_per_Hectare_tons`.

4. **Run the Application**:
   Start the Flask server:
   ```bash
   python app.py
   ```
   The app will run at `http://localhost:5000`.

## Usage
1. **Access the Web Interface**:
   - Open `http://localhost:5000` in a web browser.
   - The interface displays a form with dropdowns for categorical features (e.g., State, Crop Type) and input fields for numerical features (e.g., Area Planted, Soil pH).

2. **Enter Data**:
   - Select values from dropdowns for categorical inputs (e.g., `State: Punjab`, `Crop_Type: Wheat`).
   - Enter numerical values (e.g., `Area Planted: 5.0 hectares`, `Soil pH: 7.0`).
   - All fields are required, with constraints (e.g., `Soil_pH` between 0 and 14).

3. **Predict Yield**:
   - Click the "Predict Yield" button.
   - The form sends data to the `/predict` endpoint, which returns the predicted yield per hectare.
   - The total yield (in tons) for the specified area is displayed below the form.

## Technical Details
- **Frontend**:
  - `templates/index.html`: Uses HTML, Tailwind CSS, and JavaScript to create a form and handle API requests.
  - Categorical features are populated with unique values from the dataset (e.g., States: Andhra Pradesh, Bihar, etc.).
  - JavaScript submits form data as JSON to `/predict` and displays results.

- **Backend**:
  - `app.py`: Flask app serving `index.html` and the `/predict` endpoint.
  - `/predict` accepts JSON input, passes it to `CropYieldPredictor`, and returns the prediction.

- **Machine Learning Pipeline**:
  - `crop_yield_prediction.py`: Defines the `CropYieldPredictor` class.
  - Preprocessing: `OneHotEncoder` for categorical features (with `handle_unknown='ignore'`) and `StandardScaler` for numerical features.
  - Model: RandomForestRegressor with 100 estimators.
  - Training: Uses `indian_agricultural_dataset.csv` with an 80/20 train-test split.
  - Prediction: Returns yield per hectare in tons.

## Troubleshooting
- **Dataset Issues**: Ensure `indian_agricultural_dataset.csv` is in the project root and matches the expected column structure.
- **Prediction Errors**: Check the browser console or server logs for errors (e.g., missing columns, invalid inputs). The pipeline validates input data and returns errors if columns are missing.
- **Model Performance**: The R² score is printed during training. If low, consider tuning the RandomForestRegressor (e.g., adjust `n_estimators`, `max_depth`) or adding feature engineering.
- **Server Issues**: Ensure Flask is running (`python app.py`) and accessible at `http://localhost:5000`.

## Future Enhancements
- Add client-side input validation (e.g., ensure `Soil_pH` is within 0–14).
- Implement a loading spinner during API calls.
- Add visualizations (e.g., predicted vs. actual yield charts).
- Support dynamic dropdowns (e.g., filter `Crop_Type` by `State` or `Season`).
- Persist the trained model using `joblib` to avoid retraining on startup.

## License
This project is for educational purposes and uses open-source libraries. Ensure compliance with the licenses of Flask, Pandas, NumPy, and scikit-learn.

## Contact
For questions or contributions, please contact [your contact information or repository maintainer].