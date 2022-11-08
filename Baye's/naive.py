import csv

with open('./data.csv','r') as file:
    data=list(csv.reader(file))
    del data[0]
file.close()

classes=list()
for sample in data:
    if sample[-1] not in classes:
        classes.append(sample[-1])

observations=dict()
for cls in classes:
    observations[cls]={}
    observations[cls]['count']=sum([1 if sample[-1]==cls else 0 for sample in data])

for i in range(len(data)):
    for j in range(len(data[0])-1):
        try:
            observations[data[i][-1]][data[i][j]]+=1
        except:
            observations[data[i][-1]][data[i][j]]=1
sample=list(map(str,(input("Enter an unseen sample : ").lower()).split()))
calculations=dict()
for cls in classes:
    calculations[cls]=1
    for val in sample:
        try:
            calculations[cls]*=observations[cls][val]/observations[cls]['count']
        except:
            calculations[cls]=0
    calculations[cls]*=observations[cls]['count']/len(data)
for val in calculations:
    print(f'P({val}|X) = {calculations[val]}')

print(f"The given data sample belongs to class {max(calculations.items(), key=lambda x:x[1])[0]}")