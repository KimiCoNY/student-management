from app import get_students, get_student, search_students

def test_get_students():
    students = get_students()
    assert len(students) >= 2

def test_get_student_found():
    student = get_student(1)
    assert student is not None
    assert student["name"] == "Nguyen Van A"

def test_get_student_not_found():
    student = get_student(999)
    assert student is None

# Test: Tìm thấy sinh viên
def test_search_student_found():
    result = search_students("Nguyen")
    assert len(result) > 0
    assert result[0]["name"] == "Nguyen Van A"

# Test: Không tìm thấy sinh viên
def test_search_student_not_found():
    result = search_students("KhongTonTai")
    assert len(result) == 0

# Test: Tìm kiếm không phân biệt hoa/thường
def test_search_student_case_insensitive():
    result = search_students("nguyen")
    assert len(result) > 0
    assert result[0]["name"] == "Nguyen Van A"

