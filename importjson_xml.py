import json
import xml.etree.ElementTree as ET

# Зчитуємо дані з файлу JSON
with open('1.json', 'r') as f:
    data = json.load(f)

# Отримуємо список студентів
students = data['students']

# Створюємо заголовок таблиці
print('{:<10} {:<10} {:<10} {:<20}'.format('First Name', 'Last Name', 'Group', 'Grades'))

# Друкуємо рядки таблиці для кожного студента
for student in students:
    first_name = student['first_name']
    last_name = student['last_name']
    group = student['group']
    grades = student['grades']
    grades_str = ', '.join(str(grade) for grade in grades)
    print('{:<10} {:<10} {:<10} {:<20}'.format(first_name, last_name, group, grades_str))

# Зчитуємо дані з файлу XML
tree = ET.parse('1.xml')
root = tree.getroot()

# Отримуємо список студентів
students = root.findall('student')

# Створюємо заголовок таблиці
print('{:<10} {:<10} {:<10} {:<20}'.format('First Name', 'Last Name', 'Group', 'Grades'))

# Друкуємо рядки таблиці для кожного студента
for student in students:
    first_name = student.find('first_name').text
    last_name = student.find('last_name').text
    group = student.find('group').text
    grades = student.findall('grades/grade')
    grades_str = ', '.join(grade.text for grade in grades)
    print('{:<10} {:<10} {:<10} {:<20}'.format(first_name, last_name, group, grades_str))
