'''
count amount of dts that each chid has record in, and split into 4 cases
./data/dt_all.csv: chids with record in every dt
./data/dt_10to22.csv: chids with record in 10~22 dts
./data/dt_less10.csv: chids with record in 2~10 dts
./data/dt_only1.csv: chids with record in only 1 dt
'''
from functools import reduce
import pandas as pd

df_list = []
for i in range(1,24):
    path = "./data/dt/dt%d.csv" %i
    df_list.append(pd.read_csv(path))
df_merged = reduce(lambda left,right: pd.merge(left,right,on="chid",how='outer'), df_list)

def count_notna(df_merged):
    na_list = []
    for i in range(1,24):
        col_name = "dt%d" %i
        na_list.append(df_merged[col_name].notna())
    count_list = []
    for j in range(len(df_merged)):
        count = 0
        for k in range(len(na_list)):
            #print()
            if na_list[k].iloc[j] == True:
                count += 1
        count_list.append(count)
    df_merged["count"] = count_list
    return df_merged

df_merged = count_notna(df_merged)
dt_all = df_merged.loc[df_merged['count'] == 23].drop("count", 1).to_csv("./data/dt_all.csv", index=False)
dt_10to22 = df_merged.loc[(df_merged['count'] >= 10) & (df_merged['count'] <= 22)].to_csv("./data/dt_10to22.csv", index=False)
dt_less10 = df_merged.loc[(df_merged['count'] >= 2) & (df_merged['count'] <= 9)].to_csv("./data/dt_less10.csv", index=False)
dt_only1 = df_merged.loc[df_merged['count'] == 1].to_csv("./data/dt_only1.csv", index=False)
print(pd.value_counts(df_merged["count"]))