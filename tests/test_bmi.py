import unittest

from bmi import bmi_guidance, calculate_bmi


class BmiUnitTests(unittest.TestCase):
    def test_calculate_bmi(self):
        self.assertEqual(calculate_bmi(170, 65), 22.5)

    def test_calculate_bmi_rounds_to_one_decimal(self):
        self.assertEqual(calculate_bmi(180, 80), 24.7)

    def test_calculate_bmi_rejects_invalid_values(self):
        for height, weight in [
            (0, 65),
            (-1, 65),
            (170, 0),
            (170, -2),
            (float("inf"), 65),
            (170, float("nan")),
            (1e-300, 65),
            (1e308, 65),
            (1, 1e308),
        ]:
            with self.subTest(height=height, weight=weight):
                with self.assertRaises(ValueError):
                    calculate_bmi(height, weight)

    def test_taiwan_adult_thresholds(self):
        for bmi, category in [
            (18.4, "體重過輕"),
            (18.5, "健康體位"),
            (23.9, "健康體位"),
            (24.0, "體重過重"),
            (26.9, "體重過重"),
            (27.0, "肥胖"),
        ]:
            with self.subTest(bmi=bmi):
                self.assertEqual(bmi_guidance(bmi)["label"], category)


if __name__ == "__main__":
    unittest.main()
