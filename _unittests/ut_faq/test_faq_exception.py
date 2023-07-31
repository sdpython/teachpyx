import unittest
from teachpyx.ext_test_case import ExtTestCase
from teachpyx.faq.faq_exception import call_stack


class TestFaqException(ExtTestCase):
    def test_call_back(self):
        def insidef():
            ft = call_stack()
            return ft

        def insidefe():
            try:
                raise RuntimeError("an error was raised")
            except Exception:
                ft = call_stack()
                return ft

        cb, sb = insidef()
        self.assertEqual(sb, "")
        self.assertEqual(len(cb), 0)
        cb, sb = insidefe()
        self.assertEqual(len(cb), 1)
        self.assertIn('raise RuntimeError("an error was raised")', sb)


if __name__ == "__main__":
    unittest.main()
