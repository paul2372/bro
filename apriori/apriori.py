import itertools,numpy,csv
with open("./apri_data.csv", 'r') as file:
    transactions = list(csv.reader(file))
    items=data=[[trans] for trans in transactions[0]]
    del transactions[0]
file.close()
min_support=(int(input("Enter the minimun support (in %): ")))/100
thrs_conf=(int(input("Enter the minimun confidence (in %): ")))/100
size=len(transactions)
iteration=1
store=dict()
database=list()
while True:
    itemset=dict()
    for item in items:
        support=0
        for trans in transactions:
            if len(set([trans.count(char) for char in item]))==1:
                support+=[trans.count(char) for char in item][0]
        if support/len(transactions)>=min_support:
            itemset[(''.join(f'{i} ' for i in item)).rstrip()]=support/len(transactions)
    store.update(itemset)
    datapoints=''.join(f'{item} ' for item in list(itemset.keys())).rstrip()
    data=sorted(list(set(datapoints.split(' '))))
    iteration+=1
    items=[''.join(f'{i} ' for i in list(i)).rstrip().split(' ') for i in itertools.combinations(data, iteration)]
    if len(itemset)==0:
        itemset=database[-1]
        break
    database.append(itemset)
print(store)
items=[item.split(' ') for item in itemset.keys()]
final=list()
print("The final rules are : ")
for rule in items:
    confidence=dict()
    for i in range(len(rule)-1):
        for elem in list(list(j) for j in itertools.combinations(rule,i+1)):
            confidence[(''.join(f'{char} ' for char in elem)).rstrip()]=(''.join(f'{char} ' for char in numpy.setdiff1d(rule,elem))).rstrip()
    for rule in confidence:
        if (store[''.join(f'{char} ' for char in sorted(f'{rule} {confidence[rule]}'.split(' '))).rstrip()]/store[rule])>=thrs_conf:
            print(f'{rule} --> {confidence[rule]}')
