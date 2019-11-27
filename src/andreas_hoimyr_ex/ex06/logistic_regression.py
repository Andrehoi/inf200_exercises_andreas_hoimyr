# -*- coding: utf-8 -*-

"""
source https://github.com/yngvem/INF200-2019-Exercises/blob/master
/src/YOUR_NAME_ex/ex06/logistic_regression.py
"""

__author__ = "Andreas Sandvik Hoeimyr"
__email__ = "andrehoi@nmbu.no"


import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.exceptions import NotFittedError
from sklearn.utils import check_random_state, check_X_y


def sigmoid(z):
    r"""Perform a logistic transform on the input.
    This function applies the sigmoidal function element-wise to all
    elements of `z`. The sigmoidal function is on the following form:

    Parameters
    ----------
    z : np.ndarray
        Logit to transform.
    Returns
    -------
    sigmoidal_transformed_z : np.ndarray
        Transformed input.
    """
    return 1/(1 + np.exp(-z))


def predict_proba(coef, X):
    r"""Predict the class probabilities for each data point in :math:`X`.
    Estimate which class each data point in X corresponds to.

    ----------
    coef : np.ndarray(shape=(r,))
        The weight vector, :math:`w`
    X : np.ndarray(shape=(n, r))
        The data matrix (aka design or measurement matrix)
    Returns
    -------
    p : np.ndarray(shape(n,))
        The predicted class probabilities.
    """
    return sigmoid(X@coef)


def logistic_gradient(coef, X, y):
    r"""Returns the gradient of a logistic regression model.

    Parameters
    ----------
    coef : np.ndarray(shape=(r,))
        The weight vector, :math:`w`
    X : np.ndarray(shape=(n, r))
        The data matrix (aka design or measurement matrix)
    y : np.ndarray(shape=(n,))
        The true class labels for each data point.
    Returns
    -------
    gradient : np.ndarray(shape=(r,))
        The gradient of the cross entropy loss related to the linear
        logistic regression model.
    """
    return -(y - predict_proba(coef, X))@X


