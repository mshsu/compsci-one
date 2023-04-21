# Project 2
#
# Name: Martin Hsu
# Instructor: Brian Jones
# Section: 01

import unittest

import lander_funcs


class TestCases(unittest.TestCase):
    def test_update_acceleration1(self):
        self.assertAlmostEqual(
            lander_funcs.update_acceleration(1.62, 0), -1.62)

    def test_update_acceleration2(self):
        self.assertAlmostEqual(
            lander_funcs.update_acceleration(1.62, 5), 0.00)

    def test_update_acceleration3(self):
        self.assertAlmostEqual(
            lander_funcs.update_acceleration(1.62, 9), 1.296)

    def test_update_altitude1(self):
        self.assertAlmostEqual(
            lander_funcs.update_altitude(0, 0, 0), 0)

    def test_update_altitude2(self):
        self.assertAlmostEqual(
            lander_funcs.update_altitude(1300, 10, 1.296), 1310.648)

    def test_update_altitude3(self):
        self.assertAlmostEqual(
            lander_funcs.update_altitude(0, -30, -2), 0)

    def test_update_velocity1(self):
        self.assertAlmostEqual(
            lander_funcs.update_velocity(0, 0), 0)

    def test_update_velocity2(self):
        self.assertAlmostEqual(
            lander_funcs.update_velocity(20, -1.62), 18.38)

    def test_update_velocity3(self):
        self.assertAlmostEqual(
            lander_funcs.update_velocity(-20, -1.62), -21.62)

    def test_update_velocity4(self):
        self.assertAlmostEqual(
            lander_funcs.update_velocity(20, 1.296), 21.296)

    def test_update_velocity5(self):
        self.assertAlmostEqual(
            lander_funcs.update_velocity(-20, 1.296), -18.704)

    def test_update_fuel1(self):
        self.assertEqual(
            lander_funcs.update_fuel(0, 0), 0)

    def test_update_fuel2(self):
        self.assertEqual(
            lander_funcs.update_fuel(100, 5), 95)

    def test_update_fuel3(self):
        self.assertEqual(
            lander_funcs.update_fuel(1, 1), 0)


if __name__ == '__main__':
    unittest.main()
