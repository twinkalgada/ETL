import os
import sys
import pandas as pd
import numpy as np
import subprocess
import glob
import argparse


def preprocessA1(file_name, folder_path):
    data = pd.read_csv(file_name)
    train_size = int(len(data)*0.8)
    print("Train_size="+str(train_size))
    train_set = data.iloc[:train_size]
    print("TrainSizePositive="+str(len(train_set[train_set.is_anomaly == 1])))
    print("TrainSizeNegative="+str(len(train_set[train_set.is_anomaly == 0])))
    train_set = train_set.iloc[:,:-1]
    test_set = data.iloc[train_size:,:-1]
    print("Test_size="+str(len(test_set)))
    test_labels = data.iloc[train_size:,[0]+[-1]]
    print("TestSizePositive="+str(len(test_labels[test_labels.is_anomaly == 1])))
    print("TestSizeNegative="+str(len(test_labels[test_labels.is_anomaly == 0])))
    train_set.to_csv(folder_path+'/train.csv', index=False)
    test_set.to_csv(folder_path+'/test.csv', index=False)
    test_labels.to_csv(folder_path+'/test_labels.csv', index=False)

def preprocessA3(file_name, folder_path):
    data = pd.read_csv(file_name)
    train_size = int(len(data)*0.8)
    print("Train_size="+str(train_size))
    train_set = data.iloc[:train_size]
    print("TrainSizePositive="+str(len(train_set[train_set.anomaly == 1])))
    print("TrainSizeNegative="+str(len(train_set[train_set.anomaly == 0])))
    train_set = train_set[['timestamps','value']]
    test_set = data.iloc[train_size:]
    test_set = test_set[['timestamps','value']]
    print("Test_size="+str(len(test_set)))
    test_labels = data.iloc[train_size:]
    test_labels = test_labels[['timestamps','anomaly']]
    print("TestSizePositive="+str(len(test_labels[test_labels.anomaly == 1])))
    print("TestSizeNegative="+str(len(test_labels[test_labels.anomaly == 0])))
    train_set.to_csv(folder_path+'/train.csv', index=False)
    test_set.to_csv(folder_path+'/test.csv', index=False)
    test_labels.to_csv(folder_path+'/test_labels.csv', index=False)

parser = argparse.ArgumentParser()
parser.add_argument('--file_name', type=str, default=None)
args = parser.parse_args()
file_name = args.file_name
print("Running file: ",file_name)
basename = os.path.basename(file_name)
folder_name = os.path.splitext(basename)[0]
folder_path = 'dataset/Yahoo/Test/'+folder_name
if not os.path.exists(folder_path):
   os.makedirs(folder_path)

preprocessA1(file_name, folder_path)
# preprocessA3(file_name, folder_path)