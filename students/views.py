from django.shortcuts import render

# Fake data — no database, no ORM
STUDENTS = [
    {"id": 1, "name": "Arun", "age": 20},
    {"id": 2, "name": "Priya", "age": 21},
    {"id": 3, "name": "Vishal", "age": 22},
]

def students_list(request):
    return render(request, 'students/list.html', {"students": STUDENTS})
