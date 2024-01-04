import unittest
from teachpyx.ext_test_case import ExtTestCase
from teachpyx.faq.faq_geo import lambert93_to_WGPS


class TestFaqGeoHelper(ExtTestCase):
    def test_lambert93_to_longlat(self):
        x1, y1 = lambert93_to_WGPS(99217.1, 6049646.300000001)
        x2, y2 = lambert93_to_WGPS(1242417.2, 7110480.100000001)
        d1 = abs(x1 - (-4.1615802638173065)) + abs(y1 - 41.303505287589545)
        d2 = abs(x2 - 10.699505053975292) + abs(y2 - 50.85243395553585)
        assert d1 + d2 < 1e-8, AssertionError(f"d1={d1}, d2={d2}")


if __name__ == "__main__":
    unittest.main()
