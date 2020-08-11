import numpy as np
import pandas as pd
import functools
import math
from datetime import date

# n_per_SMA is used to calculate the Simple Moving Average (SMA) over the last n periods. 
# SMA = (A1 + A2 + ... + An)/n, where Ai is the value i periods prior to the current period.


def n_per_SMA(arr,n): 
    sum = 0
    l = len(arr)
    for j in range(0,n):
        sum = sum + arr[l-j-1]
    return (sum/n)

# n_per_ROC is used to calculate the Rate of Change. 
# ROC = 100*(Close[i]-Close[i-n])/Close[i-n]

def n_per_ROC(arr,n,i):
    arr1 = []
    for j in range(0,n):
        roc = (arr[i-j]-arr[i-j-n])*100/n
        arr1.append(roc) 
    return arr1
    

### KST = (RCMA#1*1) + (RCMA#2*2) + (RCMA#3*3) + (RCMA#4*4) where
# RCMA#1 = 10 period SMA of 10 period ROC 
# RCMA#2 = 10 period SMA of 15 period ROC 
# RCMA#3 = 10 period SMA of 20 period ROC 
# RCMA#4 = 15 period SMA of 30 period ROC
    
#Pring's Know Sure Thing

def KST(data): 
    arr = []
    n = len(data)
    for i in range(0,30):
        arr.append('N')
    for i in range(30,n):
        RCMA_1 = n_per_SMA(n_per_ROC(data.Close.tolist(),10,i),10)
        RCMA_2 = n_per_SMA(n_per_ROC(data.Close.tolist(),15,i),10)
        RCMA_3 = n_per_SMA(n_per_ROC(data.Close.tolist(),20,i),10)
        RCMA_4 = n_per_SMA(n_per_ROC(data.Close.tolist(),30,i),15)
        kst = 1*RCMA_1 + 2*RCMA_2 + 3*RCMA_3 + 4*RCMA_4
        arr.append(kst)
    return arr







