import unittest
import datetime
import matplotlib
from teachpyx.faq.faq_python import (
    class_getitem,
    get_day_name,
    get_month_name,
    graph_sankey,
)

matplotlib.use("Agg")


class TestFaqPython(unittest.TestCase):
    def test_month_name(self):
        dt = datetime.datetime(2016, 1, 25)
        name = get_month_name(dt)
        self.assertEqual(name, "January")

    def test_day_name(self):
        dt = datetime.datetime(2016, 1, 25)
        name = get_day_name(dt)
        self.assertEqual(name, "Monday")

    def test_class_getitem(self):
        class_getitem()

    def test_graph_sankey(self):
        ax, diagrams = graph_sankey(
            [1, -0.25, -0.75],
            labels=["input", "loss", "output"],
            orientations=[0, 1, -1],
            trunklength=2.0,
            title="flux",
        )
        self.assertEqual(ax.get_title(), "flux")
        self.assertEqual(len(diagrams), 1)


if __name__ == "__main__":
    unittest.main()
