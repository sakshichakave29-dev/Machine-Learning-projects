# 🚗 Automobile Price Prediction Dashboard

An interactive **Automobile Price Prediction Dashboard** built with **Streamlit** and a **Decision Tree Regression** model. The application combines exploratory data analysis, interactive filtering, visualizations, and automobile price prediction in one dashboard.

## 📌 Project Overview

This project uses an automobile dataset containing vehicle specifications and prices. A Decision Tree Regression model is trained on the numeric vehicle characteristics and saved as a pickle file. The Streamlit application loads the trained model and dataset to provide interactive analysis and price prediction.

## ✨ Features

### 📊 Interactive Dashboard
- Filter vehicles by:
  - Make
  - Fuel Type
  - Body Style
  - Drive Wheels
  - Price Range
- View KPI cards for:
  - Number of vehicles
  - Average price
  - Average horsepower
  - Average engine size

### 📈 Data Visualizations
The dashboard includes:
- Average automobile price by make
- Engine size vs. price
- Vehicle distribution by body style
- Horsepower vs. price
- Automobile price distribution

### 🔮 Price Prediction
Users can enter numeric vehicle characteristics and get an estimated automobile price using the trained **Decision Tree Regressor**.

### 📋 Data Exploration
A filtered automobile data table is displayed at the bottom of the dashboard.

## 🛠️ Technologies Used

- **Python**
- **Streamlit** – interactive web dashboard
- **Pandas** – data loading and manipulation
- **NumPy** – numerical processing
- **Plotly Express** – interactive charts
- **Scikit-learn** – machine learning
- **Pickle** – model serialization
- **Jupyter Notebook** – model development and experimentation

## 📂 Project Structure

```text
Automobile-Price-Prediction/
│
├── app.py
├── autos_dataset.csv
├── auto_price_decision_tree.pkl
├── Day 60_Decision Tree Linear regression_Auto Data Set.ipynb
└── README.md
```

> **Important:** The Streamlit application expects the dataset to be named `autos_dataset.csv` and the model to be named `auto_price_decision_tree.pkl`, located in the same directory as `app.py`.

## 📦 Installation

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd Automobile-Price-Prediction
```

### 2. Create a virtual environment (optional)

```bash
python -m venv venv
```

Activate it:

**Windows**
```bash
venv\Scripts\activate
```

**macOS / Linux**
```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install streamlit pandas numpy plotly scikit-learn
```

## ▶️ Run the Dashboard

Make sure these three files are in the same folder:

```text
app.py
autos_dataset.csv
auto_price_decision_tree.pkl
```

Then run:

```bash
streamlit run app.py
```

The application will open in your browser.

## 🤖 Machine Learning Workflow

The model development follows these main steps:

1. Load the automobile dataset.
2. Convert the `num-of-cylinders` values from words to numbers.
3. Replace `?` values with missing values (`NaN`).
4. Convert `price`, `horsepower`, and `peak-rpm` to numeric values.
5. Remove categorical/non-model columns.
6. Fill missing numeric values using column means.
7. Separate features (`X`) and target (`y`).
8. Split the data into training and testing sets using an 80/20 split with `random_state=42`.
9. Train a `DecisionTreeRegressor`.
10. Save the trained model as `auto_price_decision_tree.pkl`.

The training notebook also contains experimentation with model evaluation and hyperparameter tuning using `GridSearchCV`.

## 🧮 Model

**Algorithm:** Decision Tree Regression

```python
from sklearn.tree import DecisionTreeRegressor

model = DecisionTreeRegressor(random_state=42)
model.fit(X_train, y_train)
```

The saved model is loaded by the Streamlit application using Python's `pickle` module.

## 📊 Dataset

The project uses an automobile dataset with **205 records and 26 columns**, including attributes such as:

- Make
- Fuel type
- Body style
- Drive wheels
- Engine size
- Horsepower
- City MPG
- Highway MPG
- Price

The target variable for prediction is:

```text
price
```

## 🔍 Prediction Features

The dashboard uses numeric vehicle characteristics after removing categorical/non-model columns. These include fields such as:

- `symboling`
- `wheel-base`
- `length`
- `width`
- `height`
- `curb-weight`
- `num-of-cylinders`
- `engine-size`
- `compression-ratio`
- `horsepower`
- `peak-rpm`
- `city-mpg`
- `highway-mpg`

Missing numeric values are handled using mean values before prediction.

## ⚠️ Important Notes

- The `.pkl` model should be used with preprocessing consistent with the training process.
- The Streamlit app and saved model must use compatible feature names and ordering.
- The application displays an estimated price; it should not be treated as a guaranteed market price.
- When sharing the project publicly, avoid committing sensitive files or credentials.

## 🚀 Future Improvements

Possible enhancements include:

- Compare Decision Tree with Linear Regression, Random Forest, and Gradient Boosting.
- Add model performance metrics such as MAE, RMSE, and R² to the dashboard.
- Add model feature-importance visualization.
- Improve categorical feature handling with proper encoding.
- Add downloadable filtered data.
- Deploy the Streamlit application online.
- Add a dedicated requirements file.

## 👨‍💻 Project

**Automobile Price Prediction Dashboard**

Built as a practical project combining **Data Analysis, Machine Learning, and Streamlit Dashboard Development**.

## 📜 License

This project is intended for educational and portfolio purposes. Add an appropriate license if you plan to distribute or modify the project publicly.
