import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from app.predictor import predict_priority
from app.recommender import generate_recommendation

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Gridlock Traffic Management System",
    page_icon="🚦",
    layout="wide"
)

# ==========================================
# HEADER
# ==========================================

st.title("🚦 Gridlock Traffic Management System")

st.info(
    """
    AI-Powered Event Traffic Impact Management Platform

    Features:
    • Event Priority Prediction
    • Traffic Risk Assessment
    • Resource Allocation Planning
    • Response Team Recommendation
    • Traffic Impact Estimation
    • Incident Management Support
    """
)

# ==========================================
# COMMAND CENTER SUMMARY
# ==========================================

st.header("🚨 Traffic Command Center Overview")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Events", "8,173")
c2.metric("High Priority Events", "5,030")
c3.metric("Road Closures", "676")
c4.metric("Peak Hour", "9 PM")

st.markdown("---")

# ==========================================
# INPUT SECTION
# ==========================================

st.header("📋 Event Details")

col1, col2 = st.columns(2)

with col1:

    event_type = st.selectbox(
        "Event Type",
        ["planned", "unplanned"]
    )

    event_cause = st.selectbox(
        "Event Cause",
        [
            "accident",
            "vehicle_breakdown",
            "construction",
            "water_logging",
            "public_event",
            "congestion",
            "tree_fall",
            "road_conditions",
            "others"
        ]
    )

    zone = st.selectbox(
        "Zone",
        [
            "Central Zone 1",
            "Central Zone 2",
            "North Zone 1",
            "North Zone 2",
            "South Zone 1",
            "South Zone 2",
            "East Zone 1",
            "East Zone 2",
            "West Zone 1",
            "West Zone 2"
        ]
    )

with col2:

    requires_road_closure = st.checkbox(
        "Requires Road Closure"
    )

    hour = st.slider(
        "Hour",
        0,
        23,
        12
    )

    weekday = st.selectbox(
        "Weekday",
        [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
        ]
    )

# ==========================================
# ANALYZE
# ==========================================

if st.button("🚀 Analyze Event"):

    priority, confidence = predict_priority(
        event_type=event_type,
        event_cause=event_cause,
        zone=zone,
        requires_road_closure=requires_road_closure,
        hour=hour,
        weekday=weekday
    )

    recommendation = generate_recommendation(
        priority=priority,
        event_cause=event_cause,
        zone=zone,
        requires_road_closure=requires_road_closure
    )

    st.markdown("---")

    # ======================================
    # KPI CARDS
    # ======================================

    st.header("📊 Incident Assessment")

    k1, k2, k3 = st.columns(3)

    k1.metric(
        "Priority",
        priority
    )

    k2.metric(
        "Confidence",
        f"{confidence*100:.1f}%"
    )

    k3.metric(
        "Alert Level",
        recommendation["alert_level"]
    )

    # ======================================
    # SEVERITY SCORE
    # ======================================

    severity_score = int(confidence * 100)

    st.header("⚠️ Severity Assessment")

    st.progress(severity_score / 100)

    st.write(
        f"Severity Score: {severity_score}/100"
    )

    if severity_score >= 80:
        st.error("🔴 Critical Risk")

    elif severity_score >= 60:
        st.warning("🟠 High Risk")

    elif severity_score >= 40:
        st.info("🟡 Medium Risk")

    else:
        st.success("🟢 Low Risk")

    # ======================================
    # IMPACT SCORE
    # ======================================

    impact_score = severity_score

    st.header("🌐 Traffic Impact Estimate")

    "Impact Level"

    if impact_score >= 80:
        st.error("🔴 City-Level Impact")

    elif impact_score >= 60:
        st.warning("🟡 Zone-Level Impact")

    else:
        st.success("🟢 Local Impact")

    # ======================================
    # RESOURCE ALLOCATION
    # ======================================

    st.header("🚔 Resource Allocation")

    r1, r2 = st.columns(2)

    r1.metric(
        "Traffic Officers",
        recommendation["officers"]
    )

    r2.metric(
        "Barricades",
        recommendation["barricades"]
    )

    # ======================================
    # EXPLAINABLE AI
    # ======================================

    st.header("🧠 Why This Prediction?")

    reasons = []

    if requires_road_closure:
        reasons.append(
            "Road closure required"
        )

    if event_type == "unplanned":
        reasons.append(
            "Unexpected traffic disruption"
        )

    if event_cause in [
        "accident",
        "vehicle_breakdown",
        "construction"
    ]:
        reasons.append(
            f"Critical event cause: {event_cause}"
        )

    if hour in [7, 8, 9, 17, 18, 19, 20]:
        reasons.append(
            "Peak traffic hour"
        )

    if not reasons:
        reasons.append(
            "Standard operating conditions"
        )

    for reason in reasons:
        st.write("•", reason)

    # ======================================
    # RESPONSE TEAM
    # ======================================

    st.header("👮 Recommended Response Team")

    for team in recommendation["response_team"]:
        st.info(team)

    # ======================================
    # ACTIONS
    # ======================================

    st.header("✅ Recommended Actions")

    for action in recommendation["recommended_actions"]:
        st.success(action)

