import pytest
from app import add, subtract, divide

# 1. Позитивний кейс
def test_add_positive():
    assert add(2, 3) == 5

# 2. Кейс з нулем
def test_add_with_zero():
    assert add(0, 5) == 5

# 3. Кейс з від'ємними числами
def test_add_negative():
    assert add(-4, -6) == -10

# 4. Звичайне ділення
def test_divide_normal():
    assert divide(10, 2) == 5.0

# 5. Перевірка винятку (ділення на 0)
def test_divide_by_zero():
    with pytest.raises(ValueError, match="Ділення на нуль неможливе"):
        divide(10, 0)