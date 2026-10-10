import streamlit as st
import numpy as np
import joblib
import pandas as pd
import os

# set page title and icon
st.set_page_config(
    page_title="Smart Crop Recommendation",
    page_icon="🌱",
    layout="wide"
)

# Model loading with caching
@st.cache_resource
def load_model():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    model_path = os.path.join(BASE_DIR, "models", "crop_rf_model.pkl")
    encoder_path = os.path.join(BASE_DIR, "models", "label_encoder.pkl")

    model = joblib.load(model_path)
    encoder = joblib.load(encoder_path)
    return model, encoder

model, label_encoder = load_model()

# # header and description
st.title("🌱 Smart Crop Recommendation System")
st.markdown(
    """
    This intelligent system recommends the **best crops** based on
    soil nutrients and environmental conditions using a **Random Forest ML model**.
    """
)

st.divider()

# ------------------- SIDEBAR -------------------
st.sidebar.header("⚙️ Input Parameters")

N = st.sidebar.slider("Nitrogen (N)", 0, 200, 50)
P = st.sidebar.slider("Phosphorus (P)", 0, 200, 50)
K = st.sidebar.slider("Potassium (K)", 0, 210, 50)

temperature = st.sidebar.slider("Temperature (°C)", 0.0, 60.0, 25.0)
humidity = st.sidebar.slider("Humidity (%)", 0.0, 100.0, 70.0)
ph = st.sidebar.slider("Soil pH", 3.5, 10.0, 6.5)
rainfall = st.sidebar.slider("Rainfall (mm)", 0.0, 500.0, 150.0)

FEATURE_NAMES = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]
input_data = pd.DataFrame(
    [[N, P, K, temperature, humidity, ph, rainfall]],
    columns=FEATURE_NAMES
)

# ------------------- MAIN ACTION -------------------
def run_prediction():
    probabilities = model.predict_proba(input_data)[0]
    classes = label_encoder.inverse_transform(model.classes_)
    results = pd.DataFrame({
        "Crop": classes,
        "Probability (%)": np.round(probabilities * 100, 2)
    }).sort_values(by="Probability (%)", ascending=False)
    best_crop = results.iloc[0]["Crop"]
    feature_names = [
        "Nitrogen", "Phosphorus", "Potassium",
        "Temperature", "Humidity", "pH", "Rainfall"
    ]
    importance_df = pd.DataFrame({
        "Feature": feature_names,
        "Importance": model.feature_importances_
    }).sort_values(by="Importance", ascending=False)
    st.session_state["results"] = results
    st.session_state["best_crop"] = best_crop
    st.session_state["importance_df"] = importance_df

# Run prediction on first load (default values)
if "results" not in st.session_state:
    run_prediction()

if st.sidebar.button("🌾 Predict Crop"):
    run_prediction()

# Show results if available
if "results" in st.session_state:
    results = st.session_state["results"]
    best_crop = st.session_state["best_crop"]
    importance_df = st.session_state["importance_df"]
    col1, col2 = st.columns([2, 3])
    with col1:
        st.subheader("✅ Best Recommended Crop")
        st.success(f"🌾 **{best_crop.upper()}**")
        st.markdown("### 🌱 Top 3 Crop Recommendations")
        st.table(results.head(3).reset_index(drop=True))
    with col2:
        st.subheader("📊 Prediction Confidence")
        st.bar_chart(results.set_index("Crop").head(5))
    st.divider()
    st.subheader("🔍 Feature Importance (Random Forest)")
    st.bar_chart(importance_df.set_index("Feature"))

# ------------------- FOOTER -------------------
st.markdown("---")
st.markdown(
    "🚀 **Built with Streamlit & Random Forest ML**  \n"
    "📈 Accurate | 🌍 Smart | 🌱 Sustainable Agriculture"
)
