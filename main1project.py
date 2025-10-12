import numpy as np

# Subjects and student names
subjects = ['Math', 'Physics', 'Chemistry', 'ICT', 'English']
students = ['John', 'Emma', 'Aryan', 'Sophia', 'Liam', 'Olivia']

scores = np.array([
    [85, 92, 78, 90, 88],
    [76, 85, 83, 80, 79],
    [90, 88, 92, 95, 91],
    [65, 70, 68, 72, 66],
    [88, 84, 82, 86, 85],
    [79, 75, 80, 78, 77]
])

print("Original Scores:")
for student, student_scores in zip(students, scores):
    print(f"{student}: " + "  ".join(str(s) for s in student_scores))
print("\n")

avg_per_student = np.mean(scores, axis=1)
avg_per_subject = np.mean(scores, axis=0)
highest_score = np.max(scores)
lowest_score = np.min(scores)
total_per_student = np.sum(scores, axis=1)

print("Average score per student:")
for student, avg in zip(students, avg_per_student):
    print(f"{student}: {avg:.2f}")

print("\nAverage score per subject:")
for subject, avg in zip(subjects, avg_per_subject):
    print(f"{subject}: {avg:.2f}")

print(f"\nHighest score: {highest_score}")
print(f"Lowest score: {lowest_score}\n")

print("Total score per student:")
for student, total in zip(students, total_per_student):
    print(f"{student}: {total}")
print("\n")

scores_bonus = scores + 5
print("Scores after 5 bonus marks:")
for student, student_scores in zip(students, scores_bonus):
    print(f"{student}: " + "  ".join(str(s) for s in student_scores))
print("\n")

scores_increase = np.round(scores * 1.1, 1)
print("Scores after 10% increase:")
for student, student_scores in zip(students, scores_increase):
    print(f"{student}: " + "  ".join(str(s) for s in student_scores))
print("\n")

sorted_scores = np.sort(scores, axis=1)
print("Sorted scores per student:")
for student, student_scores in zip(students, sorted_scores):
    print(f"{student}: " + "  ".join(str(s) for s in student_scores))
print("\n")

random_scores = np.random.randint(50, 101, size=(5,4))
random_students = ['Alex', 'Mia', 'Noah', 'Isabella', 'Ethan']
random_subjects = ['Math', 'Physics', 'Chemistry', 'ICT']

print("Randomly generated scores:")
for student, student_scores in zip(random_students, random_scores):
    print(f"{student}: " + "  ".join(str(s) for s in student_scores))
