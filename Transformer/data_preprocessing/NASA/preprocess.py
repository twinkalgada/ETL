import os
import sys
import pandas as pd
import numpy as np

data = pd.read_csv('thuml-Anomaly-Transformer/data_preprocessing/stan_norm_cleaned_nasa.csv')
data = data.drop(columns=['Unnamed: 0','class'],axis=0)
data = data.sort_values(by=["time"], ascending=True)

# train = data.iloc[:34370]
# print(len(train[train.outlier == 0]))
# exit()
train = data.iloc[:34370, 1:-1]
print(len(train.columns))
exit()
# print(train.head())
# exit()
# test = data.iloc[34370:44189,:-1]
# test = data.iloc[24548:,:-1]
test = data.iloc[34370:,1:-1]
# test_labels = data.iloc[34370:44189,[0]+[-1]]
# test_labels = data.iloc[24548:,[0]+[-1]]
test_labels = data.iloc[34370:,[0]+[-1]]
# print(len(test_labels[test_labels.outlier == 0]))
# exit()
train.to_csv('dataset/NASA/train.csv', index=False)
test.to_csv('dataset/NASA/test.csv', index=False)
test_labels.to_csv('dataset/NASA/test_labels.csv', index=False)