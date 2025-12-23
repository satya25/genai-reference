import pandas as pd

# Sample in-memory data for demo
STUDENT_DATA = pd.DataFrame([
    {"student_id": 101, "course": "Math", "score": 85, "timetable": "Mon 10AM"},
    {"student_id": 102, "course": "CS", "score": 90, "timetable": "Tue 2PM"},
    {"student_id": 103, "course": "Physics", "score": 78, "timetable": "Wed 11AM"},
])

def fetch_from_db(query: str) -> str:
    """
    Minimal DB fetch simulation
    """
    if "score" in query:
        return "\n".join([f"{row['course']}: {row['score']}" for _, row in STUDENT_DATA.iterrows()])
    elif "timetable" in query:
        return "\n".join([f"{row['course']}: {row['timetable']}" for _, row in STUDENT_DATA.iterrows()])
    else:
        return "No matching data found in DB."
