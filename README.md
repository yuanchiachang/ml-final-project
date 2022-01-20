# ��i��l���
1. �N 6.7GB ����l�V�m��� train.csv ��b ./train ��Ƨ���

# �Q�� yaml �ɦw�����ҡB�Ұ�����
1. ���} environment.yml �ɡA�ھڹq���� anaconda3 �w�˪���m�A��� prefix: <anaconda3 �w�˸��|>\anaconda3\envs\ml_final_project_tbrain_2
1. �� anaconda prompt ����J conda env create -f environment.yml
2. activate ml_final_project_tbrain_2

# �p��N train data �����ܦh���p�ɮ�
1. �T�{�b ./train ��Ƨ����O�_�s�b train.csv 6.7GB ��l�V�m�ɮ�
2. �i�h ./src/nn ��
3. �� Kernel / Run All ���� 1_all_data_chunk.ipynb
���槹����b ./src/nn �̭����S�� Tbrain_splitData ��Ƨ��A�̭��n�� 330 �Ӥ��Ϋ᪺�ɮ�

# �έp��k�L simple baseline
1. �i�h ./src/nn ��
2. �� Kernel / Run All ���� 2_count_how_many.ipynb
���槹����T�{���S������ ./result/test_data.csv ��

./result/test_data.csv �ɧY���來�Q�U�W���O�̫e�T�����O���B���O�w�����

# neural network ��k
1. �i�h ./src/nn ��
2. �� Kernel / Run All ���� 3_count_most_label_customer.ipynb
���槹����T�{���S������ ./data/all_record.csv ��

3. �� Kernel / Run All ���� 4_classification.ipynb
���槹����T�{���S������ ./data/full_record.csv, ./data/not_full_record.csv,./data/empty_record.csv ��

4. �� Kernel / Run All ���� 5_reduce_training_data.ipynb
���槹����T�{���S������ ./data/reduced_train.csv ��

5. �� Kernel / Run All ���� 6_split_reduced_train.ipynb
���槹����T�{���S������ ./data/full_reduced_train.csv, ./data/not_full_reduced_train.csv ��

6. �� Kernel / Run All ���� 7_linear_model.ipynb
���槹����T�{���S������ ./data/predict_not_full.csv ��

7. �� Kernel / Run All ���� 8_output_result.ipynb
���槹����T�{���S������ ./result/result.csv ��

./result/result.csv �ɧY���來�Q�U�W���O�̫e�T�����O���B���O�w�����

# lstm ��k
1. �i�h ./src/lstm ��

2. �̧Ƕ]�H�U�ɮ�
  (1). python make_dt.py 
  (2). python buildnotna.py
  (3). python squeeze.py

3. �T�{�o���ɮצ��S���b "./data" �̭�
  (1). dt_all.csv
  (2). dt_10to22_post.csv
  (3). dt_less10_post.csv
  (4). dt_only1_post.csv

4. Model
�]�H�U��� ipynb ��
  (1). LSTM.ipynb
  (2). Regression.ipynb

5. �T�{�o���ɮצ��S���b "./result" �̭�
1. result_all.csv
2. result_10to22.csv
3. result_less10.csv
4. result_only1.csv

6. Result
python result.py 
�T�{�O�_�ͦ� ./result.csv�A./result.csv �Y���來�Q�U�W���O�̫e�T�����O���B���O�w�����

# TSNE �����k
1. �i�h ./src/tsne ��
2. �] lstm_tsne.ipynb
�o�ӵ{���|�ϥ�lstm����X�Ӫ�feature�Ӷi���ı��

3. python raw_data_tsne.py
�o�ӵ{���|�����ϥιw�B�z�L�᪺���O��ҨӶi���ı��

# ���ҡG
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
