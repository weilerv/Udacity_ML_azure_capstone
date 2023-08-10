from sklearn.linear_model import LogisticRegression
import argparse
import os
import numpy as np
from sklearn.metrics import mean_squared_error
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
from azureml.core.run import Run
from azureml.data.dataset_factory import TabularDatasetFactory
from azureml.core import Dataset

def clean_data(data):
    # Clean and one hot encode data
    x_df = data.to_pandas_dataframe().dropna()
    x_df["gender"] = x_df.gender.apply(lambda s: 1 if s == "Male" else 0)
    smoking_history = pd.get_dummies(x_df.smoking_history, prefix="smoking_history")
    x_df.drop("smoking_history", inplace=True, axis=1)
    x_df = x_df.join(smoking_history)
    y_df = x_df.pop("diabetes")
    return x_df, y_df

def main():
    # Add arguments to script
    parser = argparse.ArgumentParser()

    parser.add_argument('--C', type=float, default=1.0, help="Inverse of regularization strength. Smaller values cause stronger regularization")
    parser.add_argument('--max_iter', type=int, default=100, help="Maximum number of iterations to converge")

    args = parser.parse_args()

    run = Run.get_context()

    run.log("Regularization Strength:", np.float(args.C))
    run.log("Max iterations:", np.int(args.max_iter))

    # TODO: get dataset from kaggle
    # Data is located at:
    # https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset

    data_name = "diabetes_prediction_dataset.csv"

    data = Dataset.get_by_name(ws, name=data_name) 

    
    x, y = clean_data(ds)

    # TODO: Split data into train and test sets.

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    model = LogisticRegression(C=args.C, max_iter=args.max_iter).fit(x_train, y_train)

    accuracy = model.score(x_test, y_test)
    run.log("Accuracy", np.float(accuracy))

if __name__ == '__main__':
    main()