import pickle
from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st

# ---------------------------------------------------------
# Facebook Live Sellers - Interactive K-Means Dashboard
# Uses the supplied model.pkl and scaler.pkl.
# ---------------------------------------------------------

st.set_page_config(
    page_title="Facebook Live Cluster Explorer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "model.pkl"
SCALER_PATH = BASE_DIR / "scaler.pkl"

FEATURES = [
    "status_type",
    "num_reactions",
    "num_comments",
    "num_shares",
    "num_likes",
    "num_loves",
    "num_wows",
    "num_hahas",
    "num_sads",
    "num_angrys",
]

STATUS_MAP = {
    "link": 0,
    "photo": 1,
    "status": 2,
    "video": 3,
}

# Maximum values represented by the supplied scaler.
MAX_VALUES = {
    "num_reactions": 4710,
    "num_comments": 20990,
    "num_shares": 3424,
    "num_likes": 4710,
    "num_loves": 657,
    "num_wows": 278,
    "num_hahas": 157,
    "num_sads": 51,
    "num_angrys": 31,
}


@st.cache_resource
def load_artifacts():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Missing {MODEL_PATH.name}")
    if not SCALER_PATH.exists():
        raise FileNotFoundError(f"Missing {SCALER_PATH.name}")

    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)

    with open(SCALER_PATH, "rb") as f:
        scaler = pickle.load(f)

    return model, scaler


def predict_cluster(values, model, scaler):
    raw = np.array([values], dtype=float)
    scaled = scaler.transform(raw)
    prediction = int(model.predict(scaled)[0])
    distances = model.transform(scaled)[0]
    return prediction, scaled[0], distances


def cluster_profile(model, scaler):
    """Return the original-scale values represented by each cluster centroid."""
    centers = scaler.inverse_transform(model.cluster_centers_)
    rows = []
    for cluster_id, center in enumerate(centers):
        row = {"Cluster": f"Cluster {cluster_id}"}
        row.update(dict(zip(FEATURES, center)))
        rows.append(row)
    return pd.DataFrame(rows)


def set_example(name):
    examples = {
        "Low engagement": {
            "status": "photo",
            "reactions": 30,
            "comments": 3,
            "shares": 1,
            "likes": 25,
            "loves": 2,
            "wows": 0,
            "hahas": 0,
            "sads": 0,
            "angrys": 0,
        },
        "Typical video": {
            "status": "video",
            "reactions": 529,
            "comments": 512,
            "shares": 262,
            "likes": 432,
            "loves": 92,
            "wows": 3,
            "hahas": 1,
            "sads": 1,
            "angrys": 0,
        },
        "High comments": {
            "status": "video",
            "reactions": 1500,
            "comments": 5000,
            "shares": 500,
            "likes": 1100,
            "loves": 250,
            "wows": 30,
            "hahas": 20,
            "sads": 5,
            "angrys": 2,
        },
    }

    ex = examples[name]
    for key, value in ex.items():
        st.session_state[key] = value


# -----------------------------
# Load model
# -----------------------------
try:
    model, scaler = load_artifacts()
except Exception as exc:
    st.error(f"Could not load the model files: {exc}")
    st.stop()


