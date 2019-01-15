# 1071 期末作業
## 規則
- 52張拿出以下8張當test imags, 其餘為training images: 
- 紅桃 6, J; 黑桃 7, Q; 鑽石 8, K; 梅花 9, Q
  - => 編號：32、37、46、50、21、26、9、12
- input 採 PCA 60% 結果; 
- 要寫 Autoencoder 和 Autoencoder+Gan 兩種程式, 比較結果。

## 程式對應
- AE: 0114_AE.ipynb
- GAN: 0114_GAN.ipynb

## 環境：
- google colab
- python
- keras

## 結果
<!--
- AE 1: 當初的複雜架構
- GAN 1: 每個 epoch 有數個 batch，discriminator 每個 batch 訓練一次。
- GAN 2: 每個 epoch 有數個 batch，discriminator 每個 epoch 訓練一次。
-->
|  | PSNR | 內容 |
| -------- | -------- |  -------- | 
|  AE 1   | 12.44   | 當初的複雜架構 |
| GAN 1   | 12.68   | discriminator 每個 batch 訓練一次。 |
| GAN 2   | 12.54   | discriminator 每個 epoch 訓練一次。 |
