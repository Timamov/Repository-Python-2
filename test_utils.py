from utils import add_two_numbers
import pytest

class TestAddTwoNumbers:
    target_function = add_two_numbers

    def test_add_two_numbers_success(self):
        number1 = 2
        number2 = 3
        expected_result = 5
        actual_result = add_two_numbers(number1, number2)

    def test_add_two_numbers_success_fail(self):
        number1 = 'dfjiffhnijfl'
        number2 = 'ewferhifreufh'
        with pytest.raises(ValueError):
             add_two_numbers(number1, number2)
        print(2222222)
