# 🌸 Iris Studio – Machine Learning Flower Classification Dashboard

An interactive web application built with **Flask** and **Machine Learning** for exploring and predicting Iris flower classes from four flower measurements.

The project combines an **Iris K-Means clustering notebook** with a Flask-based interactive dashboard.

## 🚀 Project Overview

The application takes four Iris flower measurements:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

Users can adjust the measurements using sliders and click **Predict Species** to generate a model prediction.

The dashboard also provides:

- 🌸 Interactive flower classification
- 🎚️ Measurement sliders
- 📊 Prediction result display
- 📈 Species probability chart when probability output is available
- 🎲 Random sample generation
- 🔄 Reset controls
- 🕘 Prediction history
- 🌷 Iris species information
- 🎨 Responsive Bootstrap-based interface

The Flask application loads a saved scaler and machine-learning model using `joblib`.

##  Machine Learning

The notebook uses **K-Means Clustering** on the Iris dataset.

### Dataset

The included `Iris.csv` contains:

- **150 samples**
- **4 numerical features**
- **3 Iris species**

Features used for clustering:

```text
SepalLengthCm
SepalWidthCm
PetalLengthCm
PetalWidthCm
```

The `Species` column is used only for post-hoc evaluation in the clustering notebook, not for fitting K-Means.

### Preprocessing

The four numerical features are standardized using:

```python
StandardScaler()
```

### Clustering

K-Means is evaluated for multiple values of K. The notebook uses:

- Elbow Method
- Silhouette Score
- Post-hoc accuracy comparison
- Confusion matrix
- PCA visualization

The final notebook configuration uses:

```text
K = 3
```

because the Iris dataset contains three known species.

The final model is saved as:

```text
model.pkl
```

and the fitted scaler is saved as:

```text
scaler.pkl
```

## 📁 Project Structure

```text
.
├── app(20261004-065423).py
├── Iris.csv
├── Iris_KMeans_Clustering_Corrected.ipynb
├── model.pkl
├── scaler.pkl
└── README.md
```

> `model.pkl` and `scaler.pkl` are generated from the notebook. Make sure these files are present before starting the Flask application.

## 🛠️ Technologies Used

- Python
- Flask
- NumPy
- Pandas
- Scikit-learn
- Joblib
- Matplotlib
- Seaborn
- Bootstrap 5
- Chart.js
- Jupyter Notebook

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <https://github.com/sakshichakave29-dev/Machine-Learning-projects>
cd <c:\iris>
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install flask numpy pandas scikit-learn joblib matplotlib seaborn jupyter
```

## ▶️ Run the Project

First, make sure `model.pkl` and `scaler.pkl` are in the same directory as the Flask application.

Then run:

```bash
python app(20261004-065423).py
```

The Flask server runs on:

```text
http://127.0.0.1:5000
```

Open that address in your browser.

## 🔌 API Endpoint

The application exposes a prediction endpoint:

```text
POST /predict
```

Example request:

```json
{
  "SepalLengthCm": 5.1,
  "SepalWidthCm": 3.5,
  "PetalLengthCm": 1.4,
  "PetalWidthCm": 0.2
}
```

The Flask backend validates the measurements, applies the saved scaler, and sends the transformed values to the saved model.

## 📊 Notebook Workflow

The machine-learning notebook follows this workflow:

```text
Load Iris Dataset
       ↓
Exploratory Data Analysis
       ↓
Select 4 Numerical Features
       ↓
Standardize Features
       ↓
Evaluate K = 2, 3, 4, 5, 6
       ↓
Elbow Method + Silhouette Score
       ↓
Select K = 3
       ↓
K-Means Clustering
       ↓
Post-hoc Species Comparison
       ↓
Confusion Matrix
       ↓
PCA Visualization
       ↓
Save Model + Scaler
```

## 📈 Visualizations

The notebook includes:

- Iris feature relationship plots
- Elbow curve
- Silhouette score comparison
- Clustering accuracy comparison
- Confusion matrix
- PCA-based cluster visualization
- Species/cluster comparison

The Flask dashboard includes an interactive probability chart when the loaded model provides probability estimates.

## ⚠️ Important Note About K-Means

K-Means is an **unsupervised learning algorithm**. Cluster IDs are arbitrary.

For example, cluster `0` does not inherently mean `Iris-setosa`. Therefore, comparing cluster IDs directly with species labels is not valid without a label-mapping step.

The notebook handles this by using **majority-species mapping for post-hoc evaluation**.

Also, clustering accuracy and silhouette score measure different things:

- **Accuracy** measures agreement with the known species labels after mapping.
- **Silhouette Score** evaluates the quality/separation of the clusters without using the species labels for training.

## 🎯 Learning Outcomes

This project demonstrates practical experience with:

- Unsupervised Machine Learning
- K-Means Clustering
- Feature standardization
- Exploratory Data Analysis
- Model evaluation
- PCA
- Flask API development
- Interactive web dashboards
- JavaScript and Chart.js
- Connecting a trained ML model to a web application

## 🔮 Future Improvements

Possible improvements include:

- Add a proper cluster-to-species mapping layer in the Flask API
- Display cluster assignments separately from species labels
- Add model evaluation metrics directly to the dashboard
- Add downloadable prediction history
- Add more datasets and models
- Deploy the application using a cloud platform
- Add automated model training and model versioning

## 👨‍💻 Author

sakshi chakave

- GitHub: <https://github.com/sakshichakave29-dev/Machine-Learning-projects/tree/main/iris>
linkdin:<https://lnkd.in/p/gF4TXye4>

## ⭐ Support

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.
