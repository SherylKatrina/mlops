
    students = [
    {"id": 101, "name": "Rahul"},
    {"id": 102, "name": "Anita"}
    ]

    def search_student(student_id):

    for student in students:
        if student["id"] == student_id:
            return student

    return "Student not found"

