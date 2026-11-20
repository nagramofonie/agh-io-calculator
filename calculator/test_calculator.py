from calculator import Calculator
import pytest

#calc = Calculator(2, 0)
#print(calc.devide())

class TestCalculator:

    def test_sum(self):
        calc = Calculator(1,3)
        assert calc.sum() == 4

    def test_subtract(self):
        calc = Calculator(3, 5)
        assert calc.subtract() == -2

    def test_multiply(self):
        calc = Calculator(3, 5)
        assert calc.multiply() == 15

    def test_divide(self):
        calc = Calculator(3, 1)
        assert calc.divide() == 3

    def test_divide_by_zero(self):
        calc = Calculator(3, 0)

        with pytest.raises(ZeroDivisionError):
            assert calc.divide()
