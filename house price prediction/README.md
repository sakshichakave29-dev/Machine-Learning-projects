# 🏠 House Price Prediction System

A **Streamlit-based Machine Learning web application** that predicts the estimated price of a house from property, location, accessibility, and other housing features.

The application uses a **Decision Tree Regressor** together with feature encoding and a `DictVectorizer` to transform user-entered property information into the format expected by the trained model.

## 🚀 Project Overview

This project provides an interactive interface where users can enter house details such as:

- State and City
- Property Type
- BHK
- Size in Sq.Ft
- Price per Sq.Ft
- Year Built
- Furnished Status
- Floor Number
- Total Floors
- Age of Property
- Nearby Schools
- Nearby Hospitals
- Public Transport Accessibility
- Parking Space
- Security
- Amenities
- Facing
- Owner Type
- Availability Status

After clicking **Predict House Price**, the application displays the estimated house price in **Indian Rupees (₹ Lakhs)**.

## ✨ Features

- 🏠 Interactive house-price prediction
- 📍 Location-based inputs
- 🏢 Multiple property types
- 🛏️ BHK and property-size inputs
- 🛋️ Furnishing-status selection
- 🚗 Parking and security information
- 🏫 Nearby school and hospital counts
- 🚌 Public transport accessibility
- 🧭 Property-facing direction
- 🤖 Decision Tree Regressor model
- 🔢 DictVectorizer for feature transformation
- 🧩 Ordinal Encoding for selected categorical features
- 📋 Expandable input-data preview
- 🎈 Interactive Streamlit interface

## 🧠 Machine Learning Workflow

The application follows this general workflow:

```text
User Input
    ↓
Categorical Feature Encoding
    ↓
Ordinal Encoding
    ↓
Input Dictionary
    ↓
DictVectorizer
    ↓
Trained Decision Tree Regressor
    ↓
Predicted House Price
    ↓
Streamlit Result
```

The application loads the following serialized model components:

```text
house_price_model.pkl
vectorizer.pkl
encoder.pkl
features.pkl
```

The uploaded application code loads these components at startup. fileciteturn1file0L14-L27

## 🤖 Model

### Algorithm

**Decision Tree Regressor**

The application identifies the model in its sidebar as a Decision Tree Regressor and uses it to predict the estimated house price. fileciteturn1file0L224-L240

### Feature Processing

Selected categorical features are processed using an ordinal encoder:

- `Property_Type`
- `Furnished_Status`
- `Public_Transport_Accessibility`
- `Facing`
- `Security`

The encoded values are then included in the prediction input. fileciteturn1file0L149-L167

The resulting dictionary is transformed using `DictVectorizer` before being passed to the trained model. fileciteturn1file0L174-L205

## 📊 Input Features

The current Streamlit application accepts the following 20 inputs:

| # | Feature |
|---:|---|
| 1 | State |
| 2 | City |
| 3 | Property Type |
| 4 | BHK |
| 5 | Size in Sq.Ft |
| 6 | Price Per Sq.Ft |
| 7 | Year Built |
| 8 | Furnished Status |
| 9 | Floor Number |
| 10 | Total Floors |
| 11 | Age of Property |
| 12 | Nearby Schools |
| 13 | Nearby Hospitals |
| 14 | Public Transport |
| 15 | Parking Space |
| 16 | Security |
| 17 | Amenities |
| 18 | Facing |
| 19 | Owner Type |
| 20 | Availability Status |

These fields correspond to the inputs defined in the Streamlit application. fileciteturn1file0L40-L148

## 📁 Project Structure

Recommended GitHub repository structure:

```text
House-Price-Prediction/
│
├── app(8).py
├── E06_house price data less(2).csv
│
├── house_price_model.pkl
├── vectorizer.pkl
├── encoder.pkl
├── features.pkl
│
└── README.md
```

> Make sure the four `.pkl` files are present in the same working directory as the Streamlit application. The application opens these files directly by filename. fileciteturn1file0L14-L27

