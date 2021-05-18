import pandas as pd 

MAX_SEQ_LEN = 128

df = pd.read_csv("news.csv")

out_df = pd.DataFrame(data=dict())
for field in ['title', 'text', 'label']:
    out_df[field] = [" ".join(s.split()[:MAX_SEQ_LEN]) for s in df[field]]

s1 = list(df['title'])
s2 = list(df['text'])
out_df['titletext'] = [" ".join((s1[i] + " " + s2[i]).split()[:MAX_SEQ_LEN]) for i in range(len(df))]

split = [0.8, 0.1, 0.1]
n = len(out_df)
n_train = int(n * split[0])
n_valid = int(n * split[1])

train = out_df[:n_train]
valid = out_df[n_train: n_train + n_valid]
tests = out_df[n_train + n_valid:]

train.to_csv("train.csv", index=None)
valid.to_csv("valid.csv", index=None)
tests.to_csv("test.csv", index=None)