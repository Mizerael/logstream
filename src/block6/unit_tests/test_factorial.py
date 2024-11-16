# python -m unittest src.block6.unit_tests.test_factorial
# from project root directory
import datetime
import unittest
from src.block6.factorial import factorial


class TestFactorial(unittest.TestCase):
    def setUp(self) -> None:
        self.start_time = datetime.datetime.now()

    def test_factorial(self):
        test_data = [
            {"n": 0, "expected": 1},
            {"n": 1, "expected": 1},
            {"n": 2, "expected": 2},
            {"n": 3, "expected": 6},
            {"n": 4, "expected": 24},
            {"n": 5, "expected": 120},
            {"n": 6, "expected": 720},
            {"n": 7, "expected": 5040},
            {"n": 20, "expected": 2432902008176640000},
        ]
        for test_case in test_data:
            self.assertEqual(
                factorial(test_case.get("n")), test_case.get("expected")
            )

    def test_factorial_exceptions(self):
        exceptions_data = [
            {"n": -1, "expected": ValueError},
            {"n": 0.5, "expected": TypeError},
            {"n": "a", "expected": TypeError},
            {"n": 21, "expected": ValueError},
        ]
        for exception_case in exceptions_data:
            with self.assertRaises(exception_case.get("expected")):
                factorial(exception_case.get("n"))

    def tearDown(self) -> None:
        final_time = datetime.datetime.now()
        print(
            f"""\nВремя выполнения {self._testMethodName}: """
            f"""{final_time - self.start_time} ms"""
        )


if __name__ == "__main__":
    unittest.main()