## 🛠️ Technologies Used

- **Python**
- **Streamlit**
- **Pandas**
- **Scikit-learn**
- **Pickle**
- **DictVectorizer**
- **Ordinal Encoding**
- **Decision Tree Regression**

The application imports Streamlit, Pandas, and Pickle directly. fileciteturn1file0L1-L3

## ⚙️ Installation

### 1. Clone the repository

Replace the URL with your own GitHub repository:

```bash
git clone https://github.com/YOUR_USERNAME/house-price-prediction.git
cd house-price-prediction
```

### 2. Create a virtual environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install streamlit pandas scikit-learn
```

### 4. Run the application

If your Python file is named `app(8).py`:

```bash
streamlit run "app(8).py"
```

The application will open in your browser.

## 💻 How to Use

1. Start the Streamlit application.
2. Select the **State**.
3. Enter the **City**.
4. Select the **Property Type**.
5. Enter BHK and property size.
6. Enter the price per square foot.
7. Enter construction year and property age.
8. Select furnishing status.
9. Enter floor information.
10. Enter nearby school and hospital counts.
11. Select public transport accessibility.
12. Select parking and security options.
13. Enter amenities, facing, owner type, and availability.
14. Click **Predict House Price**.
15. View the estimated price in the result section.

The application displays the result using a Streamlit metric labeled **Estimated House Price**. fileciteturn1file0L201-L214

## 📋 View Input Data

The application includes a **View Input Data** expandable section that displays the current prediction input dictionary. fileciteturn1file0L249-L255

## 📌 Example

Example input:

```text
State: Maharashtra
City: Nagpur
Property Type: Apartment
BHK: 2
Size: 1200 Sq.Ft
Price Per Sq.Ft: 5000
Year Built: 2018
Furnished: Semi-furnished
Floor: 2
Total Floors: 10
Age: 5
Nearby Schools: 5
Nearby Hospitals: 3
Public Transport: High
Parking: Yes
Security: Yes
Amenities: Gym, Lift, Garden
Facing: East
Owner Type: Owner
Availability: Ready to Move
```

The actual prediction depends on the trained model and the complete encoded feature representation.

## 📈 Output

The prediction is displayed in the format:

```text
Estimated House Price
₹ XX.XX Lakhs
```

The application formats the model prediction as Indian Rupees in Lakhs. fileciteturn1file0L205-L212

## ⚠️ Important Notes

- The prediction is an **estimated machine-learning output**, not a guaranteed market price.
- Model performance depends on the training data and preprocessing used to create the serialized model files.
- The `.pkl` files must match the preprocessing and feature format expected by the application.
- Do not load pickle files from untrusted sources.
- Real estate prices can vary based on market conditions, exact location, property condition, legal status, and many other factors not necessarily represented in the model.

## 🔮 Future Improvements

Possible improvements include:

- Add model evaluation metrics
- Add actual-vs-predicted price visualization
- Add feature importance visualization
- Add price comparison by city
- Add historical market trends
- Add map/location visualization
- Add multiple ML model comparison
- Add input validation and clearer error messages
- Deploy the application using Streamlit Community Cloud
- Add a responsive dashboard design
- Add downloadable prediction reports

## 👨‍💻 Author

**Your Name**

GitHub: https://github.com/sakshichakave29-dev/Machine-Learning-projects/tree/main/house%20price%20prediction

LinkedIn: https://www.linkedin.com/posts/sakshi-chakave-15a211380_machinelearning-datascience-python-activity-7491400984187854849-l0c5?utm_source=share&utm_medium=member_desktop&rcm=ACoAAF4A8JYBrwSz76kkhrv4cNSG4WF5ky3mbfU

## ⭐ [Support))

If you find this project useful, consider giving the GitHub repository a ⭐ star.

---

### 🏠 House Price Prediction System

**Built with Python + Streamlit + Scikit-learn**
