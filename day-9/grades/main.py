scores = {
    "Alice": 92,
    "Bob": 76,
    "Charlie": 88,
    "Diana": 95,
    "Ethan": 67,
    "Fiona": 81,
    "George": 73,
    "Hannah": 99,
    "Ian": 84,
    "Jasmine": 90,
    "Kevin": 62,
    "Laura": 78,
    "Michael": 85,
    "Nina": 91,
    "Oscar": 69,
    "Paula": 87,
    "Quentin": 80,
    "Rachel": 94,
    "Sam": 71,
    "Tina": 89
}

for _ in scores:
    if scores[_] >= 91:
        scores[_] = "Outstanding"
    elif scores[_] >= 81:
        scores[_] = "Exceeds Expectations"
    elif scores[_] >= 71:
        scores[_] = "Acceptable"
    elif scores[_] <= 70:
        scores[_] = "Fail"

print(scores)