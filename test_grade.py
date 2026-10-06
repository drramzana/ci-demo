from grade import grade


def test_grade_a():
    assert grade(95) == "A"


def test_grade_pass():
    assert grade(75) == "Pass"
