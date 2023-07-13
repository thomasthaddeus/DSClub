# Licensed under the MIT License. See LICENSE
# for details.
# Author: Thaddeus Thomas <the-boss@thaddeust.com>
# =================================================================

""" knn_wrapper.py

This module provides a wrapper class for the K-Nearest Neighbors (KNN)
classifier from scikit-learn. The class encapsulates methods for data import,
model training, and prediction.

Summary:
This module contains a class, knnWrapperClass, which simplifies the process of
applying a KNN classifier to a given dataset. The class supports importing data
from CSV files, training the classifier, and making predictions.

Returns:
knnWrapperClass: A class object that encapsulates methods for a KNN
classification task.
"""

from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from numpy import ndarray

class KNNWrapperClass:
    """
    This class provides methods for training a KNN classifier, making
    predictions, and importing data files for training and testing.

    Attributes:
        knn (KNeighborsClassifier): An instance of the KNeighborsClassifier
        class from scikit-learn.
        df_train (pd.DataFrame): Pandas DataFrame for training data.
        df_train_target (pd.DataFrame): Pandas DataFrame for training targets.
        df_test (pd.DataFrame): Pandas DataFrame for test data.
        df_test_target (pd.DataFrame): Pandas DataFrame for test targets.
    """

    def __init__(self):
        self.knn = None
        self.df_train = None
        self.df_train_target = None
        self.df_test = None
        self.df_test_target = None

    def train(self, neighbors: int) -> None:
        """
        Train the KNN classifier with the specified number of neighbors.

        Args:
            neighbors (int): The number of neighbors to consider for
            classification.

        Raises:
            ValueError: If the training data or target is not imported.
        """
        if self.df_train is None or self.df_train_target is None:
            raise ValueError("Training data or target not imported")
        self.knn = KNeighborsClassifier(n_neighbors=neighbors)
        self.knn.fit(self.df_train, self.df_train_target)

    def predict(self) -> ndarray:
        """
        Make predictions using the trained KNN classifier on the test data.

        Returns:
            np.array: Array of predictions for the test data.

        Raises:
            ValueError: If the classifier is not trained or the test data is
            not imported.
        """
        if self.knn is None:
            raise ValueError("Classifier not trained")
        if self.df_test is None:
            raise ValueError("Test data not imported")
        return self.knn.predict(self.df_test)

    def import_train_file(self, trn_dat_fl: str, trn_tgt_fil: str) -> None:
        """
        Import training data and target files.

        Args:
            train_data_file (str): Path to the training data file.
            train_target_file (str): Path to the training target file.
        """
        self.df_train = pd.read_csv(trn_dat_fl)
        self.df_train_target = pd.read_csv(trn_tgt_fil)

    def import_test_file(self, test_data_file: str, test_target_file: str) -> None:
        """
        Import test data and target files.

        Args:
            test_data_file (str): Path to the test data file.
            test_target_file (str): Path to the test target file.
        """
        self.df_test = pd.read_csv(test_data_file)
        self.df_test_target = pd.read_csv(test_target_file)

    def evaluate(self) -> float:
        """
        Evaluate the accuracy of the trained KNN classifier on the test data.

        Returns:
            float: Accuracy of the classifier on the test data.

        Raises:
            ValueError: If the classifier is not trained, or the test data or
            targets are not imported.
        """
        if self.knn is None:
            raise ValueError("Classifier not trained")
        if self.df_test is None or self.df_test_target is None:
            raise ValueError("Test data or targets not imported")
        predictions = self.knn.predict(self.df_test)
        return accuracy_score(self.df_test_target, predictions)
