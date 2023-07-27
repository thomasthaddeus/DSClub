"""svm_visualization.py
This module provides utilities for visualizing the decision boundaries of
support vector machine (SVM) classifiers.

The module includes functions to create a meshgrid based on the axes limits of
a plot, plot the decision boundaries of an SVM classifier, and a higher-level
function to generate the meshgrid and draw the boundaries in one step.

Returns:
    None: These functions are used for their side effects of plotting to the
    current matplotlib figure.
"""

import numpy as np
import matplotlib.pyplot as plt


def make_meshgrid(ax, h=.02):
    """
    Generates a 2D meshgrid of points based on the limits of the given axes.

    Args:
        ax (matplotlib.axes.Axes): The axes for which to generate the meshgrid.
        h (float, optional): The step size for the meshgrid. Default is .02.

    Returns:
        tuple: A tuple containing two 2D arrays representing the X and Y
        coordinates of the points in the meshgrid.
    """
    x_min, x_max = ax.get_xlim()
    y_min, y_max = ax.get_ylim()

    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    return xx, yy

def plot_contours(ax, clf, xx, yy, **params):
    """
    Plots the decision boundaries of a classifier using filled contours.

    Args:
        ax (matplotlib.axes.Axes): The axes on which to plot the contours.
        clf (sklearn.base.ClassifierMixin): The classifier for which to plot
        the decision boundaries.
        xx (np.array): The X coordinates of the points at which to evaluate the
        classifier.
        yy (np.array): The Y coordinates of the points at which to evaluate the
        classifier.
        **params: Additional parameters to pass to the contourf function.

    Returns:
        A ContourSet object containing the plotted contours.
    """
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    out = ax.contourf(xx, yy, Z, **params)
    return out

def draw_boundary(ax, clf):
    """
    Draws the decision boundary of a classifier.

    Args:
        ax (matplotlib.axes.Axes): The axes on which to draw the boundary.
        clf (sklearn.base.ClassifierMixin): The classifier for which to draw
        the boundary.

    Returns:
        A ContourSet object containing the plotted contours.
    """
    xx, yy = make_meshgrid(ax)
    return plot_contours(ax, clf, xx, yy,cmap=plt.cm.coolwarm, alpha=0.5)
