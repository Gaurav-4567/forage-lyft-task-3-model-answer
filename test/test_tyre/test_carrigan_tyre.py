import unittest
from tyre.carrigan_tires import CarriganTire


class TestCarriganTire(unittest.TestCase):
    def test_needs_service_true(self):
        tire_worn = [0.8, 0.9, 1.0, 0.7]
        tyre = CarriganTire(tire_worn)
        self.assertTrue(tyre)

    def test_needs_service_false(self):
        tire_worn = [0.8, 0.6, 0.5, 0.7]
        tyre = CarriganTire(tire_worn)
        self.assertFalse(tyre)
