students_score = {
    "Ivan": 5.00,
    "Alex": 3.50,
    "Maria": 5.50,
    "Georgy": 5.00
}

best_student_score = {name: score for name, score in students_score.items() if score > 4.00}
for name, score in best_student_score.items():
    print(f"{name:<8} - {score:.2f}")