import networkx as nx 
import pylab as py  
# Create blank graph  
D=nx.DiGraph()  
# Feed page link to graph  
D.add_weighted_edges_from([('A','B',1),('A','C',1),('C','A',1),('B','C',1)]) # Print page rank for each pages 
print (nx.pagerank(D)) 
nx.draw(D, with_labels=True) 
py.show()
