import numpy as np
import random
from numpy.random import default_rng
from tabulate import tabulate


students = []
first = ['ვენერა', 'თინა', 'თეა', 'სოსო', 'მირანდა', 'ჟენია', 'ტატიანა', 'ედუარდ', 'კლარა', 'სიმონ', 'ანზორ', 'სოფია',
         'სოსო', 'ნელი', 'ბონდო', 'ედუარდ', 'სონია', 'არჩილ', 'მარიამ', 'სოფია', 'ემა', 'იზოლდა', 'ომარ', 'ტატიანა',
         'ვიქტორ', 'კარინე', 'გუგული', 'კახა', 'როზა', 'რუსუდან', 'სიმონ', 'ნელი', 'ბადრი', 'მადონა', 'ირინე', 'მინდია',
         'ნათია', 'გულნარა', 'კახა', 'ელზა', 'როინ', 'ნაირა', 'ლიანა', 'ნინელი', 'მაყვალა', 'რეზო', 'ჟუჟუნა', 'ზინა',
         'გოჩა', 'მურმან']

last = ['ქუთათელაძე', 'მეგრელიშვილი', 'სალუქვაძე', 'ხარაიშვილი', 'შელია', 'კევლიშვილი', 'ბუჩუკური', 'ტყებუჩავა',
        'მიქაბერიძე', 'ურუშაძე', 'ძიძიგური', 'გოგუაძე', 'ანთაძე', 'ვალიევა', 'როგავა', 'ნაკაშიძე', 'ღურწკაია',
        'გვაზავა', 'გვასალია', 'ზარანდია', 'სხირტლაძე', 'ბერაძე', 'ხვიჩია', 'ბასილაშვილი', 'კაკაბაძე', 'მერებაშვილი',
        'ნოზაძე',  'ხარაბაძე', 'მუსაევა', 'მამულაშვილი', 'ელიზბარაშვილი', 'მამულაშვილი', 'ჯოჯუა', 'გულუა', 'ხალვაში',
        'ხარატიშვილი', 'დუმბაძე', 'ბერიანიძე', 'ჯოხაძე', 'სამხარაძე', 'ლიპარტელიანი', 'იობიძე', 'გაბაიძე', 'ხარაბაძე',
        'ინასარიძე', 'ბერაძე', 'შენგელია', 'ქობალია', 'მიქავა', 'რევაზიშვილი']
for i in range(100):
    students.append(random.choice(first) + " " + random.choice(last))

subjects = ["Name", "Maths", "English", "History", "Biology", "Logic"]

# Create an empty 2D array to store the grades
num_students = len(students)
num_subjects = len(subjects)
grades_matrix = np.empty((num_students + 1, num_subjects), dtype=object)


# Assign student names and subject names to the matrix
grades_matrix[0] = subjects
grades_matrix[1:, 0] = students

# Fill in the grades for each subject
grades = (default_rng().random((100, 5)) * 100).round()
grades_matrix[1:, 1:] = grades  # Skip the first element of grades (name)

# Print the matrix

print(tabulate(grades_matrix))
average_row = np.mean(grades, axis=1)
print("---------")
highest_average = np.max(average_row)
index = np.argmax(average_row) + 1

print(f"The student with the highest average grade in all subjects: {highest_average}: {grades_matrix[index]}")
print("---------")
maths = grades_matrix[1:, 1]
max_maths = np.max(maths)
min_maths = np.min(maths)
math_max_index = np.argmax(maths) + 1
math_min_index = np.argmin(maths) + 1
print(f"Highest grade in maths {max_maths} {grades_matrix[math_max_index]}")
print(f"Lowest grade in maths {min_maths} {grades_matrix[math_min_index]}")

print("---------")
average_english_grade = np.mean(grades_matrix[1:, 1])
comp = grades_matrix[1:]
higher_than_average = comp[grades_matrix[1:, 2] > average_english_grade]
print("Students with higher than average grades in English")
print(higher_than_average[:, 0])
