"""Sample data for the Individual Performance Report MVP."""

report_data = {
    "client_logo_text": "Academy",
    "provider_logo_text": "PST",
    "report_title": "Individual Performance Report - Batch U17",
    "date": "23 July 2026",
    "program_name": "U17 Development Program",
    "athlete_name": "Priya Sharma",
    "gender": "Female",
    "dob": "12 Mar 2010",
    "age_group": "15-17 Years",
    "academy_name": "Riverside Sports Academy",
    "sport": "Athletics",
    "position_role": "Sprinter",
    "coach_name": "Arjun Mehta",

    "power": {
        "cmj": {"turn1": 31.2, "turn2": 29.8, "best": 31.2},
        "broad_jump": {"turn1": 198.0, "turn2": 202.0, "best": 202.0},
    },
    "agility": {
        "illinois_time": 16.42,
        "arrowhead": {"left": 9.1, "right": 8.9, "best_direction": "Right",
                      "difference": 0.2, "asymmetry_pct": 2.2, "total_time": 18.0},
        "norms": [
            {"category": "Excellent", "range": "< 16.0", "rating": 5},
            {"category": "Very Good", "range": "16.0 - 17.0", "rating": 4, "highlight": True},
            {"category": "Good", "range": "17.0 - 18.0", "rating": 3},
            {"category": "Moderate", "range": "18.0 - 19.0", "rating": 2},
            {"category": "Low", "range": "19.0 - 20.0", "rating": 1},
            {"category": "Poor", "range": "> 20.0", "rating": 0},
        ],
    },
    "speed": {
        "sprint_30m": {"time": 4.62, "velocity": 23.4},
        "splits": [
            {"split": 0, "t1": 0.0, "t2": 0.0, "t3": 0.0, "avg": 0.0, "min": 0.0, "max": 0.0},
            {"split": 10, "t1": 2.01, "t2": 1.98, "t3": 2.02, "avg": 2.00, "min": 1.98, "max": 2.02},
            {"split": 20, "t1": 3.35, "t2": 3.30, "t3": 3.38, "avg": 3.34, "min": 3.30, "max": 3.38},
            {"split": 30, "t1": 4.65, "t2": 4.62, "t3": 4.70, "avg": 4.66, "min": 4.62, "max": 4.70},
        ],
        "rsa": {
            "turns": 5, "avg_time": 4.71, "best_time": 4.62, "slowest_time": 4.85,
            "total_time": 23.55, "ideal_total": 23.10, "decrement_pct": 1.9, "fatigue_index": 1.6,
        },
    },
    "radar": {
        "labels": ["Power (Jump)", "Power (Broad Jump)", "Agility", "Acceleration", "Sprint Ability", "Endurance (RSA)"],
        "scores": [4, 4, 4, 5, 4, 4],  # 0-5 rating scale, matches norm tables
    },

    "notes": {
        "power": "Good improvement in broad jump on second attempt.",
        "agility": "Slight right-side dominance noted, within normal range.",
        "speed": "Consistent split times, low fatigue index.",
    },
}
