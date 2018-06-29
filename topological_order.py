import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

def plot_graph(grafo):
    n=len(grafo)    
    nxGraph=nx.DiGraph()
    for i in range(n):
        for j in grafo[i]:
            nxGraph.add_edge(i,j)
    labels={}
    for i in range(n):
        labels[i]=str(i)
    pos=nx.spring_layout(nxGraph)
    nodeList=range(n)
    nx.draw_networkx_nodes(nxGraph,pos,node_color='r',node_size=500)
    nx.draw_networkx_edges(nxGraph,pos,width=1.0,alpha=0.5,arrows=True)
    nx.draw_networkx_labels(nxGraph,pos,labels,font_size=16)
    plt.axis('off')
    plt.savefig("Grafo.eps")
    print("O grafo percorrido foi gerado no arquivo Grafo.eps")    

def top_sort(grafo):
    n=len(grafo)
    topSort=-np.ones([n])    
    numberIncomeEdges=np.zeros([n])
    setOfNodesWithNoActiveEdges=set()
    # Loop O(m+n)
    for i in range(n):
        for j in grafo[i]:
            numberIncomeEdges[j]=numberIncomeEdges[j]+1
    #O(n)
    for i in range(n):
        if(numberIncomeEdges[i]==0):
            setOfNodesWithNoActiveEdges.add(i)
    i=0
    #O(m+n)
    while((i<n) and (len(setOfNodesWithNoActiveEdges)!=0)):
        i=i+1
        node=setOfNodesWithNoActiveEdges.pop()
        topSort[i-1]=node
        for j in grafo[node]:
            numberIncomeEdges[j]=numberIncomeEdges[j]-1
            if(numberIncomeEdges[j]==0):
                setOfNodesWithNoActiveEdges.add(j)

    if(i!=n):
        print ("O grafo não é Acíclico!")
    else:
        print("Melhor ordenação topográfica: ")
        print (topSort)        

if __name__ == '__main__':

    """
    n=8 # número de nós

    grafo=[set() for i in range(n)]

    grafo[0].add(1) # 7 -> 11
    grafo[0].add(2) # 7 -> 8
    grafo[1].add(7) # 11 -> 2
    grafo[1].add(5) # 11 -> 9
    grafo[1].add(6) # 11 -> 10
    grafo[2].add(5) # 8 -> 9
    grafo[3].add(1) # 5 -> 11
    grafo[4].add(2) # 3 -> 8
    grafo[4].add(6) # 3 -> 10
    """
    
    """
    n=6 # número de nós

    grafo=[set() for i in range(n)]
    grafo[0].add(1)
    grafo[0].add(2)
    grafo[1].add(0)
    grafo[1].add(3)
    grafo[2].add(0)
    grafo[2].add(4)
    grafo[3].add(1)
    grafo[3].add(5)
    grafo[4].add(2)
    grafo[4].add(5)
    grafo[5].add(3)
    grafo[5].add(4)
    """

    """
    n=7 #number of nodes

    grafo=[set() for i in range(n)]

    grafo[0].add(3)
    grafo[0].add(4)
    grafo[0].add(6)    
    grafo[1].add(2)
    grafo[1].add(4)
    grafo[1].add(5)    
    grafo[2].add(3)
    grafo[2].add(4)
    grafo[3].add(4)
    grafo[4].add(5)
    grafo[4].add(6)
    grafo[5].add(6)
    """

    plot_graph(grafo)

    top_sort(grafo)