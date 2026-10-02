# 📊 Facebook Live Cluster Explorer

An interactive **K-Means Clustering** project built with Python, Scikit-learn, and Streamlit to explore engagement patterns in Facebook Live posts.

The project includes a Jupyter Notebook for data preparation and K-Means experimentation, plus a Streamlit dashboard that loads the trained model and scaler to predict the cluster of a new Facebook Live post.

> **Note:** The supplied saved model is a **2-cluster K-Means model** with 10 input features. The Streamlit dashboard is built around this saved model.

---

## 🚀 Project Overview

This project applies **K-Means Clustering**, an unsupervised machine learning algorithm, to Facebook Live seller engagement data.

The model uses post type and engagement/reaction features such as:

- Reactions
- Comments
- Shares
- Likes
- Loves
- Wows
- Hahas
- Sads
- Angrys
- Status type

The Streamlit application allows users to enter these values interactively and immediately see:

- Predicted cluster
- Distance to each cluster centroid
- Distance margin for the two-cluster model
- Scaled input values
- Engagement profile visualization
- Cluster profiles
- Scaled centroid comparison
- Model information

---

## 🎯 Objectives

- Explore the Facebook Live Sellers dataset.
- Perform basic exploratory data analysis.
- Remove redundant and identifier-like columns.
- Convert the categorical `status_type` feature into numeric labels.
- Scale features using `MinMaxScaler`.
- Apply K-Means clustering.
- Experiment with different numbers of clusters.
- Save the trained model and scaler.
- Build an interactive Streamlit dashboard for cluster prediction.

---

## 📁 Dataset

The project uses `Live.csv`, containing **7,050 records and 16 columns**.

The original dataset contains:

- `status_id`
- `status_type`
- `status_published`
- `num_reactions`
- `num_comments`
- `num_shares`
- `num_likes`
- `num_loves`
- `num_wows`
- `num_hahas`
- `num_sads`
- `num_angrys`
- `Column1`
- `Column2`
- `Column3`
- `Column4`

### Data preprocessing

The notebook removes:

```text
Column1
Column2
Column3
Column4
status_id
status_published
```

`status_id` and `status_published` are treated as identifier-like fields because they contain a very large number of unique values.

The remaining categorical feature is:

```text
status_type
```

It contains four categories:

```text
link
photo
status
video
```

For the supplied Streamlit application, these are represented as:

```text
link   → 0
photo  → 1
status → 2
video  → 3
```

The resulting model input contains 10 features.

---

## 🧠 Machine Learning Workflow

The project follows this general workflow:

```text
Facebook Live Dataset
        ↓
Exploratory Data Analysis
        ↓
Remove redundant / identifier-like columns
        ↓
Encode status_type
        ↓
MinMaxScaler
        ↓
K-Means Clustering
        ↓
Save Model + Scaler
        ↓
Streamlit Dashboard
        ↓
Interactive Cluster Prediction
```

---

## 🔬 K-Means Clustering

K-Means groups observations into clusters based on their distance from cluster centroids.

The supplied saved model uses:

```python
KMeans(n_clusters=2, random_state=0)
```

The saved model has:

- **Algorithm:** K-Means
- **Number of clusters:** 2
- **Number of features:** 10
- **Inertia:** approximately `237.7573`

The model works in the scaled feature space produced by `MinMaxScaler`.

### Important

Cluster numbers are model labels. For example, `Cluster 0` does **not automatically mean** "low engagement" and `Cluster 1` does **not automatically mean** "high engagement."

The cluster meaning should be interpreted by examining the centroid profiles and the characteristics of the posts assigned to each cluster.

---

## 📊 Model Features

The saved model expects the following feature order:

| # | Feature |
|---|---|
| 1 | `status_type` |
| 2 | `num_reactions` |
| 3 | `num_comments` |
| 4 | `num_shares` |
| 5 | `num_likes` |
| 6 | `num_loves` |
| 7 | `num_wows` |
| 8 | `num_hahas` |
| 9 | `num_sads` |
| 10 | `num_angrys` |

The supplied scaler uses Min-Max scaling to transform these features into the range `[0, 1]`.

---

## 🖥️ Streamlit Dashboard

The application is called:

**Facebook Live Cluster Explorer**

The dashboard lets users modify the post inputs from the sidebar.

### Quick examples

The application provides three predefined examples:

- **Low engagement**
- **Typical video**
- **High comments**

Users can also select **Custom** and enter their own values.

### Dashboard outputs

After entering the values, the application calculates:

1. Scaled feature values
2. Predicted cluster
3. Distance to each cluster centroid
4. Closest centroid distance
5. Distance margin
6. Engagement profile chart
7. Cluster centroid profiles

The model assigns the post to the cluster with the smallest centroid distance.

---

## 📈 Example Input

A typical video example included in the application uses:

