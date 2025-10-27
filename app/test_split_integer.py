import pytest
from app.split_integer import split_integer

# Все тесты должны использовать функцию 'split_integer' и pytest.
# В каждом тесте вам нужно сравнить ожидаемый результат
# (на основе примеров) с фактическим результатом функции.

def test_should_return_part_equals_to_value_when_split_into_one_part():
    """Проверяет случай, когда число частей равно 1.
    Пример: split_integer(8, 1) == [8]"""
    value = 8
    parts = 1
    expected = [8]
    actual = split_integer(value, parts)
    assert actual == expected

def test_should_split_into_equal_parts_when_value_divisible_by_parts():
    """Проверяет случай, когда value делится на number_of_parts без остатка.
    Пример: split_integer(6, 2) == [3, 3]"""
    value = 6
    parts = 2
    expected = [3, 3]
    actual = split_integer(value, parts)
    assert actual == expected

def test_returns_correct_result_with_remainder_example_17_4():
    """Проверяет точный результат для первого примера с остатком.
    Пример: split_integer(17, 4) == [4, 4, 4, 5]"""
    value = 17
    parts = 4
    expected = [4, 4, 4, 5]
    actual = split_integer(value, parts)
    assert actual == expected

def test_returns_correct_result_with_remainder_example_32_6():
    """Проверяет точный результат для второго примера с остатком.
    Пример: split_integer(32, 6) == [5, 5, 5, 5, 6, 6]"""
    value = 32
    parts = 6
    expected = [5, 5, 5, 5, 6, 6]
    actual = split_integer(value, parts)
    assert actual == expected

def test_parts_should_be_sorted_when_they_are_not_equal():
    """Проверяет, что массив всегда отсортирован по возрастанию.
    Использует случай с остатком (17, 4) для проверки."""
    value = 17
    parts = 4
    # Ожидаем, что результат [4, 4, 4, 5] будет соответствовать ожидаемому
    expected = [4, 4, 4, 5]
    actual = split_integer(value, parts)
    assert actual == expected

def test_difference_between_max_min_is_at_most_one():
    """Проверяет основное требование: max(array) - min(array) <= 1."""
    value = 17
    parts = 4
    actual = split_integer(value, parts)
    # Проверяем, что разница между максимальным и минимальным элементом <= 1
    assert max(actual) - min(actual) <= 1

def test_sum_of_the_parts_should_be_equal_to_value():
    """Проверяет, что сумма всех частей всегда равна исходному value."""
    value = 32
    parts = 6
    actual = split_integer(value, parts)
    # Проверяем, что сумма всех частей равна исходному value
    assert sum(actual) == value

def test_value_equal_to_number_of_parts():
    """Проверяет граничный случай, когда value == number_of_parts.
    (Например, split_integer(4, 4) должен вернуть [1, 1, 1, 1])"""
    value = 4
    parts = 4
    expected = [1, 1, 1, 1]
    actual = split_integer(value, parts)
    assert actual == expected
