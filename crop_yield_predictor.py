import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor

class CropYieldPredictor:
    def __init__(self):
        self.pipeline = None
        self.categorical_columns = [
            'State', 'Crop_Type', 'Season', 'Fertilizer_Type',
            'Irrigation_Type', 'Seed_Variety'
        ]
        self.numerical_columns = [
            'Year', 'Area_Planted_Hectares', 'Avg_Temperature_C', 'Total_Rainfall_mm',
            'Humidity_Percent', 'Soil_pH', 'Nitrogen_Content_ppm',
            'Phosphorus_Content_ppm', 'Potassium_Content_ppm',
            'Organic_Matter_Percent', 'Soil_Quality_Score',
            'Fertilizer_Used_kg_per_hectare', 'Pesticide_Used_kg_per_hectare',
            'Irrigation_Frequency_per_month'
        ]

    def run_pipeline(self, dataset_path):
        # Load dataset
        data = pd.read_csv(dataset_path)
        
        # Features and target
        X = data[self.categorical_columns + self.numerical_columns]
        y = data['Yield_per_Hectare_tons']
        
        # Preprocessing
        preprocessor = ColumnTransformer(
            transformers=[
                ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), self.categorical_columns),
                ('num', StandardScaler(), self.numerical_columns)
            ])
        
        # Create pipeline
        self.pipeline = Pipeline([
            ('preprocessor', preprocessor),
            ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
        ])
        
        # Split data and train
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.pipeline.fit(X_train, y_train)
        
        # Optional: Evaluate model
        score = self.pipeline.score(X_test, y_test)
        print(f"Model R^2 Score: {score:.4f}")

    def predict_yield(self, input_data):
        if self.pipeline is None:
            raise ValueError("Pipeline not trained. Call run_pipeline first.")
        
        try:
            # Convert input_data to DataFrame if it's a dict
            if isinstance(input_data, dict):
                input_data = pd.DataFrame([input_data])
            
            # Ensure all required columns are present
            for col in self.categorical_columns + self.numerical_columns:
                if col not in input_data.columns:
                    raise ValueError(f"Missing column: {col}")
            
            # Make prediction
            prediction = self.pipeline.predict(input_data)
            return prediction
        except Exception as e:
            print(f"Prediction error: {str(e)}")
            return None