```text
Status type : video
Reactions   : 529
Comments    : 512
Shares      : 262
Likes       : 432
Loves       : 92
Wows        : 3
Hahas       : 1
Sads        : 1
Angrys      : 0
```

You can modify these values directly in the dashboard.

---

## 📦 Project Structure

Recommended project structure:

```text
Facebook-Live-KMeans/
│
├── app.py
├── Live.csv
├── model.pkl
├── scaler.pkl
├── Day 71_K means Clustering_Project.ipynb
└── README.md
```

### Important filename note

The supplied artifacts were uploaded with these names:

```text
model(2).pkl
scaler(1).pkl
```

The current Streamlit application looks specifically for:

```text
model.pkl
scaler.pkl
```

Therefore, rename/copy the supplied files to:

```text
model.pkl
scaler.pkl
```

before running the dashboard.

---

## ⚙️ Installation

### 1. Clone or download the project

Place all required project files in the same directory.

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Activate it on macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install streamlit numpy pandas scikit-learn
```

---

## ▶️ Run the Streamlit App

Make sure the following files are in the same directory:

```text
app.py
model.pkl
scaler.pkl
```

Then run:

```bash
streamlit run app.py
```

Streamlit will provide a local URL where the dashboard can be opened in a browser.

---

## 📓 Jupyter Notebook

The notebook:

```text
Day 71_K means Clustering_Project.ipynb
```

contains the main experimentation workflow, including:

- Dataset loading
- Exploratory data analysis
- Missing-value checking
- Feature inspection
- Removal of redundant columns
- Encoding of `status_type`
- Min-Max feature scaling
- K-Means training
- Cluster-center inspection
- Inertia calculation
- Comparison of different cluster counts

The notebook experiments with multiple values of `k`, including 2, 3, 4, and 5.

For the saved dashboard artifacts used by the current application, the trained model is the **2-cluster model**.

---

## 📊 Evaluation Notes

The notebook compares K-Means cluster labels with the encoded `status_type` labels as an additional experiment.

For `k = 2`, the notebook reports:

```text
Correctly labeled: 63 / 7050
Accuracy: 0.01163
```

For `k = 4`, the notebook reports:

```text
Correctly labeled: 4340 / 7050
Accuracy: approximately 0.62
```

However, this comparison should be interpreted carefully because **K-Means is an unsupervised clustering algorithm**, while `status_type` is a categorical variable being used as a reference label. Cluster labels themselves are arbitrary and do not inherently correspond to the original category numbers.

For clustering quality, measures such as inertia, silhouette score, and cluster interpretability can also be considered.

---

## 🔍 How Prediction Works

The Streamlit app follows these steps:

```python
raw input
    ↓
convert values to NumPy array
    ↓
MinMaxScaler.transform()
    ↓
KMeans.predict()
    ↓
KMeans.transform()
    ↓
predicted cluster + centroid distances
```

The core prediction logic is conceptually:

```python
scaled = scaler.transform(raw)
prediction = model.predict(scaled)
distances = model.transform(scaled)
```

The cluster with the smallest distance is selected as the prediction.

---

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **K-Means Clustering**
- **MinMaxScaler**
- **Streamlit**
- **Matplotlib**
- **Seaborn**
- **Jupyter Notebook**
- **Pickle**

---

## 💡 Key Learning Outcomes

This project demonstrates practical understanding of:

- Unsupervised Machine Learning
- K-Means Clustering
- Feature preprocessing
- Categorical feature encoding
- Min-Max normalization
- Cluster centroids
- Inertia
- Cluster-distance analysis
- Exploratory Data Analysis
- Model serialization with Pickle
- Interactive ML deployment with Streamlit

---

## ⚠️ Limitations

- K-Means requires the number of clusters to be selected in advance.
- Cluster labels do not have an inherent business meaning.
- The dashboard uses the supplied trained model and scaler rather than retraining the model.
- The notebook's comparison with `status_type` should not be treated as a conventional supervised-learning accuracy measurement.
- The current application expects the model and scaler files to be available locally.
- The model was trained on the supplied feature representation and should receive inputs in the same feature order and preprocessing format.

---

## 🚀 Possible Future Improvements

- Add silhouette score analysis.
- Add an interactive elbow-method plot.
- Add PCA visualization of the clusters.
- Add cluster distribution charts.
- Allow CSV upload for batch predictions.
- Add downloadable prediction results.
- Add model retraining from the dashboard.
- Add automated model and scaler artifact validation.
- Deploy the Streamlit application online.

---

## 👨‍💻 Project

**Facebook Live Cluster Explorer — K-Means Clustering**

An end-to-end machine learning project demonstrating how an unsupervised learning model can be transformed into an interactive application for exploring Facebook Live engagement patterns.

---

## 📌 Note

This project is intended for learning and demonstration purposes. Cluster assignments should be interpreted using the model's centroid profiles and the underlying feature distributions rather than assuming that a particular cluster number represents a fixed engagement category.
