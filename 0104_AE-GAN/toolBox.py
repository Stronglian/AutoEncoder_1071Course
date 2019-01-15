# -*- coding: utf-8 -*-
"""@author: StrongPria
"""
import numpy as np
import os
DEBUG_PRINT = True
#%%
# python >= 3.2
def CheckFolder(outputFolder):
    """ 確認資料夾存在與否，若無，遞迴創建。
    原本是回傳 bool；改成回傳輸入的名稱"""
    print(outputFolder, ":", end = "")
    if ( os.path.isdir(outputFolder)):
        print("Directory exists~")
        return outputFolder
    else:
        print("Directory not found!")
        os.makedirs(outputFolder, exist_ok=True) # os.mkdir(outputFolder) 
        if ( os.path.isdir(outputFolder)):
            print("CREAT DONE: Directory exists!")
            return outputFolder
    return False
#%%
from pytz import timezone
from datetime import datetime
class DataLog:
    def __init__(self, timezone_local = "Asia/Taipei", folder = "./"):
        """ # timeaone set #TPE 以這樣的變數可能要改一下變數名稱。 """
        # 
        self.SetFolder(folder, txtName = "tmp")
        print("Remember Set Folder!" if folder is "./" else "Set Folder " + folder)
        
        print("Set Timezone", timezone_local)
        self.tpe = timezone(timezone_local)
        return
    def SetFolder(self, folder, txtName = None, file_extension = ".log"):
        """ 設定記錄檔以及對應的目錄"""
        if folder[-1] != "/":
            folder += "/"
        CheckFolder(folder);
        self.folder = folder
        # txtName set
        if txtName is None:
            self.txtName = folder.rsplit("/", 2)[1] + file_extension
        elif txtName.rsplit(".", 1)[-1] != file_extension:
            self.txtName = txtName + file_extension
        else:
            self.txtName = txtName
        return
    def _GetTime_TPE(self):
        """ 取得指定時區的時間。 """
        utcnow = datetime.utcnow()
        return self.tpe.fromutc(utcnow).timetuple()
    def WriteLog(self, inputString):
        """ 將 inputString 輸入設定好的位置。 """
        with open(self.folder + self.txtName, "a") as f:
            f.write(inputString + "\n")
        return inputString
    def SetTimeLog(self, eventTitle):
        """ 以 eventTitle 配合當下時間輸入記錄檔。 """
        time_now = self._GetTime_TPE()
#         self.WriteLog(eventTitle + ": " + "-".join([str(i) for i in time_now[0:3]]) + " " +":".join([str(i) for i in time_now[3:5]]))
        self.WriteLog("%s : %4d-%2d-%2d %2d:%2d"%(eventTitle, time_now[0], time_now[1], time_now[2], time_now[3], time_now[4]))
        return
#%%
import matplotlib.pyplot as plt
from cv2 import imwrite
def ResultImgShow(inputImg1, cols_output = 4, inputImg2 = None, modelName = "MODELNAME", strImgLabel = "TMP", boolShow = True):
    """ 
    目錄放在 modelName 前
    圖片名稱： modelName 去副檔名，加上 strImgLabel 
    cols_output: 橫軸幾張圖，"""
    # 輸出參數設置
    img_amount1 = len(inputImg1)
    cols_output = cols_output 
    rows_output = img_amount1//cols_output; #print(rows_output1);
#     if rows_output > cols_output:
#         rows_output = cols_output
    # 輸出設置 - 水平堆疊再垂直堆疊
    ## v - 初始
    img_h = inputImg1[0]
    for i in range(1, cols_output):
        img_tmp = inputImg1[i]
        img_h = np.hstack((img_h, img_tmp))
    img_v = img_h.copy()
    ## v - Loop - inputImg1
    for j in range(1, rows_output): #在 2
        ## h - 初始
        img_h = inputImg1[j * cols_output]
        ## h - Loop
        for i in range(1, cols_output):
            img_tmp = inputImg1[j * cols_output + i]
            img_h = np.hstack((img_h, img_tmp))
        img_v = np.vstack((img_v, img_h))
    
    if not inputImg2 is None:
        img_amount = len(inputImg2)
        rows_output = img_amount//cols_output; #print(rows_output);
        ## v - Loop - inputImg2
        for j in range(0, rows_output):
            ## h - 初始
            img_h = inputImg2[j * cols_output]
            ## h - Loop
            for i in range(1, cols_output):
                img_tmp = inputImg2[j * cols_output + i]
                img_h = np.hstack((img_h, img_tmp))
            img_v = np.vstack((img_v, img_h))
    
    # 顯示 與 存取
    imwrite(modelName.rsplit(".", 1)[0] +"_"+ strImgLabel+ ".png", img_v)
    if boolShow:
        plt.imshow(img_v, cmap = "gray")
    #     plt.savefig(model_name.split(".")[0] +"_"+ strImgLabel+ ".png")
        plt.show()
        plt.close()
    return

#%%
from skimage.measure import compare_psnr, compare_ssim
def PSNR_ALL(testData, truthData, strImgLabel = "TMP", boolTest = False):
    """ """
#     dataAmount = 1 if testData.shape < 3 else testData.shape[0]
#     if testData.shape < 3:
#         dataAmount = 1
#     else:
    dataAmount = testData.shape[0]
    psnrSum_test = 0
    for i in range(dataAmount):
        groundTruth   = truthData[i, :,:]
        predictResult = testData[i, :,:]
        psnrTmp = float(compare_psnr(groundTruth, predictResult))
        psnrSum_test += psnrTmp
    psnrSum_test /= dataAmount
    print(strImgLabel, "PSNR:", psnrSum_test)
    return psnrSum_test
def SSIM_ALL(testData, truthData, strImgLabel = "TMP", boolTest = False):
    """ """
    dataAmount = testData.shape[0]
    ssimSum_test = 0
    for i in range(dataAmount):
        groundTruth   = truthData[i, :,:]
        predictResult = testData[i, :,:]
        ssimTmp = float(compare_ssim(groundTruth, predictResult))
        ssimSum_test += ssimTmp
    ssimSum_test /= dataAmount
    print(strImgLabel, "SSIM:", ssimSum_test)
    return ssimSum_test