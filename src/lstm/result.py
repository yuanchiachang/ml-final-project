import pandas as pd

df1 = pd.read_csv("./result/result_all.csv")
df2 = pd.read_csv("./result/result_10to22.csv")
df3 = pd.read_csv("./result/result_less10.csv")
df4 = pd.read_csv("./result/result_only1.csv")

#inverse the predicted result of LSTM
# (3rd, 2nd, 1st) => (1st, 2nd, 3rd)
df1.loc[:,['top1','top3']] = df1.loc[:,['top3','top1']].values
df2.loc[:,['top1','top3']] = df2.loc[:,['top3','top1']].values

result = pd.concat([df1, df2, df3, df4])

# assign result for chid with no shopping record in any dt
# using the top 3 most frequent shop type
for i in range(10000000, 10500000):
    if result.loc[result["chid"] == i].empty:
        result = result.append({"chid": i, "top1" : "37", "top2" : "2", "top3": "48"}, ignore_index=True)

result = result.astype({"chid": str, "top1" : str, "top2" : str, "top3": str})
result = result.sort_values(by=["chid"])
result.to_csv("result.csv", index=False)