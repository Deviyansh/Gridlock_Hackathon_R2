import pickle
import pandas as pd
from pathlib import Path

# ==========================================
# LOAD MODEL & RISK MAPS
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "event_model.pkl"
RISK_MAP_PATH = BASE_DIR / "models" / "risk_maps.pkl"

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

with open(RISK_MAP_PATH, "rb") as f:
    risk_maps = pickle.load(f)

zone_risk_map = risk_maps["zone_risk"]
cause_risk_map = risk_maps["cause_risk"]
hour_risk_map = risk_maps["hour_risk"]

# ==========================================
# HELPER FUNCTIONS
# ==========================================

def get_average_risk(risk_map):
    return sum(risk_map.values()) / len(risk_map)

# ==========================================
# PREDICTION FUNCTION
# ==========================================

def predict_priority(
    event_type,
    event_cause,
    zone,
    requires_road_closure,
    hour,
    weekday
):

    # --------------------------------------
    # Risk Feature Engineering
    # --------------------------------------

    zone_risk = zone_risk_map.get(
        zone,
        get_average_risk(zone_risk_map)
    )

    cause_risk = cause_risk_map.get(
        event_cause,
        get_average_risk(cause_risk_map)
    )

    hour_risk = hour_risk_map.get(
        hour,
        get_average_risk(hour_risk_map)
    )

    # --------------------------------------
    # Create Input Data
    # --------------------------------------

    input_df = pd.DataFrame([{
        "event_type": event_type,
        "event_cause": event_cause,
        "zone": zone,
        "requires_road_closure": requires_road_closure,
        "hour": hour,
        "weekday": weekday,
        "zone_risk": zone_risk,
        "cause_risk": cause_risk,
        "hour_risk": hour_risk
    }])

    # --------------------------------------
    # Predict
    # --------------------------------------

    prediction = model.predict(input_df)[0]

    probabilities = model.predict_proba(input_df)[0]

    confidence = float(max(probabilities))

    priority = "High" if prediction == 1 else "Low"

    return priority, confidence


# ==========================================
# TEST
# ==========================================

if __name__ == "__main__":

    priority, confidence = predict_priority(
        event_type="unplanned",
        event_cause="accident",
        zone="Central Zone 2",
        requires_road_closure=True,
        hour=18,
        weekday="Monday"
    )

    print("\n===== GRIDLOCK PREDICTION =====")
    print("Priority  :", priority)
    print("Confidence:", round(confidence * 100, 2), "%")
