import numpy as np

data_type = [('name', 'S15'), ('Grade', int), ('Height', float)]
student_details = [
    ('John', 12, 159.3),
    ('Emma', 11, 162.6),
    ('Aryan', 13, 172.5)
]

student_array = np.array(student_details, dtype=data_type)
print(f"Original array: {student_array}")

sorted_array = np.sort(student_array, order="Height")
print("Sorted by height (ascending):", sorted_array)