# -----------------------------
# Styling
# -----------------------------
st.markdown(
    """
    <style>
    .main-title {
        font-size: 2.4rem;
        font-weight: 800;
        margin-bottom: 0.2rem;
    }
    .subtitle {
        color: #667085;
        font-size: 1.05rem;
        margin-bottom: 1.2rem;
    }
    .prediction-box {
        padding: 1.2rem;
        border-radius: 16px;
        background: linear-gradient(135deg, #eef4ff, #f8faff);
        border: 1px solid #dbe5ff;
        text-align: center;
    }
    .prediction-number {
        font-size: 2.5rem;
        font-weight: 800;
    }
    .small-note {
        color: #667085;
        font-size: 0.9rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="main-title">📊 Facebook Live Cluster Explorer</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Interactively explore the supplied K-Means model and predict the cluster of a Facebook Live post.</div>',
    unsafe_allow_html=True,
)

# -----------------------------
# Sidebar controls
# -----------------------------
with st.sidebar:
    st.header("🎛️ Post inputs")
    st.caption("Change any value and the prediction updates immediately.")

    example = st.selectbox(
        "Quick example",
        ["Custom", "Low engagement", "Typical video", "High comments"],
    )

    if "last_example" not in st.session_state:
        st.session_state.last_example = "Custom"

    if example != "Custom" and example != st.session_state.last_example:
        set_example(example)
    st.session_state.last_example = example

    status = st.selectbox(
        "Status type",
        list(STATUS_MAP.keys()),
        index=3 if "status" not in st.session_state else list(STATUS_MAP.keys()).index(
            st.session_state.status
        ),
        key="status",
    )

    st.markdown("**Engagement**")

    reactions = st.number_input(
        "Reactions",
        min_value=0,
        max_value=MAX_VALUES["num_reactions"],
        value=st.session_state.get("reactions", 529),
        step=1,
        key="reactions",
    )
    comments = st.number_input(
        "Comments",
        min_value=0,
        max_value=MAX_VALUES["num_comments"],
        value=st.session_state.get("comments", 512),
        step=1,
        key="comments",
    )
    shares = st.number_input(
        "Shares",
        min_value=0,
        max_value=MAX_VALUES["num_shares"],
        value=st.session_state.get("shares", 262),
        step=1,
        key="shares",
    )

    st.markdown("**Reaction types**")

    likes = st.number_input(
        "Likes",
        min_value=0,
        max_value=MAX_VALUES["num_likes"],
        value=st.session_state.get("likes", 432),
        step=1,
        key="likes",
    )
    loves = st.number_input(
        "Loves",
        min_value=0,
        max_value=MAX_VALUES["num_loves"],
        value=st.session_state.get("loves", 92),
        step=1,
        key="loves",
    )
    wows = st.number_input(
        "Wows",
        min_value=0,
        max_value=MAX_VALUES["num_wows"],
        value=st.session_state.get("wows", 3),
        step=1,
        key="wows",
    )
    hahas = st.number_input(
        "Hahas",
        min_value=0,
        max_value=MAX_VALUES["num_hahas"],
        value=st.session_state.get("hahas", 1),
        step=1,
        key="hahas",
    )
    sads = st.number_input(
        "Sads",
        min_value=0,
        max_value=MAX_VALUES["num_sads"],
        value=st.session_state.get("sads", 1),
        step=1,
        key="sads",
    )
    angrys = st.number_input(
        "Angrys",
        min_value=0,
        max_value=MAX_VALUES["num_angrys"],
        value=st.session_state.get("angrys", 0),
        step=1,
        key="angrys",
    )

values = [
    STATUS_MAP[status],
    reactions,
    comments,
    shares,
    likes,
    loves,
    wows,
    hahas,
    sads,
    angrys,
]

prediction, scaled_values, distances = predict_cluster(values, model, scaler)

# -----------------------------
# Main result
# -----------------------------
left, right = st.columns([1.05, 1.5])

with left:
    st.markdown(
        f"""
        <div class="prediction-box">
            <div class="small-note">Predicted cluster</div>
            <div class="prediction-number">Cluster {prediction}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.metric("Closest centroid distance", f"{distances[prediction]:.4f}")

    other_cluster = 1 - prediction if len(distances) == 2 else None
    if other_cluster is not None:
        margin = distances[other_cluster] - distances[prediction]
        st.metric("Distance margin", f"{margin:.4f}")

with right:
    st.subheader("📏 Distance to each cluster")
    distance_df = pd.DataFrame(
        {
            "Cluster": [f"Cluster {i}" for i in range(len(distances))],
            "Distance": distances,
        }
    ).set_index("Cluster")

    st.bar_chart(distance_df, height=240)
    st.caption("The model assigns the post to the cluster with the smallest distance.")

# -----------------------------
# Tabs
# -----------------------------
tab1, tab2, tab3 = st.tabs(["🔎 Prediction details", "🧩 Cluster profiles", "📚 About the model"])

with tab1:
    st.subheader("Input summary")

    input_df = pd.DataFrame(
        {
            "Feature": FEATURES,
            "Value": values,
            "Scaled value": scaled_values,
        }
    )

    st.dataframe(
        input_df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Scaled value": st.column_config.NumberColumn(format="%.4f"),
        },
    )

    st.subheader("📈 Your engagement profile")

    chart_df = pd.DataFrame(
        {"Value": values[1:]},
        index=[
            "Reactions",
            "Comments",
            "Shares",
            "Likes",
            "Loves",
            "Wows",
            "Hahas",
            "Sads",
            "Angrys",
        ],
    )
    st.bar_chart(chart_df, height=350)

with tab2:
    st.subheader("Cluster profiles in original units")

    profiles = cluster_profile(model, scaler)

    display_profiles = profiles.copy()
    for col in FEATURES[1:]:
        display_profiles[col] = display_profiles[col].round(2)

    st.dataframe(
        display_profiles,
        use_container_width=True,
        hide_index=True,
    )

    st.subheader("Scaled centroid comparison")

    centroid_df = pd.DataFrame(
        model.cluster_centers_,
        index=[f"Cluster {i}" for i in range(model.n_clusters)],
        columns=FEATURES,
    )

    st.bar_chart(centroid_df.T, height=420)

    st.caption(
        "Centroids above are shown in the scaled feature space used by K-Means."
    )

with tab3:
    st.subheader("Model information")

    c1, c2, c3 = st.columns(3)
    c1.metric("Algorithm", "K-Means")
    c2.metric("Clusters", str(model.n_clusters))
    c3.metric("Features", str(model.n_features_in_))

    st.markdown("### Feature order")
    st.code(", ".join(FEATURES))

    st.markdown("### Preprocessing")
    st.write(
        "The supplied pipeline represents status_type as numeric labels "
        "(link=0, photo=1, status=2, video=3), then applies the supplied "
        "MinMaxScaler before K-Means prediction."
    )

    st.markdown("### Current post")
    st.write(
        f"Status type: **{status}**  \n"
        f"Predicted cluster: **Cluster {prediction}**"
    )

    st.warning(
        "Cluster numbers are model labels. They do not inherently mean "
        '"good", "bad", "high", or "low" engagement.'
    )

# -----------------------------
# Footer
# -----------------------------
st.divider()
st.caption(
    "Interactive dashboard built around the supplied model.pkl and scaler.pkl. "
    "Keep all three files in the same directory when running Streamlit."
)
