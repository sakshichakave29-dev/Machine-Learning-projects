from flask import Flask, render_template, request
import pandas as pd
from pathlib import Path
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
CSV_FILE = BASE_DIR / "data.csv"

df = pd.read_csv("KNN_reg_outlet_sales - KNN_reg_outlet_sales.csv")

TARGET = "Item_Outlet_Sales"

# Build model automatically from the uploaded dataset
X = df.drop(columns=[TARGET])
y = df[TARGET]

categorical_cols = X.select_dtypes(include=["object", "category"]).columns.tolist()
numeric_cols = X.select_dtypes(exclude=["object", "category"]).columns.tolist()

preprocessor = ColumnTransformer(
    transformers=[
        (
            "num",
            Pipeline([
                ("imputer", SimpleImputer(strategy="median"))
            ]),
            numeric_cols,
        ),
        (
            "cat",
            Pipeline([
                ("imputer", SimpleImputer(strategy="most_frequent")),
                ("onehot", OneHotEncoder(handle_unknown="ignore")),
            ]),
            categorical_cols,
        ),
    ]
)

model = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(
        n_estimators=200,
        random_state=42,
        n_jobs=-1
    )),
])

model.fit(X, y)


@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    error = None

    if request.method == "POST":
        try:
            input_data = {}

            for column in X.columns:
                value = request.form.get(column, "")

                if column in numeric_cols:
                    input_data[column] = float(value) if value != "" else None
                else:
                    input_data[column] = value

            input_df = pd.DataFrame([input_data])
            prediction = round(float(model.predict(input_df)[0]), 2)

        except Exception as e:
            error = str(e)

    return render_template(
        "index.html",
        columns=X.columns.tolist(),
        numeric_cols=numeric_cols,
        categorical_cols=categorical_cols,
        prediction=prediction,
        error=error,
    )


@app.route("/data")
def data():
    return df.to_html(
        classes="table table-striped table-bordered",
        index=False
    )


if __name__ == "__main__":
    app.run(debug=True)
