import csv,pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("./data.csv")
data=df.values.tolist()

df = pd.DataFrame(data, columns = ['Id', 'Gender','Age', 'Sales','Bmi', 'Income'])
df.hist()
plt.show()
