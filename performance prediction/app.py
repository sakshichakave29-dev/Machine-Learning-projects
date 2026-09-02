import os
from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Placement Prediction</title>
    
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

    <style>
        :root {
            --glass-bg: rgba(255, 255, 255, 0.12);
            --glass-border: rgba(255, 255, 255, 0.25);
        }

        /* Animated Multi-Color Dynamic Background */
        body {
            background: linear-gradient(-45deg, #0f2027, #203a43, #2c5364, #4a00e0, #8e2de2, #f12711, #f5af19, #00c6ff);
            background-size: 400% 400%;
            animation: gradientBG 15s ease infinite;
            min-height: 100vh;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: #ffffff;
            padding-bottom: 40px;
        }

        @keyframes gradientBG {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        .glass-card {
            background: var(--glass-bg);
            backdrop-filter: blur(14px);
            -webkit-backdrop-filter: blur(14px);
            border: 1px solid var(--glass-border);
            border-radius: 20px;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        }

        .form-control, .form-select {
            background: rgba(255, 255, 255, 0.15);
            border: 1px solid rgba(255, 255, 255, 0.3);
            color: #fff !important;
            border-radius: 10px;
            padding: 12px;
        }

        .form-control::placeholder {
            color: rgba(255, 255, 255, 0.7);
        }

        .form-control:focus, .form-select:focus {
            background: rgba(255, 255, 255, 0.25);
            border-color: #00d2ff;
            box-shadow: 0 0 12px rgba(0, 210, 255, 0.6);
        }

        .btn-custom {
            background: linear-gradient(45deg, #ff007f, #7928ca);
            border: none;
            color: white;
            font-weight: 600;
            padding: 12px;
            border-radius: 10px;
            transition: all 0.3s ease;
        }

        .btn-custom:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 20px rgba(255, 0, 127, 0.5);
            color: white;
        }

        .stat-badge {
            background: rgba(255, 255, 255, 0.15);
            border-radius: 12px;
            padding: 15px;
            text-align: center;
        }

        .pulse-success {
            animation: pulse-green 2s infinite;
        }

        .pulse-danger {
            animation: pulse-red 2s infinite;
        }

        @keyframes pulse-green {
            0% { box-shadow: 0 0 0 0 rgba(40, 167, 69, 0.5); }
            70% { box-shadow: 0 0 0 15px rgba(40, 167, 69, 0); }
            100% { box-shadow: 0 0 0 0 rgba(40, 167, 69, 0); }
        }

        @keyframes pulse-red {
            0% { box-shadow: 0 0 0 0 rgba(220, 53, 69, 0.5); }
            70% { box-shadow: 0 0 0 15px rgba(220, 53, 69, 0); }
            100% { box-shadow: 0 0 0 0 rgba(220, 53, 69, 0); }
        }
    </style>
</head>

<body>

<div class="container py-5">
    <div class="text-center mb-5">
        <h1 class="display-4 fw-bold"><i class="fa-solid fa-graduation-cap text-warning me-2"></i> Placement Prediction</h1>
        <p class="text-light opacity-90">Placement Probability Assessment & Skill Gap Analysis</p>
    </div>

    <div class="row g-4">
        <div class="col-lg-5">
            <div class="glass-card p-4">
                <h4 class="mb-4 border-bottom border-light pb-2">
                    <i class="fa-solid fa-user-astronaut me-2"></i> Candidate Metrics
                </h4>

                <form method="POST">
                    <div class="mb-3">
                        <label class="form-label text-light">CGPA (out of 10.0)</label>
                        <div class="input-group">
                            <span class="input-group-text bg-transparent text-light border-light"><i class="fa-solid fa-chart-line"></i></span>
                            <input type="number" step="0.1" min="0" max="10" class="form-control" name="cgpa" placeholder="e.g. 8.2" value="{{ data.cgpa if data else '' }}" required>
                        </div>
                    </div>

                    <div class="mb-3">
                        <label class="form-label text-light">Aptitude & IQ Score</label>
                        <div class="input-group">
                            <span class="input-group-text bg-transparent text-light border-light"><i class="fa-solid fa-brain"></i></span>
                            <input type="number" min="50" max="160" class="form-control" name="iq" placeholder="e.g. 115" value="{{ data.iq if data else '' }}" required>
                        </div>
                    </div>

                    <div class="mb-3">
                        <label class="form-label text-light">Profile / Skill Score (0-100)</label>
                        <div class="input-group">
                            <span class="input-group-text bg-transparent text-light border-light"><i class="fa-solid fa-id-card"></i></span>
                            <input type="number" min="0" max="100" class="form-control" name="profile" placeholder="e.g. 75" value="{{ data.profile if data else '' }}" required>
                        </div>
                    </div>

                    <div class="mb-4">
                        <label class="form-label text-light">Completed Internships</label>
                        <div class="input-group">
                            <span class="input-group-text bg-transparent text-light border-light"><i class="fa-solid fa-briefcase"></i></span>
                            <input type="number" min="0" max="10" class="form-control" name="internships" placeholder="e.g. 2" value="{{ data.internships if data else '0' }}" required>
                        </div>
                    </div>

                    <button type="submit" class="btn btn-custom w-100">
                        <i class="fa-solid fa-wand-magic-sparkles me-2"></i> Calculate Prediction
                    </button>
                </form>
            </div>
        </div>

        <div class="col-lg-7">
            {% if result %}
            <div class="glass-card p-4 h-100">
                <h4 class="mb-4 border-bottom border-light pb-2">
                    <i class="fa-solid fa-chart-pie me-2"></i> Prediction Analytics
                </h4>

                <div class="alert {% if result.placed %}alert-success pulse-success{% else %}alert-danger pulse-danger{% endif %} text-center p-3 mb-4 rounded-3 border-0">
                    <h2 class="m-0 fw-bold">
                        {% if result.placed %}
                            <i class="fa-solid fa-circle-check me-2"></i> High Probability of Placement!
                        {% else %}
                            <i class="fa-solid fa-triangle-exclamation me-2"></i> Risk of Non-Placement
                        {% endif %}
                    </h2>
                </div>

                <div class="mb-4">
                    <div class="d-flex justify-content-between mb-1">
                        <span>Placement Chance:</span>
                        <span class="fw-bold">{{ result.probability }}%</span>
                    </div>
                    <div class="progress bg-secondary" style="height: 15px; border-radius: 10px;">
                        <div class="progress-bar {% if result.probability >= 70 %}bg-success{% elif result.probability >= 40 %}bg-warning{% else %}bg-danger{% endif %}" 
                             role="progressbar" 
                             style="width: {{ result.probability }}%;" 
                             aria-valuenow="{{ result.probability }}" aria-valuemin="0" aria-valuemax="100"></div>
                    </div>
                </div>

                <div class="row g-3 mb-4">
                    <div class="col-md-6">
                        <div class="stat-badge">
                            <span class="d-block text-light opacity-85">Predicted Salary Tier</span>
                            <h4 class="text-warning m-0 mt-1"><i class="fa-solid fa-coins me-1"></i> {{ result.package }}</h4>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="stat-badge">
                            <span class="d-block text-light opacity-85">Market Readiness</span>
                            <h4 class="text-info m-0 mt-1"><i class="fa-solid fa-gauge-high me-1"></i> {{ result.readiness }}</h4>
                        </div>
                    </div>
                </div>

                <div class="p-3 glass-card mb-4" style="position: relative; height:250px;">
                    <canvas id="profileChart"></canvas>
                </div>

                <div class="alert alert-dark border-light mb-0">
                    <i class="fa-solid fa-lightbulb text-warning me-2"></i> <strong>Recommendation:</strong> {{ result.recommendation }}
                </div>
            </div>
            {% else %}
            <div class="glass-card p-5 h-100 d-flex flex-column justify-content-center align-items-center text-center">
                <i class="fa-solid fa-chart-line display-1 text-warning mb-3"></i>
                <h3>Ready to Predict</h3>
                <p class="text-light opacity-85">Enter your academic credentials and skill ratings on the left to view detailed insights and placement predictions.</p>
            </div>
            {% endif %}
        </div>
    </div>
</div>

{% if result %}
<script>
    const ctx = document.getElementById('profileChart').getContext('2d');
    new Chart(ctx, {
        type: 'radar',
        data: {
            labels: ['CGPA (Normalized)', 'Aptitude/IQ', 'Profile Score', 'Internships Factor'],
            datasets: [{
                label: 'Candidate Metrics',
                data: [
                    {{ (data.cgpa / 10) * 100 }},
                    {{ (data.iq / 160) * 100 }},
                    {{ data.profile }},
                    {{ (data.internships / 5) * 100 if data.internships <= 5 else 100 }}
                ],
                backgroundColor: 'rgba(255, 0, 127, 0.25)',
                borderColor: '#ff007f',
                pointBackgroundColor: '#f5af19',
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                r: {
                    angleLines: { color: 'rgba(255, 255, 255, 0.3)' },
                    grid: { color: 'rgba(255, 255, 255, 0.3)' },
                    pointLabels: { color: '#ffffff', font: { size: 12 } },
                    ticks: { display: false },
                    min: 0,
                    max: 100
                }
            },
            plugins: {
                legend: { display: false }
            }
        }
    });
</script>
{% endif %}

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    data = None

    if request.method == "POST":
        cgpa = float(request.form["cgpa"])
        iq = int(request.form["iq"])
        profile = int(request.form["profile"])
        internships = int(request.form["internships"])

        data = {
            "cgpa": cgpa,
            "iq": iq,
            "profile": profile,
            "internships": internships
        }

        # Dynamic Scoring Logic
        cgpa_score = (cgpa / 10.0) * 40
        iq_score = (iq / 160.0) * 20
        profile_score = (profile / 100.0) * 30
        internship_score = min(internships * 5, 10)

        probability = round(cgpa_score + iq_score + profile_score + internship_score, 1)
        placed = probability >= 65.0

        if probability >= 85:
            package = "Dream / Tier-1 (12+ LPA)"
            readiness = "Excellent"
        elif probability >= 65:
            package = "Core / Tier-2 (6-12 LPA)"
            readiness = "Good"
        elif probability >= 50:
            package = "Mass Recruiting (3.5-6 LPA)"
            readiness = "Moderate"
        else:
            package = "Needs Improvement"
            readiness = "Low"

        if cgpa < 7.0:
            recommendation = "Focus on raising your CGPA above 7.5 to satisfy minimum criteria for most recruiters."
        elif profile < 60:
            recommendation = "Build more real-world projects or earn industry certifications to boost your Profile Score."
        elif internships == 0:
            recommendation = "Try securing at least one internship or industrial training to enhance your practical exposure."
        else:
            recommendation = "Solid profile! Practice mock technical interviews and core coding problems to maintain consistency."

        result = {
            "placed": placed,
            "probability": probability,
            "package": package,
            "readiness": readiness,
            "recommendation": recommendation
        }

    return render_template_string(HTML, result=result, data=data)

if __name__ == "__main__":
    app.run(debug=True)