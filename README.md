# Final Report 操作方法介紹
## 放進原始資料
1. 將 6.7GB 的原始訓練資料 train.csv 放在 ./train 資料夾中

## 利用 yaml 檔安裝環境、啟動環境
1. 打開 environment.yml 檔，根據電腦中 anaconda3 安裝的位置，更改 prefix: <anaconda3 安裝路徑>\anaconda3\envs\ml_final_project_tbrain_2
1. 到 anaconda prompt 中輸入 conda env create -f environment.yml
2. activate ml_final_project_tbrain_2

## 如何將 train data 切成很多的小檔案
1. 確認在 ./train 資料夾中是否存在 train.csv 6.7GB 原始訓練檔案
2. 進去 ./src/nn 中
3. 按 Kernel / Run All 執行 1_all_data_chunk.ipynb
執行完之後在 ./src/nn 裡面有沒有 Tbrain_splitData 資料夾，裡面要有 330 個切割後的檔案

## 統計方法過 simple baseline
1. 進去 ./src/nn 中
2. 按 Kernel / Run All 執行 2_count_how_many.ipynb
執行完之後確認有沒有產生 ./result/test_data.csv 檔

./result/test_data.csv 檔即為對五十萬名消費者前三高消費金額類別預測資料

## neural network 模型
1. 進去 ./src/nn 中
2. 按 Kernel / Run All 執行 3_count_most_label_customer.ipynb
執行完之後確認有沒有產生 ./data/all_record.csv 檔

3. 按 Kernel / Run All 執行 4_classification.ipynb
執行完之後確認有沒有產生 ./data/full_record.csv, ./data/not_full_record.csv,./data/empty_record.csv 檔

4. 按 Kernel / Run All 執行 5_reduce_training_data.ipynb
執行完之後確認有沒有產生 ./data/reduced_train.csv 檔

5. 按 Kernel / Run All 執行 6_split_reduced_train.ipynb
執行完之後確認有沒有產生 ./data/full_reduced_train.csv, ./data/not_full_reduced_train.csv 檔

6. 按 Kernel / Run All 執行 7_linear_model.ipynb
執行完之後確認有沒有產生 ./data/predict_not_full.csv 檔

7. 按 Kernel / Run All 執行 8_output_result.ipynb
執行完之後確認有沒有產生 ./result/result.csv 檔

./result/result.csv 檔即為對五十萬名消費者前三高消費金額類別預測資料

## lstm 模型
1. 進去 ./src/lstm 中

2. 依序跑以下檔案
  (1). python make_dt.py 
  (2). python buildnotna.py
  (3). python squeeze.py

3. 確認這些檔案有沒有在 "./data" 裡面
  (1). dt_all.csv
  (2). dt_10to22_post.csv
  (3). dt_less10_post.csv
  (4). dt_only1_post.csv

4. Model
跑以下兩個 ipynb 檔
  (1). LSTM.ipynb
  (2). Regression.ipynb

5. 確認這些檔案有沒有在 "./result" 裡面
1. result_all.csv
2. result_10to22.csv
3. result_less10.csv
4. result_only1.csv

6. Result
python result.py 
確認是否生成 ./result.csv，./result.csv 即為對五十萬名消費者前三高消費金額類別預測資料

## TSNE 視覺化
1. 進去 ./src/tsne 中
2. 跑 lstm_tsne.ipynb
這個程式會使用lstm抽取出來的feature來進行視覺化

3. python raw_data_tsne.py
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

