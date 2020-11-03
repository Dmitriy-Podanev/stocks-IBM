import pandas as pd
import matplotlib.pyplot as plt

df_file = pd.read_csv("IBM.csv", sep=";", parse_dates=['<DATE>'], dayfirst=True, index_col="<DATE>")
vol=[]
cls=[]
for i in df_file.index:
   vol.append(df_file.loc[f"{i}", "<VOL>"])
   print(df_file.loc[f"{i}", "<VOL>"])

plt.plot(df_file.index,vol)

plt.grid()
plt.show()
