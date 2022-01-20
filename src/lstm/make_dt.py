'''
Load the original training data file, considering only "shop_tag" and "txn_amt"
Convert every chid into a 16D vector representing the "shop type propotion" in one dt
Output: ./data/dt/dt1.csv ~ ./data/dt/dt23.csv, containing chid and their 16D vector
'''
import pandas as pd

def load_train(x, path='../../train/train.csv'):
    chunksize = 2 * 10 ** 6
    columns = ["shop_tag"]
    flag = 0
    count = 0
    dt_temp = pd.DataFrame()
    for chunk in pd.read_csv(path, chunksize=chunksize):
        count += 1
        dt1 = chunk.loc[chunk["dt"] == x]
        dt1 = dt1[["dt", "chid", "shop_tag", "txn_amt"]]
        dt1['shop_tag'] = pd.to_numeric(dt1['shop_tag'], errors='ignore')
        print(flag, end=" ")
        #return dt1

        if (not(dt1.empty)) & (flag == 0):
            dt_temp = dt1
            flag = 1
            #print(dt_temp)
        elif (dt1.empty) & (flag == 1):
            #print("hi")
            print("the result for %d is " % x, dt_temp)
            return dt_temp
        elif (not(dt1.empty)) & (flag == 1):
            #print("hiel")
            print("the result for %d is " % x, pd.concat([dt_temp, dt1]))
            return pd.concat([dt_temp, dt1])
          

def filter_rows_by_values(df, col, values):
    return df[df[col].isin(values)]

def add_result(df, x):
    new_col = "dt%d" %x
    res_list =[]
    for i in range(len(df)):
        tag_list = [int(x) for x in (df.iloc[[i]]["shop_tag"].tolist()[0])]
        tag_list.sort()
        #print(tag_list)
        #break
        txn_list = [float("{:.2f}".format(x)) for x in (df.iloc[[i]]["txn_amt"].tolist()[0])]
        result = [0 for i in range(16)]
        type_list = [2,6,10,12,13,15,18,19,21,22,25,26,36,37,39,48]
        count = 0
        for k in range(len(type_list)):
            if (tag_list[count] == type_list[k]):
                result[k] = txn_list[count]
                count += 1
            if (count == len(tag_list)):
                break
        #print(tag_list, txn_list)
        #print(result)
        sum_res = sum(result)
        #print(sum_res)
        for j in range(len(result)):
            result[j] /= sum_res
        
        result = [float("{:.4f}".format(x)) for x in result]
        #print(str(result))
        res_list.append(result)
    df[new_col] = res_list
    return df

def make_dt(dt):
  new_col = "dt%d" % dt
  df = load_train(dt)
  df = filter_rows_by_values(df, "shop_tag", ["2","6","10","12","13","15","18","19","21","22","25","26","36","37","39","48"])
  df = df.groupby('chid').agg(tuple).applymap(list).reset_index()
  df = add_result(df, dt)
  df = df[["chid", new_col]]
  path = "./data/dt/dt%d.csv" % dt
  df.to_csv(path, index=False)
  print("done %d" % dt)
  return 0

for i in range(1,24):
    make_dt(i)