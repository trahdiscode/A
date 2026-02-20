def analyze_student(row):
    subjects = ["Maths", "DS", "Physics"]

    scores = [row[sub] for sub in subjects]
    avg = sum(scores) / len(scores)

    strong = subjects[scores.index(max(scores))]
    weak = subjects[scores.index(min(scores))]

    gaps = {sub: row[sub] - avg for sub in subjects}

    return {
        "Average": round(avg, 2),
        "Strong": strong,
        "Weak": weak,
        "Gaps": gaps
    }
