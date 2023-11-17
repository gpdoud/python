
results = {}

with open("./Ch08/testscores.dat") as f :
    for line in f :
        name, score = line.rstrip("\r\n").split(":")
        results[name] = int(score)

sum = 0
count = 0

results_with_grades = []

for name, score in results.items() :
    sum += score
    count += 1
    if score >= 95 and score <= 100:
        grade = "A"
    elif score >= 89 and score <= 94:
        grade = "B"
    elif score >= 83 and score <= 88:
        grade = "C"
    elif score >= 75 and score <= 82:
        grade = "D"
    else:
        grade = "F"
    results_with_grades.append((name, score, grade))

sorted_results_with_grade = sorted(results_with_grades, reverse=True, key=lambda e: e[1])

for name, score, grade in sorted_results_with_grade:
    print(f"{name:20s} {score} {grade}")

print(f"Average score is {sum / count}")