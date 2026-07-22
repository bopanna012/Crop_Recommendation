# Crop Recommendation System

A machine learning–based **Crop Recommendation System** that suggests the most suitable crop based on soil nutrients and environmental conditions. The project is built using **Python**, **Scikit-learn**, and **Streamlit** with a clean, industry-standard project structure.


# Problem Statement

Farmers often struggle to decide which crop to grow based on soil and weather conditions. This project uses a **Random Forest classifier** to recommend the best crop by analyzing:

- Soil nutrients (N, P, K)
- Temperature
- Humidity
- Soil pH
- Rainfall


# Features

- ML-powered crop recommendation
- Trained Random Forest model
- Interactive Streamlit web app
- Clean & professional project structure


# Machine Learning Model

- **Algorithm**: Random Forest Classifier
- **Reason**:
  - Handles non-linear data well
  - Robust to overfitting
  - High accuracy for classification problems

The model is trained in the Jupyter Notebook and saved using `pickle`.


# Tech Stack

- **Python 3.10+**
- **Streamlit** – Frontend
- **Scikit-learn** – Machine Learning
- **Pandas & NumPy** – Data handling
- **Pickle** – Model serialization


# Project Structure

crop-recommendation/
│
├── app/
│ └── app.py
│
├── models/
│ ├── crop_rf_model.pkl
│ └── label_encoder.pkl
│
├── data/
│ └── Crop_recommendation.xlsx
│
├── notebooks/
│ └── Crop_recommendation.ipynb
│
├── powerbi/
│ └── Crop recommendation.pbix
│
├── requirements.txt
├── .gitignore
└── README.md


# Power BI Dashboard

The **Power BI report** provides interactive data analysis and visualization for the crop recommendation dataset.


# Insights Covered:

- Crop distribution across different conditions
- Soil nutrient trends (N, P, K)
- Rainfall, temperature, and humidity analysis


# How to Use:

1. Open the `.pbix` file from the `powerbi/` folder using **Power BI Desktop**
2. Connect to the dataset located in the `data/` folder if prompted
3. Refresh data to explore interactive dashboards


# Installation & Setup

# 1. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

# 2. Install dependencies

```bash
pip install -r requirements.txt
```

# 3. Run the Application

From the **project root directory**:
```bash
streamlit run app/app.py
```

The app will open in your browser


# Usage Guideline

- Crop Recommendation:
  - Input parameters:
    1. Nitrogen (N) - Soil nitrogen content
    2. Phosphorus (P) - Soil phosphorus content
    3. Potassium (K) - Soil potassium content
    4. Temperature - Ambient temperature (°C)
    5. Humidity - Relative humidity (%)
    6. pH - Soil pH value
    7. Rainfall - Rainfall in mm
    
    This system uses the above mentioned input parameter's content in your soil to receive personalized crop recommendations.

- Data Analysis:
  - Explore historical trends and insights through the provided dynamic charts.


# Output

- Displays the **recommended crop** based on input conditions


# Contributors of the project

1. Hency Babariya
2. Yashu Bopanna P D
3. Manoj Kumar
4. Mohan Krishna


# Acknowledgment: 
https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset