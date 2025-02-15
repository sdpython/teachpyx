import numpy as np
from sklearn.base import BaseEstimator, RegressorMixin


class PositiveOrNegativeLinearRegression(BaseEstimator, RegressorMixin):
    """
    Trains a linear regression with coefficients of the same sign.

    :param epsilon: gradient step
    :param max_iter: number maximum of iterations
    :param positive: only positive weights (or negative if False)
    """

    def __init__(
        self, epsilon: float = 1.0, max_iter: int = 100, positive: bool = True
    ):
        self.epsilon = epsilon
        self.max_iter = max_iter
        self.positive = positive

    def fit(self, X, y):
        "Trains."
        theta = np.random.randn(X.shape[1])
        for i in range(self.max_iter):
            epsilon = self.epsilon * 10 / (i + 10)
            grad = X.T @ (X @ theta - y)
            theta = theta - epsilon * grad / X.shape[0]
            theta = np.maximum(theta, 0) if self.positive else np.minimum(theta, 0)
            if np.abs(theta).max() == 0:
                # If all coefficients are null. The algorithm may be stuck.
                theta = np.random.randn(X.shape[1]) * epsilon
        self.theta_ = theta
        return self

    def predict(self, X):
        "Predicts."
        return X @ self.theta_
