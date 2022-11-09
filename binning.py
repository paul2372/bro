data=sorted(list(map(int,input("Enter the data : ").split())))
bin_count=round((max(data)-min(data))/len(data))
bin_size=len(data)//bin_count
bins=list()
for i in range(0,len(data),bin_size):
    bins.append(data[i:i+bin_size])
print(f"\nPartition into {bin_count} equi-depth bins : ")
for i in range(bin_count):
    print(f"Bin{i+1} : ",end="")
    print(*bins[i])
print(f"\nSmoothing by bin means : ")
for i in range(bin_count):
    print(f"Bin{i+1} : ",end="")
    print(*[round((sum(bins[i]))/len(bins[i])) for _ in range(len(bins[i]))])
print(f"\nSmoothing by bin boundaries : ")
for i in range(bin_count):
    print(f"Bin{i+1} : ",end="")
    print(*[bins[i][0] if abs(bins[i][0]-bins[i][j])<abs(bins[i][-1]-bins[i][j]) else bins[i][-1] for j in range(len(bins[i]))])