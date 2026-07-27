import streamlit as st
import pickle
import numpy as np

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

# -------------------------------
# Load Model
# -------------------------------
model = pickle.load(open("random_forest_churn_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# -------------------------------
# Custom CSS
# -------------------------------
st.markdown("""
<style>
.main{
    background-color:#f5f7fa;
}
.stButton>button{
    background-color:#0068c9;
    color:white;
    border-radius:10px;
    height:50px;
    width:100%;
    font-size:18px;
}
.result{
    padding:20px;
    border-radius:10px;
    font-size:25px;
    text-align:center;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Title
# -------------------------------
st.title("🏦 Customer Churn Prediction System")
st.write("Predict whether a customer is likely to leave the bank.")

st.divider()

# -------------------------------
# Sidebar
# -------------------------------
st.sidebar.header("Customer Information")

credit_score = st.sidebar.slider(
    "Credit Score",
    300, 900, 600
)

age = st.sidebar.slider(
    "Age",
    18, 100, 30
)

tenure = st.sidebar.slider(
    "Tenure (Years)",
    0, 10, 5
)

balance = st.sidebar.number_input(
    "Balance",
    value=50000.0
)

salary = st.sidebar.number_input(
    "Estimated Salary",
    value=50000.0
)

# -------------------------------
# Main Inputs
# -------------------------------
col1, col2 = st.columns(2)

with col1:

    num_products = st.selectbox(
        "Number of Products",
        [1,2,3,4]
    )

    has_card = st.radio(
        "Has Credit Card?",
        ["Yes","No"]
    )

with col2:

    active_member = st.radio(
        "Is Active Member?",
        ["Yes","No"]
    )

    gender = st.selectbox(
        "Gender",
        ["Male","Female"]
    )

country = st.selectbox(
    "Country",
    ["France","Germany","Spain"]
)

# -------------------------------
# Encoding
# -------------------------------
has_card = 1 if has_card=="Yes" else 0
active_member = 1 if active_member=="Yes" else 0

germany = 1 if country=="Germany" else 0
spain = 1 if country=="Spain" else 0

male = 1 if gender=="Male" else 0

# -------------------------------
# Predict Button
# -------------------------------
if st.button("🔍 Predict Churn"):

    data = np.array([[
        credit_score,
        age,
        tenure,
        balance,
        num_products,
        has_card,
        active_member,
        salary,
        germany,
        spain,
        male
    ]])

    scaled_data = scaler.transform(data)

    prediction = model.predict(scaled_data)
    probability = model.predict_proba(scaled_data)

    churn_prob = probability[0][1]
    stay_prob = probability[0][0]

    st.divider()

    st.subheader("Prediction Result")

    if prediction[0] == 1:
        st.error("❌ Customer Will Exit")
    else:
        st.success("✅ Customer Will Stay")

    st.write("### Prediction Confidence")

    st.progress(float(max(churn_prob, stay_prob)))

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Stay Probability",
            f"{stay_prob*100:.2f}%"
        )

    with col2:
        st.metric(
            "Exit Probability",
            f"{churn_prob*100:.2f}%"
        )

    st.subheader("Probability Distribution")

    st.bar_chart({
        "Probability":[stay_prob, churn_prob]
    })

st.divider()

st.caption("Machine Learning Model : Random Forest Classifier")