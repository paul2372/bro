import matplotlib.pyplot as plt
import csv
from scipy.cluster.hierarchy import dendrogram, linkage
with open('./data.csv', 'r') as file:
    data=list(csv.reader(file))
    del data[0]
file.close()

linkage_data = linkage(data, metric='euclidean',method='ward')
print(linkage_data)
dendrogram(linkage_data,labels=[f'p{i+1}' for i in range(len(data))])
plt.title("Hierarchical Clustering : Aglomerative")
plt.show()