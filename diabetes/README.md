# 🩸 DiabetesAI — Diabetes Risk Intelligence Platform

A Streamlit-based machine learning application for **educational diabetes risk assessment** using a Decision Tree classifier. The project provides an interactive dashboard for entering patient metrics, generating model predictions, exploring the dataset, reviewing prediction history, and visualizing the model architecture.

> **Medical Disclaimer:** This project is intended strictly for educational, portfolio, and analytical demonstration purposes. It is **not a medical diagnostic tool** and must not be used as a substitute for advice from a qualified healthcare professional.

## ✨ Features

- 🔮 **Prediction Engine** — Enter patient clinical metrics and generate a diabetes-risk prediction.
- 📊 **Analytics Hub** — View historical assessment statistics and risk-level distributions.
- 📜 **Prediction History** — Store and export previous predictions as CSV.
- 🗂️ **Dataset Explorer** — Inspect the diabetes dataset and visualize feature distributions.
- 🤖 **Model Architecture** — Display the Decision Tree configuration and feature ordering.
- 📚 **Clinical Insights** — Educational explanations of selected diabetes-related biomarkers.
- 📥 **Report Export** — Download an individual prediction summary as CSV.
- 🎨 **Modern UI** — Streamlit dashboard with glassmorphism styling and Plotly visualizations.

## 🧠 Machine Learning Model

The application uses a **Decision Tree Classifier**.

### Model configuration

| Parameter | Value |
|---|---|
| Algorithm | Decision Tree Classifier |
| Max Depth | 7 |
| Min Samples Leaf | 15 |
| Min Samples Split | 2 |
| Target | `Outcome` (0 or 1) |
| Input Features | 8 numerical features |

### Input features

1. Pregnancies
2. Glucose
3. BloodPressure
4. SkinThickness
5. Insulin
6. BMI
7. DiabetesPedigreeFunction
8. Age

The application loads the trained model and feature list from:

- `diabetes_model.pkl`
- `diabetes_features.pkl`

## 📁 Project Structure

```text
DiabetesAI/
│
├── app(5).py
├── Day 58_Decision Tree Diabetes Data.ipynb
├── diabetes.csv
├── diabetes_model.pkl
├── diabetes_features.pkl
├── prediction_history.csv
├── DT_Diabetes.png
└── README.md
```

## 🖥️ Dashboard Preview

### Decision Tree Visualization

![Decision Tree](DT_Diabetes.png)

## 🛠️ Technologies Used

- **Python**
- **Streamlit** — interactive web application
- **Scikit-learn** — machine learning model
- **Pandas** — data processing
- **NumPy** — numerical operations
- **Plotly** — interactive charts
- **Pickle** — loading the trained ML model and feature configuration

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

### 2. Create a virtual environment

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
pip install streamlit pandas numpy scikit-learn plotly
```

### 4. Run the application

Because the application file is named `app(5).py`, run:

```bash
streamlit run "app(5).py"
```

The Streamlit application will open in your browser.

## 📊 Dataset

The project uses `diabetes.csv` as the dataset for exploration and analysis.

The application expects the target column:

```text
Outcome
```

where:

- `0` = negative class
- `1` = positive class

## 🔍 How the Prediction Works

The Prediction Engine collects eight numerical inputs and places them into a Pandas DataFrame in the same feature order used by the trained model.

The model then generates:

- Classification (`0` or `1`)
- Diabetes probability
- Risk category
- Classification confidence

The application categorizes the calculated diabetes probability as:

| Probability | Risk Category |
|---:|---|
| 0–30% | Low Risk |
| >30–60% | Moderate Risk |
| >60–80% | High Risk |
| >80–100% | Very High Risk |

These categories are application-specific visualization labels and should not be interpreted as clinically validated risk thresholds.

## 📈 Prediction History

Each executed assessment can be recorded in:

```text
prediction_history.csv
```

The stored fields include:

- Timestamp
- Pregnancies
- Glucose
- BloodPressure
- SkinThickness
- Insulin
- BMI
- DiabetesPedigreeFunction
- Age
- Prediction
- Probability
- RiskLevel

## 📓 Notebook

The repository also contains the supporting Jupyter Notebook:

```text
Day 58_Decision Tree Diabetes Data.ipynb
```

This can be used to review the machine-learning/data-analysis workflow associated with the project.

## ⚠️ Important Notes

- The model output is a machine-learning prediction, not a clinical diagnosis.
- The project is designed for learning, portfolio demonstration, and experimentation.
- The trained `.pkl` files should only be loaded from trusted sources.
- Do not use this application to make medical decisions.
- Always consult a qualified healthcare professional for personal health concerns.

## 👨‍💻 Author

**Your Name**

GitHub: `https://github.com/YOUR_USERNAME`

## ⭐ Future Improvements

Possible extensions include:

- Model performance metrics such as accuracy, precision, recall, F1-score, and ROC-AUC
- Confusion matrix visualization
- Feature importance visualization
- Model comparison with Random Forest, Logistic Regression, and other classifiers
- Improved input validation
- Cloud deployment
- User authentication
- More comprehensive experiment tracking

---

⭐ If you find this project useful for learning or portfolio purposes, consider giving the repository a star.
