from calculator import Calculator

#calc = Calculator(2, 0)
#print(calc.devide())

class TestCalculator:

    def test_sum(self):
        calc = Calculator(1,3)
        assert calc.sum() == 4

    def test_substract(self):
        calc = Calculator(3, 5)
        assert calc.substract() == -2

    def test_multiply(self):
        calc = Calculator(3, 5)
        assert calc.multiply() == 15

    def test_devide(self):
        calc = Calculator(3, 1)
        assert calc.devide() == 3

'''
(pythonproject) kasia@centos10:~/agh/io$ pytest -v
================================================================================================== test session starts ==================================================================================================
platform linux -- Python 3.14.8, pytest-9.2.0, pluggy-1.7.0 -- /home/kasia/agh/io/.venv/bin/python
cachedir: .pytest_cache
rootdir: /home/kasia/agh/io
configfile: pyproject.toml
collected 4 items                                                                                                                                                                                                       

test_calculator.py::TestCalculator::test_sum PASSED                                                                                                                                                               [ 25%]
test_calculator.py::TestCalculator::test_substract PASSED                                                                                                                                                         [ 50%]
test_calculator.py::TestCalculator::test_multiply PASSED                                                                                                                                                          [ 75%]
test_calculator.py::TestCalculator::test_devide PASSED                                                                                                                                                            [100%]

=================================================================================================== 4 passed in 0.05s ===================================================================================================
(pythonproject) kasia@centos10:~/agh/io$ 
'''