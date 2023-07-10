"""linear_regression_simple.py

Loads the necessary Python libraries.
Reads in a dataset.
Plots a scatterplot of 'score' versus 'completed'.
Fits a simple linear regression model predicting 'score' based on 'completed'.
Prints the intercept and slope of the model.
Plots the fitted regression line on top of the scatterplot.
Predicts the 'score' for a learner who has completed 20 lessons.
Calculates and prints the fitted values and residuals from the model.
Checks the normality assumption of the residuals using a Q-Q plot.
Checks the homoscedasticity assumption by plotting residuals against fitted values.
Creates a boxplot of 'score' versus 'lesson'.
Fits a linear regression model predicting 'score' based on 'lesson'.
Calculates and prints the group means and the mean difference of 'score' between different lessons.
Plots 'score' versus 'completed', with points colored by 'lesson'.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

class DataLoader:
    """
    This class is used to load data.
    """

    def __init__(self, file_path):
        """
        Args:
            file_path (str): The path to the data file.
        """
        self.file_path = file_path

    def load_data(self):
        """
        Load data from CSV file.

        Returns:
            DataFrame: Loaded data.
        """
        return pd.read_csv(self.file_path)


class DataVisualizer:
    """
    This class is used to visualize data.
    """

    @staticmethod
    def scatter_plot(x, y, xlabel, ylabel, title):
        """
        Create a scatter plot of x vs y.

        Args:
            x (Series): The data to be plotted on x-axis.
            y (Series): The data to be plotted on y-axis.
            xlabel (str): Label for x-axis.
            ylabel (str): Label for y-axis.
            title (str): Title for the plot.
        """
        plt.scatter(x, y)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.show()
        plt.clf()

    @staticmethod
    def scatter_plot_with_line(x, y, line, xlabel, ylabel, title):
        """
        Create a scatter plot of x vs y and a line plot.

        Args:
            x (Series): The data to be plotted on x-axis.
            y (Series): The data to be plotted on y-axis.
            line (Series): The data to be plotted as line.
            xlabel (str): Label for x-axis.
            ylabel (str): Label for y-axis.
            title (str): Title for the plot.
        """
        plt.scatter(x, y)
        plt.plot(x, line, color='red')
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.show()
        plt.clf()

    @staticmethod
    def boxplot(x, y, xlabel, ylabel, title):
        """
        Create a box plot of x vs y.

        Args:
            x (Series): The data to be plotted on x-axis.
            y (Series): The data to be plotted on y-axis.
            xlabel (str): Label for x-axis.
            ylabel (str): Label for y-axis.
            title (str): Title for the plot.
        """
        sns.boxplot(x=x, y=y)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.show()
        plt.clf()


class LinearRegressionModel:
    """
    This class is used to create and analyze a linear regression model.
    """

    def __init__(self, X, y):
        """
        Args:
            X (DataFrame): The input data.
            y (Series): The output data.
        """
        self.X = X
        self.y = y
        self.model = None

    def fit(self):
        """
        Fit a linear regression model.

        Returns:
            Tuple: Intercept and slope of the model.
        """
        self.model = sm.OLS(self.y, self.X).fit()
        intercept = self.model.params[0]
        slope = self.model.params[1]
        return intercept, slope

    def predict(self, new_X):
        """
        Predict the output for new input data.

        Args:
            new_X (DataFrame): The new input data.

        Returns:
            Series: The predicted output.
        """
        return self.model.predict(new_X)

    def residuals(self):
        """
        Calculate the residuals of the model.

        Returns:
            Series: The residuals.
        """
        return self.model.resid
