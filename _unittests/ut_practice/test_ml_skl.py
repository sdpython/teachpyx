import unittest
import numpy as np
from sklearn.base import is_regressor
from sklearn.ensemble import StackingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.utils._tags import get_tags
from teachpyx.ext_test_case import ExtTestCase
from teachpyx.practice.ml_skl import PositiveOrNegativeLinearRegression


class TestPracticeMlSlk(ExtTestCase):
    def test_positive_linear_regression(self):
        np.random.seed(0)
        X = np.random.randn(5, 2)
        y = X[:, 0] * 0.3 + X[:, 1] * 0.6 + np.random.randn(5) / 100
        lr = LinearRegression().fit(X, y)
        self.assertEqualArray(lr.coef_, np.array([0.3, 0.6]), atol=0.01)
        plr = PositiveOrNegativeLinearRegression(max_iter=50, positive=True)
        plr.fit(X, y)
        self.assertEqualArray(plr.theta_, np.array([0.3, 0.6]), atol=0.01)
        self.assertTrue(is_regressor(lr))
        self.assertTrue(is_regressor(plr))
        tags = get_tags(plr)
        self.assertEqual(tags.estimator_type, "regressor")

    def test_plr_stacking(self):
        stacking_clr = StackingRegressor(
            estimators=[
                ("plr", PositiveOrNegativeLinearRegression()),
                ("nlr", PositiveOrNegativeLinearRegression(positive=False)),
            ],
            final_estimator=LinearRegression(),
            cv=5,  # Nombre de folds pour la validation croisée
        )
        np.random.seed(0)
        X = np.random.randn(5, 2)
        y = X[:, 0] * 0.3 + X[:, 1] * 0.6 + np.random.randn(5) / 100
        stacking_clr.fit(X, y)


if __name__ == "__main__":
    unittest.main(verbosity=2)
