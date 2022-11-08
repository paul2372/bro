import random #To randomly guess k means

datapoints=list(map(int,input("Enter the datapoints: ").split()))
k=int(input("Specify the number of clusters: "))
mean=[(random.randint(0,max(datapoints)))  for _ in range(k)] #Randomly assing k means

while True:
    near=list() #To store the diff of every data point from each mean
    clusters=[list() for _ in range(k)] #Create k clusters
    for m in mean:
        near.append([abs(point-m) for point in datapoints])
    for i in range(len(datapoints)):
        calc=[near[j][i] for j in range(k)] #Calculate the distance of data-point from all means
        belongs=calc.index(min(calc)) #Calculate nearest mean
        clusters[belongs].append(datapoints[i]) #Assign to a cluster
    nm=list() #To calculate new mean
    for cluster in clusters:
        try:
            nm.append(sum(cluster)/len(cluster)) #Calculate new means
        except:
            nm.append(0) #If mean is 0
    if nm==mean: #Check if new men=an and old mean are same
        break
    mean=nm

print("\nThe clusters formed are:")
for i in range(k):
    print(f"Cluster{i+1} : ",end="")
    print(*clusters[i])