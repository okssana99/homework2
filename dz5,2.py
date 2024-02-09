students = {
    "Іванов Іван": ["Python", "FrontEnd"],
    "Петров Петро": ["FullStack", "Java"],
    "Сидорова Ольга": ["Python"],
    "Коваленко Марія": ["FullStack", "Java"],
    "Семенчук Андрій": ["Python", "Java"]
}

stud = {
    "multiple_groups": set(),
    "not_in_frontend": set(),
    "python_or_java": set()
}

for student, groups in students.items():
    if len(groups) >= 2:
        stud["multiple_groups"].add(student)
    if "FrontEnd" not in groups:
        stud["not_in_frontend"].add(student)
    if "Python" in groups or "Java" in groups:
        stud["python_or_java"].add(student)

multiple_groups = "Студенти, які навчаються у двох та більше групах: " + ', '.join(stud["multiple_groups"])
not_in_frontend = "Студенти, які не навчаються на фронтенді: " + ', '.join(stud["not_in_frontend"])
python_or_java = "Студенти, які вивчають Python або Java: " + ', '.join(stud["python_or_java"])

print(multiple_groups)
print(not_in_frontend)
print(python_or_java)