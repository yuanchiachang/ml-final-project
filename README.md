# Final Report 操作方法介紹
<br>
## 放進原始資料
1. 將 6.7GB 的原始訓練資料 train.csv 放在 ./train 資料夾中
<br>
## 利用 yaml 檔安裝環境、啟動環境
1. 打開 environment.yml 檔，根據電腦中 anaconda3 安裝的位置，<br>
更改 prefix: <anaconda3 安裝路徑>\anaconda3\envs\ml_final_project_tbrain_2
2. 到 anaconda prompt 中輸入 conda env create -f environment.yml
3. activate ml_final_project_tbrain_2
<br>
## 如何將 train data 切成很多的小檔案
1. 確認在 ./train 資料夾中是否存在 train.csv 6.7GB 原始訓練檔案
2. 進去 ./src/nn 中
3. 按 Kernel / Run All 執行 1_all_data_chunk.ipynb (runtime ~ 1hr) <br>
執行完之後在 ./src/nn 裡面有沒有 Tbrain_splitData 資料夾，裡面要有 330 個切割後的檔案<br>
如果 ipynb 檔 runtime 時間太長可以直接從下方連結將 Tbrain_splitData 資料夾放進 ./src/nn 中 <br>
https://drive.google.com/drive/folders/1fJqFRbAtcO-Nypbuuj1bOGOkcGJLmcKw?usp=sharing

<br>
## 統計方法過 simple baseline
1. 進去 ./src/nn 中
2. 按 Kernel / Run All 執行 2_count_how_many.ipynb <br>
執行完之後確認有沒有產生 ./result/test_data.csv 檔
<br>
./result/test_data.csv 檔即為對五十萬名消費者前三高消費金額類別預測資料
<br>

## neural network 模型
1. 進去 ./src/nn 中
2. 按 Kernel / Run All 執行 3_count_most_label_customer.ipynb <br>
執行完之後確認有沒有產生 ./data/all_record.csv 檔

3. 按 Kernel / Run All 執行 4_classification.ipynb <br>
執行完之後確認有沒有產生 ./data/full_record.csv, ./data/not_full_record.csv,./data/empty_record.csv 檔

4. 按 Kernel / Run All 執行 5_reduce_training_data.ipynb <br>
執行完之後確認有沒有產生 ./data/reduced_train.csv 檔

5. 按 Kernel / Run All 執行 6_split_reduced_train.ipynb <br>
執行完之後確認有沒有產生 ./data/full_reduced_train.csv, ./data/not_full_reduced_train.csv 檔

6. 按 Kernel / Run All 執行 7_linear_model.ipynb <br>
執行完之後確認有沒有產生 ./data/predict_not_full.csv 檔 <br>
並且執行完後會在資料夾當中產生 checkpoint model.pth

7. 按 Kernel / Run All 執行 8_output_result.ipynb <br>
執行完之後確認有沒有產生 ./result/result.csv 檔 <br>

./result/result.csv 檔即為對五十萬名消費者前三高消費金額類別預測資料

<br>
## lstm 模型
1. 進去 ./src/lstm 中

2. 依序跑以下檔案
  1. python make_dt.py (runtime > 1hr) 
  2. python buildnotna.py (~5min)
  3. python squeeze.py(~5min)
如果 python make_dt.py runtime 時間太長可以直接從下方連結將 data 放進 ./data 中 <br>
https://drive.google.com/drive/folders/1rCgVw0g4NGvcx0pPyeVnSiSya9hHT94O?fbclid=IwAR2nDKaUBgbJf1E2SrqOBheyi1BYf4bm-v2uoXgExn3o8WIJt1Q2FVajbj0

3. 確認這些檔案有沒有在 "./data" 裡面
  1. dt_all.csv
  2. dt_10to22_post.csv
  3. dt_less10_post.csv
  4. dt_only1_post.csv

4. Model 跑以下兩個 ipynb 檔
  1. LSTM.ipynb
  2. Regression.ipynb
<br>
並且執行完後會在資料夾當中產生 LSTM 的 checkpoint model.pth

  

5. 確認這些檔案有沒有在 "./result" 裡面
  1. result_all.csv
  2. result_10to22.csv
  3. result_less10.csv
  4. result_only1.csv

6. Result
<br>
python result.py
<br> 
確認是否生成 ./result/result.csv，./result/result.csv 即為對五十萬名消費者前三高消費金額類別預測資料

<br>
## TSNE 視覺化
1. 進去 ./src/tsne 中
2. 跑 lstm_tsne.ipynb <br>
這個程式會使用 lstm 抽取出來的 feature 來進行視覺化

3. python raw_data_tsne.py <br>
這個程式會直接使用預處理過後的消費比例來進行視覺化

## 環境：
1. python 3.7.0
2. pip 21.2.4
3. tqdm 4.62.3(for all_data_chunk.ipynb)
4. numpy 1.19.5
5. pandas 1.1.5
6. pytorch=1.9.0
7. torchvision 0.10.0
8. scikit-learn 0.22.2
9. functools
10. matplotlib 3.4.3
<br>
如果檔案有任何問題，可以至 https://github.com/yuanchiachang/ml-final-project <br>
git clone https://github.com/yuanchiachang/ml-final-project 以獲取程式碼 <br>
https://tbrain.trendmicro.com.tw/Competitions/Details/18 以獲取 6.7 GB 的訓練資料 train.csv