class LogisticRegression(BaseEstimator, ClassifierMixin):
    """A logistic regression classifier that follows the scikit-learn API.
    Note that the ``__init__`` method of scikit-learn estimators should not do
    any logic or input validation. This is all taken care of in the ``fit``
    method.

    Parameters
    ----------
    max_iter : int (default=1000)
        Maximum number of gradient descent iterations to run.
    tol : float (default=1e-5)
        The gradient descent iterations will converge when the gradient
        norm is less than this.
    learning_rate : float (default=0.01)
        The step-size for the gradient descent updates.
    random_state : np.random.random_state or int or None (default=None)
        A numpy random state object or a seed for a numpy random state object.

    Attributes
    ----------
    coef_ : The logistic regression weights (initialised in ``self.fit``)
    max_iter : int (default=1000)
        Maximum number of gradient descent iterations to run.
    tol : float (default=1e-5)
        The gradient descent iterations will converge when the gradient
        norm is less than this.
    learning_rate : float (default=0.01)
        The step-size for the gradient descent updates.
    random_state : np.random.random_state or int or None (default=None)
        A numpy random state object or a seed for a numpy random state object.
    """

    def __init__(
        self, max_iter=1000, tol=1e-5, learning_rate=0.01,
            random_state=None):
        """Initialise a logistic regression instance.
        The ``__init__`` method of scikit-learn estimators should not do any
        logic or input validation. This is all taken care of in the ``fit``
        method.

        Parameters
        ----------
        max_iter : int (default=1000)
            Maximum number of gradient descent iterations to run.
        tol : float (default=1e-5)
            The gradient descent iterations will converge when the gradient
            norm is less than this.
        learning_rate : float (default=0.01)
            The step-size for the gradient descent updates.
        random_state : np.random.random_state or int or None (default=None)
            A numpy random state object or a seed for a numpy random state
            object.
        """
        self.max_iter = max_iter
        self.tol = tol
        self.learning_rate = learning_rate
        self.random_state = random_state
        self.counter = 0

    def _fit_gradient_descent(self, coef, X, y):
        r"""Fit the logisitc regression model to the data given initial
        weights

        Parameters
        ----------
        coef : np.ndarray(shape=(r,))
            The initial guess for the coefficient vector.
            May be modified inplace by the method.
        X : np.ndarray(shape=(n, r))
            The data matrix
        y : np.ndarray(shape=(n,))
            The target vector
        Returns
        -------
        coef : np.ndarray(shape=(n,))
            The logistic regression weights
        """
        counter = 0
        while True:
            coef = coef - self.learning_rate*logistic_gradient(coef, X, y)

            if self._has_converged(coef, X, y):
                print('Converged after {0} iterations'.format(counter))
                return coef

            if counter == self.max_iter:
                return coef

            counter += 1

    def _has_converged(self, coef, X, y):
        """
        Parameters
        ----------
        coef : The weight vector
        X : The data matrix (aka design or measurement matrix)
        y : The true class labels for each data point.
        Returns
        -------
        has_converged : bool
            True if the convergence criteria above is met, False otherwise.
        """

        return np.linalg.norm(logistic_gradient(coef, X, y)) < self.tol

    def fit(self, X, y):
        """Fit a logistic regression model to the data.
        Parameters
        ----------
        X : np.ndarray(shape=(n, r))
            The data matrix
        y : np.ndarray(shape=(n,))
            The observed classes for each data point in X.
        """
        # This function ensures that X and y has acceptable data types
        # and flattens y to have shape (n,) if it has shape (n, 1)
        X, y = check_X_y(X, y, order="C")

        if any((y < 0) | (y > 1)):
            raise ValueError("Only y-values between 0 and 1 are accepted.")

        # A random state is a random number generator, akin to those
        # you made in earlier coursework. It has all functions of
        # np.ranom, but its sequence of random numbers is not affected
        # by calls to np.random.
        random_state = check_random_state(self.random_state)
        coef = random_state.standard_normal(X.shape[1])

        self.coef_ = self._fit_gradient_descent(coef, X, y)
        return self

    def predict_proba(self, X):
        """Estimate the class probabilities.
        This function returns the probability that each datapoint belongs to
        the positive class.
        Parameters
        ----------
        X : np.ndarray
            The data matrix.
        Returns
        -------
        p : np.ndarray
            A vector of probabilities. The i-th entry is the probability for
            the i-th data point belonging to the positive class.
        """
        if not hasattr(self, "coef_"):
            raise NotFittedError("Call fit before prediction")
        return predict_proba(self.coef_, X)

    def predict_log_proba(self, X):
        """Estimate the class log probabilities.
        This function returns the probability that each datapoint belongs to
        the positive class.
        Parameters
        ----------
        X : np.ndarray
            The data matrix.
        Returns
        -------
        lp : np.ndarray
            A vector of log probabilities. The i-th entry is the log
            probability for the i-th data point belonging to the positive
            class.
        """
        return np.log(self.predict_proba(X))

    def predict(self, X):
        """Predict whether each data point in X belongs to the positive class
        Parameters
        ----------
        X : np.ndarray
            Data matrix
        Returns
        -------
        yhat : np.ndarray
            Predicted classes for the input data matrix. len(yhat) == len(X)
        """
        return self.predict_proba(X) >= 0.5


if __name__ == "__main__":
    # Simulate a random dataset
    X = np.random.standard_normal((100, 5))
    coef = np.random.standard_normal(5)
    y = predict_proba(coef, X) > 0.5

    # Fit a logistic regression model to the X and y vector
    lr_model = LogisticRegression(tol=2)
    lr_model.fit(X, y)

    # Create a logistic regression object and fit it to the dataset

    # Print performance information

    print(f"Accuracy: {lr_model.score(X, y)}")
    print(f"True coefficients: {coef}")
    print(f"Learned coefficients: {lr_model.coef_}")