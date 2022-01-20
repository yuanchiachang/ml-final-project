'''
Squeeze every 16D vector to the right (dt=23), order remained
Output:
./data/dt_10to22_post.csv
./data/dt_less10_post.csv
./data/dt_only1_post.csv
'''
import numpy as np
import pandas as pd

def squeeze_df(case):
    df = pd.read_csv("./data/dt_%s.csv" % case)
    df_dt = df.iloc[:, 23:0:-1]
    #print(df_dt)
    def squeeze_nan(x):
        original_columns = x.index.tolist()
        #print(original_columns)
        squeezed = x.dropna()
        squeezed.index = [original_columns[n] for n in range(squeezed.count())]

        return squeezed.reindex(original_columns, fill_value=np.nan)
    df_squeeze = df_dt.apply(squeeze_nan, axis=1)
    #print(df_squeeze)
    df_chid = df[["chid"]]
    result = pd.concat([df_chid, df_squeeze.iloc[:, ::-1]], axis=1)
    #print(result)
    result.to_csv("./data/dt_%s_post.csv" %case, index=False)

squeeze_df("only1")
squeeze_df("10to22")
squeeze_df("less10")