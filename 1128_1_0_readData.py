# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 11:41:19 2018

"""

import numpy as np

#if __name__ == "__main__":
#%% 資料引入
dataSetName = "mnist-pria-awgn_snr=10.npz"
f = np.load(dataSetName)
x_train, y_train = f['x_train'], f['y_train']
x_test, y_test = f['x_test'], f['y_test']