# ==========================================
# GRIDLOCK RECOMMENDATION ENGINE
# ==========================================

def generate_recommendation(
    priority,
    event_cause,
    zone,
    requires_road_closure
):

    recommendation = {
        "priority": priority,
        "zone": zone,
        "event_cause": event_cause,
        "alert_level": "Green",
        "response_team": [],
        "recommended_actions": [],
        "officers": 0,
        "barricades": 0,
        "impact_category": "Local Impact"
    }

    # ======================================
    # ALERT LEVEL
    # ======================================

    if priority == "High":
        recommendation["alert_level"] = "Red"
    else:
        recommendation["alert_level"] = "Yellow"

    # ======================================
    # RESOURCE ALLOCATION
    # ======================================

    if priority == "High":

        recommendation["officers"] = 8
        recommendation["barricades"] = 12
        recommendation["impact_category"] = "Zone-Level Impact"

    else:

        recommendation["officers"] = 3
        recommendation["barricades"] = 4
        recommendation["impact_category"] = "Local Impact"

    # ======================================
    # EVENT-SPECIFIC RESPONSE
    # ======================================

    if event_cause == "accident":

        recommendation["response_team"] = [
            "Traffic Police",
            "Emergency Services",
            "Ambulance Support"
        ]

        recommendation["recommended_actions"] += [
            "Secure accident scene",
            "Clear damaged vehicles",
            "Coordinate emergency response"
        ]

    elif event_cause == "vehicle_breakdown":

        recommendation["response_team"] = [
            "Traffic Police",
            "Tow Truck Unit"
        ]

        recommendation["recommended_actions"] += [
            "Dispatch tow truck",
            "Remove disabled vehicle",
            "Restore traffic flow"
        ]

    elif event_cause == "construction":

        recommendation["response_team"] = [
            "Road Maintenance Team",
            "Traffic Police"
        ]

        recommendation["recommended_actions"] += [
            "Deploy temporary traffic signs",
            "Monitor lane closures",
            "Guide vehicles to alternate routes"
        ]

    elif event_cause == "water_logging":

        recommendation["response_team"] = [
            "Municipal Drainage Team",
            "Traffic Police"
        ]

        recommendation["recommended_actions"] += [
            "Pump out water",
            "Inspect road conditions",
            "Divert traffic"
        ]

    elif event_cause == "congestion":

        recommendation["response_team"] = [
            "Traffic Monitoring Unit"
        ]

        recommendation["recommended_actions"] += [
            "Optimize signal timing",
            "Monitor congestion levels",
            "Issue traffic advisory"
        ]

    elif event_cause == "public_event":

        recommendation["response_team"] = [
            "Traffic Police",
            "Crowd Management Team"
        ]

        recommendation["recommended_actions"] += [
            "Deploy crowd barriers",
            "Control pedestrian crossings",
            "Manage event traffic flow"
        ]

    elif event_cause == "tree_fall":

        recommendation["response_team"] = [
            "Municipal Emergency Team",
            "Traffic Police"
        ]

        recommendation["recommended_actions"] += [
            "Remove fallen tree",
            "Inspect roadway",
            "Redirect traffic"
        ]

    else:

        recommendation["response_team"] = [
            "Traffic Monitoring Unit"
        ]

        recommendation["recommended_actions"] += [
            "Monitor situation",
            "Dispatch field team if required"
        ]

    # ======================================
    # ROAD CLOSURE RESPONSE
    # ======================================

    if requires_road_closure:

        recommendation["barricades"] += 4

        recommendation["recommended_actions"] += [
            "Activate diversion route",
            "Deploy road barricades",
            "Notify navigation services",
            "Issue public traffic advisory"
        ]

    # ======================================
    # HIGH PRIORITY ESCALATION
    # ======================================

    if priority == "High":

        recommendation["recommended_actions"] += [
            "Dispatch rapid response team",
            "Increase signal monitoring",
            "Escalate to traffic control center"
        ]

    return recommendation


# ==========================================
# TEST
# ==========================================

if __name__ == "__main__":

    result = generate_recommendation(
        priority="High",
        event_cause="accident",
        zone="Central Zone 2",
        requires_road_closure=True
    )

    print("\n===== GRIDLOCK RECOMMENDATION =====\n")

    for key, value in result.items():
        print(f"{key}: {value}")
