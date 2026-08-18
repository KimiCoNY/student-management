students = [
    {"id": 1, "name": "Nguyen Van A", "email": "a@example.com"},
    {"id": 2, "name": "Tran Thi B", "email": "b@example.com"}
]

def get_students():
    return students

def get_student(student_id):
    for student in students:
        if student["id"] == student_id:
            return student
    return None

if __name__ == "__main__":
    print(get_students())

def search_students(keyword):
    result = []
    for student in students:
        if keyword.lower() in student["name"].lower():
            result.append(student)
    return result

print(search_students("Nguyen"))

