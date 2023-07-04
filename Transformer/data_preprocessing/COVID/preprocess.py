import os
import sys
import pandas as pd
import numpy as np

# data = pd.read_csv('data_preprocessing/COVID/owid-covid-data.csv')
# data = data[data.iso_code == 'AFG']
# # data = data[['date','total_cases','new_cases','new_cases_smoothed','total_cases_per_million','new_cases_per_million','new_cases_smoothed_per_million']]
# data = data[['date','new_cases']]
# data.fillna(0, inplace=True)
# data.to_csv('dataset/COVID/covid.csv', index=False)
# exit()

# Covid preprocessed data
data = pd.read_csv('data_preprocessing/COVID/covid_processed.csv')
# data = data.sort_values(by=["date"], ascending=True)
train_size = round(len(data)*0.80)
test_size = len(data) - train_size
# print(len(data.columns))
# exit()
train = data.iloc[:train_size-1,0:-1]
# print(len(train[train.outlier == 0]))
# exit()
# print(train.head())
# exit()
test = data.iloc[train_size-1:,0:-1]
test_labels = data.iloc[train_size-1:,[0]+[-1]]
# test_labels = data.iloc[34370:44189,[0]+[-1]]
# test_labels = data.iloc[24548:,[0]+[-1]]
# test_labels = data.iloc[34370:,[0]+[-1]]
# print(len(test_labels[test_labels.outliers == 1]))
# exit()
# print(train_size, test_size, len(data))
train.to_csv('dataset/COVID/train.csv', index=False)
test.to_csv('dataset/COVID/test.csv', index=False)
test_labels.to_csv('dataset/COVID/test_labels.csv', index=False)