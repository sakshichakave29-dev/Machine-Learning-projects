import streamlit as st
import pandas as pd
import numpy as np
import pickle
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Auto Price Prediction Dashboard",
    page_icon="🚗",
    layout="wide"
)

# -------------------------------------------------
# Load model and dataset
# -------------------------------------------------

@st.cache_resource
def load_model():
    with open("auto_price_decision_tree.pkl", "rb") as file:
        return pickle.load(file)

@st.cache_data
def load_data():
    df = pd.read_csv("autos_dataset.csv")

    df["num-of-cylinders"] = df["num-of-cylinders"].replace({
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "eight": 8,
        "twelve": 12
    })

    df = df.replace("?", np.nan)

    for col in ["price", "horsepower", "peak-rpm"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    return df

model = load_model()
df = load_data()

# -------------------------------------------------
# Title
# -------------------------------------------------

st.title("🚗 Automobile Price Prediction Dashboard")
st.markdown(
    "Interactive dashboard using a **Decision Tree Regression** model."
)

# -------------------------------------------------
# Sidebar Slicers
# -------------------------------------------------

st.sidebar.header("🎛️ Dashboard Slicers")

# Make
make_list = sorted(df["make"].dropna().unique())
selected_make = st.sidebar.multiselect(
    "Select Make",
    make_list,
    default=make_list
)

# Fuel type
fuel_list = sorted(df["fuel-type"].dropna().unique())
selected_fuel = st.sidebar.multiselect(
    "Select Fuel Type",
    fuel_list,
    default=fuel_list
)

# Body style
body_list = sorted(df["body-style"].dropna().unique())
selected_body = st.sidebar.multiselect(
    "Select Body Style",
    body_list,
    default=body_list
)

# Drive wheels
drive_list = sorted(df["drive-wheels"].dropna().unique())
selected_drive = st.sidebar.multiselect(
    "Select Drive Wheels",
    drive_list,
    default=drive_list
)

# Price range
df["price"] = pd.to_numeric(df["price"], errors="coerce")

min_price = float(df["price"].min())
max_price = float(df["price"].max())

price_range = st.sidebar.slider(
    "Price Range",
    min_value=min_price,
    max_value=max_price,
    value=(min_price, max_price)
)

# -------------------------------------------------
# Apply filters
# -------------------------------------------------

filtered_df = df[
    (df["make"].isin(selected_make)) &
    (df["fuel-type"].isin(selected_fuel)) &
    (df["body-style"].isin(selected_body)) &
    (df["drive-wheels"].isin(selected_drive)) &
    (df["price"].between(price_range[0], price_range[1]))
].copy()

if filtered_df.empty:
    st.warning("No vehicles match the selected filters.")
    st.stop()

# -------------------------------------------------
# KPI Cards
# -------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "🚘 Vehicles",
    f"{len(filtered_df):,}"
)

col2.metric(
    "💰 Average Price",
    f"${filtered_df['price'].mean():,.0f}"
)

col3.metric(
    "🐎 Average Horsepower",
    f"{pd.to_numeric(filtered_df['horsepower'], errors='coerce').mean():,.0f}"
)

col4.metric(
    "⚙️ Average Engine Size",
    f"{pd.to_numeric(filtered_df['engine-size'], errors='coerce').mean():,.0f}"
)

st.divider()

# -------------------------------------------------
# Chart 1 - Average Price by Make
# -------------------------------------------------

st.subheader("📊 Average Price by Make")

price_make = (
    filtered_df.groupby("make", as_index=False)["price"]
    .mean()
    .sort_values("price", ascending=False)
)

fig1 = px.bar(
    price_make,
    x="make",
    y="price",
    text_auto=".0f",
    title="Average Automobile Price by Make",
    labels={
        "make": "Make",
        "price": "Average Price"
    }
)

fig1.update_layout(
    xaxis_tickangle=-45,
    height=500
)

st.plotly_chart(fig1, use_container_width=True)

# -------------------------------------------------
# Chart 2 - Engine Size vs Price
# -------------------------------------------------

st.subheader("📈 Engine Size vs Price")

scatter_df = filtered_df.copy()
scatter_df["engine-size"] = pd.to_numeric(
    scatter_df["engine-size"],
    errors="coerce"
)
scatter_df["horsepower"] = pd.to_numeric(
    scatter_df["horsepower"],
    errors="coerce"
)

