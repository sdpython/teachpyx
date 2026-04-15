import unittest
from matplotlib.axes import Axes
import pandas
from teachpyx.ext_test_case import ExtTestCase
from teachpyx.tools.pandas import plot_waterfall, read_csv_cached


class TestPandas(ExtTestCase):
    def test_read_csv_cached(self):
        df = read_csv_cached(
            "https://github.com/sdpython/teachpyx/raw/main/_data/paris_54000.zip"
        )
        df2 = read_csv_cached(
            "https://github.com/sdpython/teachpyx/raw/main/_data/paris_54000.zip"
        )
        self.assertEqual(df.shape, df2.shape)
        self.assertEqual(list(df.columns), list(df2.columns))

    def test_plot_waterfall(self):
        df = pandas.DataFrame(
            {
                "name": ["A", "B", "C"],
                "delta": [10, -3, 5],
            }
        )
        ax, plot_df = plot_waterfall(df, "delta", "name", total_label="TOTAL")
        self.assertIsInstance(ax, Axes)
        self.assertEqual(list(plot_df["label"]), ["A", "B", "C", "TOTAL"])
        self.assertEqual(list(plot_df["start"]), [0.0, 10.0, 7.0, 0.0])
        self.assertEqual(list(plot_df["end"]), [10.0, 7.0, 12.0, 12.0])

    def test_plot_waterfall_missing_column(self):
        df = pandas.DataFrame({"name": ["A"], "delta": [1]})
        with self.assertRaises(ValueError):
            plot_waterfall(df, "missing", "name")

    def test_plot_waterfall_missing_label_column(self):
        df = pandas.DataFrame({"name": ["A"], "delta": [1]})
        with self.assertRaises(ValueError):
            plot_waterfall(df, "delta", "missing")

    def test_plot_waterfall_bad_colors(self):
        df = pandas.DataFrame({"name": ["A"], "delta": [1]})
        with self.assertRaises(ValueError):
            plot_waterfall(df, "delta", "name", colors=("r",))

    def test_plot_waterfall_not_numeric(self):
        df = pandas.DataFrame({"name": ["A"], "delta": ["x"]})
        with self.assertRaises(ValueError):
            plot_waterfall(df, "delta", "name")


if __name__ == "__main__":
    unittest.main()
