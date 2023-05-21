import unittest
from tyre.octoprime_tires import OctoprimeTire


class TestOctoprimeTire(unittest.TestCase):
    def test_needs_service_true(self):
        tire_worn = [0.8, 0.8, 1.0, 0.7]
        tyre = OctoprimeTire(tire_worn)
        self.assertTrue(tyre)

    def test_needs_service_false(self):
        tire_worn = [0.8, 0.6, 0.5, 0.8]
        tyre = OctoprimeTire(tire_worn)
        self.assertFalse(tyre)
