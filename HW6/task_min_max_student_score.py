students_score = {
    "Ivan": 5.00,
    "Alex": 3.50,
    "Maria": 5.50,
    "Georgy": 5.00
}

for key, v in students_score.items():
    if v == max(students_score.values()):
        print(f"{key} - {v}")

for key, v in students_score.items():
    if v == min(students_score.values()):
        print(f"{key} - {v}")