# ==========================================
# ANALYTICS
# ==========================================

st.markdown("---")

st.header("📈 Historical Traffic Insights")

left, right = st.columns(2)

with left:

    st.subheader("Top Event Causes")

    causes = pd.DataFrame({
        "Cause": [
            "Vehicle Breakdown",
            "Construction",
            "Water Logging",
            "Accident"
        ],
        "Count": [
            4896,
            480,
            458,
            365
        ]
    })

    st.bar_chart(
        causes.set_index("Cause")
    )

with right:

    st.subheader("Peak Incident Hours")

    peak_hours = pd.DataFrame({
        "Hour": [
            "5 AM",
            "6 AM",
            "8 PM",
            "9 PM"
        ],
        "Events": [
            661,
            660,
            681,
            810
        ]
    })

    st.bar_chart(
        peak_hours.set_index("Hour")
    )


# ==========================================
# LIVE TRAFFIC OPERATIONS CENTER
# ==========================================

st.markdown("---")

st.header("🚦 Live Traffic Operations Center")

live_data = pd.DataFrame({
    "Zone": [
        "Central Bengaluru",
        "North Bengaluru",
        "South Bengaluru",
        "East Bengaluru",
        "West Bengaluru"
    ],
    "Status": [
        "🟡 Moderate",
        "🔴 Congested",
        "🟢 Normal",
        "🟡 Moderate",
        "🟢 Normal"
    ],
    "Active Incidents": [
        5,
        8,
        2,
        4,
        1
    ]
})

st.dataframe(
    live_data,
    use_container_width=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Active Incidents", "16")

with col2:
    st.metric("Road Closures", "4")

with col3:
    st.metric("Traffic Units Deployed", "22")

with col4:
    st.metric("Avg Response Time", "11 min")

# ==========================================
# SMART TRAFFIC MAP
# ==========================================

st.markdown("---")

st.header("🗺️ Bengaluru Smart Traffic Map")

m = folium.Map(
    location=[12.9716, 77.5946],  # Bengaluru
    zoom_start=11
)

# Central Bengaluru (MG Road)
folium.Marker(
    [12.9755, 77.6068],
    popup="Central Zone",
    icon=folium.Icon(color="orange")
).add_to(m)

# North Bengaluru (Hebbal)
folium.Marker(
    [13.0358, 77.5970],
    popup="North Zone",
    icon=folium.Icon(color="red")
).add_to(m)

# South Bengaluru (Jayanagar)
folium.Marker(
    [12.9250, 77.5938],
    popup="South Zone",
    icon=folium.Icon(color="green")
).add_to(m)

# East Bengaluru (Whitefield)
folium.Marker(
    [12.9698, 77.7499],
    popup="East Zone",
    icon=folium.Icon(color="orange")
).add_to(m)

# West Bengaluru (Rajajinagar)
folium.Marker(
    [12.9916, 77.5553],
    popup="West Zone",
    icon=folium.Icon(color="green")
).add_to(m)

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.caption(
    "- Developed by Deviyansh Rajpurohit "
)