fig2 = px.scatter(
    scatter_df,
    x="engine-size",
    y="price",
    color="fuel-type",
    size="horsepower",
    hover_name="make",
    hover_data=[
        "body-style",
        "drive-wheels",
        "horsepower"
    ],
    title="Engine Size vs Automobile Price",
    labels={
        "engine-size": "Engine Size",
        "price": "Price"
    }
)

fig2.update_layout(height=500)

st.plotly_chart(fig2, use_container_width=True)

# -------------------------------------------------
# Chart 3 - Body Style Pie Chart
# -------------------------------------------------

st.subheader("🥧 Vehicle Distribution by Body Style")

body_count = (
    filtered_df["body-style"]
    .value_counts()
    .reset_index()
)

body_count.columns = ["body-style", "count"]

fig3 = px.pie(
    body_count,
    names="body-style",
    values="count",
    hole=0.4,
    title="Vehicle Distribution"
)

fig3.update_layout(height=500)

st.plotly_chart(fig3, use_container_width=True)

# -------------------------------------------------
# Chart 4 - Horsepower vs Price
# -------------------------------------------------

st.subheader("🐎 Horsepower vs Price")

fig4 = px.scatter(
    scatter_df,
    x="horsepower",
    y="price",
    color="drive-wheels",
    hover_name="make",
    hover_data=[
        "engine-size",
        "city-mpg",
        "highway-mpg"
    ],
    title="Horsepower vs Automobile Price",
    labels={
        "horsepower": "Horsepower",
        "price": "Price"
    }
)

fig4.update_layout(height=500)

st.plotly_chart(fig4, use_container_width=True)

# -------------------------------------------------
# Price Distribution
# -------------------------------------------------

st.subheader("💵 Price Distribution")

fig5 = px.histogram(
    filtered_df,
    x="price",
    nbins=30,
    title="Distribution of Automobile Prices",
    labels={"price": "Price"}
)

fig5.update_layout(height=450)

st.plotly_chart(fig5, use_container_width=True)

# -------------------------------------------------
# Prediction Section
# -------------------------------------------------

st.divider()
st.header("🔮 Predict Automobile Price")

st.write(
    "Enter the numeric vehicle characteristics used by "
    "the Decision Tree model."
)

# The pickle created earlier contains the raw model.
# These are the model input columns after preprocessing.
drop_columns = [
    "make",
    "fuel-type",
    "aspiration",
    "engine-type",
    "normalized-losses",
    "num-of-doors",
    "bore",
    "stroke",
    "fuel-system",
    "body-style",
    "drive-wheels",
    "engine-location",
    "price"
]

model_features = [
    col for col in df.columns
    if col not in drop_columns
]

# Convert model feature columns to numeric
for col in model_features:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Fill missing values
feature_means = df[model_features].mean()

with st.form("prediction_form"):

    input_values = {}

    prediction_columns = st.columns(3)

    for i, feature in enumerate(model_features):

        default_value = feature_means[feature]

        if pd.isna(default_value):
            default_value = 0.0

        with prediction_columns[i % 3]:
            input_values[feature] = st.number_input(
                feature,
                value=float(default_value),
                format="%.2f"
            )

    predict_button = st.form_submit_button(
        "🚀 Predict Price"
    )

if predict_button:

    input_data = pd.DataFrame(
        [input_values],
        columns=model_features
    )

    try:
        prediction = model.predict(input_data)

        st.success(
            f"### Estimated Automobile Price: ${prediction[0]:,.2f}"
        )

    except Exception as e:
        st.error(
            "Prediction failed. Make sure the pickle file "
            "was created using the same preprocessing as this app."
        )
        st.exception(e)

# -------------------------------------------------
# Data Table
# -------------------------------------------------

st.divider()

st.subheader("📋 Filtered Automobile Data")

display_columns = [
    "make",
    "fuel-type",
    "body-style",
    "drive-wheels",
    "engine-size",
    "horsepower",
    "city-mpg",
    "highway-mpg",
    "price"
]

display_columns = [
    col for col in display_columns
    if col in filtered_df.columns
]

st.dataframe(
    filtered_df[display_columns],
    use_container_width=True
)

st.caption(
    "Dashboard created with Streamlit, Plotly, Pandas and Scikit-learn."
)
