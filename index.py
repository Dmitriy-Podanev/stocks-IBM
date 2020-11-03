import pandas as pd
import matplotlib.pyplot as plt

df_file = pd.read_csv("IBM.csv", sep=";", parse_dates=['<DATE>'], dayfirst=True, index_col="<DATE>")

new_sample = df_file.loc["2012":"2020", "<CLOSE>"]
plt.plot(new_sample)

plt.grid()
plt.show()
