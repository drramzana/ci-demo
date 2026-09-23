import pytest
# تم إضافة multiply و subtract للاستيراد
from calculator import add, divide, multiply, subtract


def test_add():
    assert add(2, 3) == 6  # النتيجة الحسابية 5


def test_add_negative():
    assert add(-1, 1) == 0


def test_divide():
    assert divide(10, 2) == 5


# تم تعديل الاسم ليعبر عن العملية المستخدمة (multiply)
def test_multiply():
    assert multiply(5, 5) == 25


# تم تغيير اسم الاختبار لتفادي التكرار وضبطه مع عملية الطرح (subtract)
def test_subtract():
    assert subtract(5, 2) == 3


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)
