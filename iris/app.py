
from flask import Flask, request, jsonify, render_template_string
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model and scaler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

FEATURES = [
    "SepalLengthCm",
    "SepalWidthCm",
    "PetalLengthCm",
    "PetalWidthCm"
]

SPECIES_NAMES = {
    0: "Iris-setosa",
    1: "Iris-versicolor",
    2: "Iris-virginica"
}

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<title>Iris AI Studio</title>

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
rel="stylesheet">

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<style>
body {
    background: linear-gradient(135deg, #eef2ff, #fdf2f8);
    font-family: Arial, sans-serif;
    color: #25233a;
}

.hero {
    background: linear-gradient(120deg, #4f46e5, #9333ea);
    color: white;
    padding: 35px;
    border-radius: 22px;
    margin-bottom: 25px;
}

.panel {
    background: white;
    border-radius: 20px;
    padding: 25px;
    box-shadow: 0 8px 25px rgba(0,0,0,.07);
    margin-bottom: 22px;
}

.slider-value {
    color: #6d28d9;
    font-weight: bold;
}

input[type=range] {
    accent-color: #7c3aed;
}

.result {
    background: linear-gradient(135deg, #ede9fe, #fce7f3);
    border-radius: 18px;
    padding: 22px;
    text-align: center;
}

.flower-img {
    width: 100%;
    height: 210px;
    object-fit: cover;
    border-radius: 15px;
}

.btn-purple {
    background: #6d28d9;
    color: white;
    border: none;
}

.btn-purple:hover {
    background: #5b21b6;
    color: white;
}

.metric {
    background: #f5f3ff;
    border-radius: 12px;
    padding: 12px;
    text-align: center;
}

footer {
    color: #777;
    text-align: center;
    padding: 20px;
}
</style>
</head>

<body>
<div class="container py-4">

<div class="hero">
    <h1>🌸 Iris </h1>
    <p class="mb-0">
        Interactive machine learning flower classification dashboard
    </p>
</div>

<div class="row g-4">

<div class="col-lg-5">
<div class="panel">

<h4>🎚️ Flower Measurements</h4>
<p class="text-muted">Adjust the sliders to classify a flower.</p>

<div class="mb-4">
<label>Sepal Length: <span id="v0" class="slider-value">5.1</span> cm</label>
<input type="range" class="form-range" id="f0" min="4.0" max="8.0"
step="0.1" value="5.1">
</div>

<div class="mb-4">
<label>Sepal Width: <span id="v1" class="slider-value">3.5</span> cm</label>
<input type="range" class="form-range" id="f1" min="2.0" max="4.5"
step="0.1" value="3.5">
</div>

<div class="mb-4">
<label>Petal Length: <span id="v2" class="slider-value">1.4</span> cm</label>
<input type="range" class="form-range" id="f2" min="1.0" max="7.0"
step="0.1" value="1.4">
</div>

<div class="mb-4">
<label>Petal Width: <span id="v3" class="slider-value">0.2</span> cm</label>
<input type="range" class="form-range" id="f3" min="0.1" max="2.5"
step="0.1" value="0.2">
</div>

<button class="btn btn-purple w-100 py-2" onclick="predict()">
🔍 Predict Species
</button>

<div class="d-flex gap-2 mt-3">
<button class="btn btn-outline-secondary w-50" onclick="sample()">
🎲 Random Sample
</button>
<button class="btn btn-outline-danger w-50" onclick="resetForm()">
↺ Reset
</button>
</div>

</div>
</div>

<div class="col-lg-7">

<div class="panel">
<h4>🌺 Prediction Result</h4>

<div class="result">
<h2 id="species">Waiting for prediction...</h2>
<p id="confidence">Move the sliders and click Predict</p>
</div>

<div class="row g-2 mt-3">
<div class="col-6">
<div class="metric">
<small>Sepal Length</small>
<h5 id="m0">5.1 cm</h5>
</div>
</div>
<div class="col-6">
<div class="metric">
<small>Sepal Width</small>
<h5 id="m1">3.5 cm</h5>
</div>
</div>
<div class="col-6">
<div class="metric">
<small>Petal Length</small>
<h5 id="m2">1.4 cm</h5>
</div>
</div>
<div class="col-6">
<div class="metric">
<small>Petal Width</small>
<h5 id="m3">0.2 cm</h5>
</div>
</div>
</div>
</div>

<div class="panel">
<h4>📊 Species Probability</h4>
<canvas id="probChart"></canvas>
</div>

</div>
</div>

<div class="panel">
<h4>🌷 Explore Iris Species</h4>

<div class="row g-4 mt-1">

<div class="col-md-4">
<img class="flower-img"
src="https://images.unsplash.com/photo-1490750967868-88aa4486c946?w=700"
alt="Flower photograph">
<h5 class="mt-3">Iris Setosa</h5>
<p>Typically has shorter petals and a narrower petal profile.</p>
</div>

<div class="col-md-4">
<img class="flower-img"
src="https://images.unsplash.com/photo-1499002238440-d264edd596ec?w=700"
alt="Purple flower">
<h5 class="mt-3">Iris Versicolor</h5>
<p>Often shows intermediate petal measurements.</p>
</div>

<div class="col-md-4">
<img class="flower-img"
src="https://images.unsplash.com/photo-1497250681960-ef046c08a56e?w=700"
alt="Plant photograph">
<h5 class="mt-3">Iris Virginica</h5>
<p>Often has larger petal measurements in the Iris dataset.</p>
</div>

</div>
</div>

<div class="panel">
<h4>🕘 Prediction History</h4>
<div class="table-responsive">
<table class="table table-hover">
<thead>
<tr>
<th>#</th>
<th>Sepal Length</th>
<th>Sepal Width</th>
<th>Petal Length</th>
<th>Petal Width</th>
<th>Prediction</th>
</tr>
</thead>
<tbody id="history"></tbody>
</table>
</div>
<button class="btn btn-outline-danger btn-sm" onclick="clearHistory()">
Clear History
</button>
</div>

<footer>
Iris AI Studio | Flask + Machine Learning
</footer>

</div>

<script>
let historyCount = 0;

const chart = new Chart(document.getElementById("probChart"), {
    type: "bar",
    data: {
        labels: ["Setosa", "Versicolor", "Virginica"],
        datasets: [{
            label: "Probability (%)",
            data: [0, 0, 0],
            backgroundColor: ["#8b5cf6", "#ec4899", "#06b6d4"],
            borderRadius: 8
        }]
    },
    options: {
        responsive: true,
        scales: {
            y: {
                beginAtZero: true,
                max: 100,
                title: { display: true, text: "Probability (%)" }
            }
        },
        plugins: {
            legend: { display: false }
        }
    }
});

const ids = ["f0", "f1", "f2", "f3"];

ids.forEach((id, i) => {
    document.getElementById(id).addEventListener("input", () => {
        document.getElementById("v" + i).innerText =
            document.getElementById(id).value;
    });
});

async function predict() {
    const values = ids.map(id =>
        parseFloat(document.getElementById(id).value)
    );

    try {
        const response = await fetch("/predict", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({
                SepalLengthCm: values[0],
                SepalWidthCm: values[1],
                PetalLengthCm: values[2],
                PetalWidthCm: values[3]
            })
        });

        const result = await response.json();

        if (!response.ok) {
            alert(result.error || "Prediction failed");
            return;
        }

        document.getElementById("species").innerText =
            "🌸 " + result.prediction;

        document.getElementById("confidence").innerText =
            result.confidence !== null
            ? "Model confidence: " + result.confidence + "%"
            : "Prediction generated successfully";

        values.forEach((v, i) => {
            document.getElementById("m" + i).innerText = v + " cm";
        });

        if (result.probabilities) {
            chart.data.datasets[0].data = result.probabilities;
            chart.update();
        }

        historyCount++;

        const row = document.createElement("tr");
        [historyCount, ...values, result.prediction].forEach(value => {
            const cell = document.createElement("td");
            cell.textContent = value;
            row.appendChild(cell);
        });

        document.getElementById("history").prepend(row);

    } catch (error) {
        alert("Could not connect to Flask server.");
    }
}

function sample() {
    const samples = [
        [5.1, 3.5, 1.4, 0.2],
        [6.0, 2.9, 4.5, 1.5],
        [6.7, 3.0, 5.2, 2.3],
        [5.4, 3.4, 1.7, 0.2],
        [6.3, 2.8, 5.1, 1.5]
    ];

    const item = samples[Math.floor(Math.random() * samples.length)];

    item.forEach((value, i) => {
        document.getElementById(ids[i]).value = value;
        document.getElementById("v" + i).innerText = value;
    });

    predict();
}

function resetForm() {
    const defaults = [5.1, 3.5, 1.4, 0.2];

    defaults.forEach((value, i) => {
        document.getElementById(ids[i]).value = value;
        document.getElementById("v" + i).innerText = value;
        document.getElementById("m" + i).innerText = value + " cm";
    });

    document.getElementById("species").innerText =
        "Waiting for prediction...";

    document.getElementById("confidence").innerText =
        "Move the sliders and click Predict";

    chart.data.datasets[0].data = [0, 0, 0];
    chart.update();
}

function clearHistory() {
    document.getElementById("history").innerHTML = "";
    historyCount = 0;
}
</script>

</body>
</html>
"""

@app.route("/", methods=["GET"])
def home():
    return render_template_string(HTML)


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(silent=True) or {}

    try:
        values = [float(data[name]) for name in FEATURES]

        if not np.all(np.isfinite(values)):
            raise ValueError("Measurements must be finite numbers.")

        input_data = np.array([values])
        scaled = scaler.transform(input_data)

        prediction = model.predict(scaled)[0]

        if isinstance(prediction, (int, np.integer)):
            prediction = SPECIES_NAMES.get(int(prediction), str(prediction))
        else:
            prediction = str(prediction)

        probabilities = None
        confidence = None

        if hasattr(model, "predict_proba"):
            raw_probs = model.predict_proba(scaled)[0]
            probabilities = [round(float(p) * 100, 2) for p in raw_probs]
            confidence = round(float(max(raw_probs)) * 100, 2)

        return jsonify({
            "prediction": prediction,
            "confidence": confidence,
            "probabilities": probabilities
        })

    except (ValueError, KeyError, TypeError) as error:
        return jsonify({"error": str(error)}), 400


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)