#!/usr/bin/env python
# coding: utf-8

# In[1]:


from numpy import inf

graph = {'A':{'E':3,'C':2,'D':1,'H':2},
         'B':{'F':1,'G':2},
         'C':{'A':2,'D':1,'F':2,'G':1},
         'D':{'A':1,'C':1,'F':1,'H':2},
         'E':{'A':3,'G':1},
         'F':{'H':3,'D':1,'C':2,'G':3,'B':1},
         'G':{'E':1,'C':1,'F':3,'B':2},
         'H':{'A':2,'D':2,'F':3}
        }
#Initialization, the costs of each node specified to INF at first
costs = {'A': 0, 'B': inf, 'C': inf, 'D': inf, 'E': inf, 'F': inf, 'G': inf,'H':inf}

parents = {}
print(graph['A']['E']) # Verifying the code


# In[2]:


get_ipython().run_cell_magic('html', '', '<img src="Images/Dijkstra.jpg",width=60,height=60>')


# In[3]:


#The method of searching each node's parent
def search(source, target, graph, costs, parents): 
    #set 'nextNode' variable points to 'source' start point
    nextNode = source
    
    #When the variable has not attain to the target
    while nextNode != target:
        #For each neighbor point of 'nextNode'
        for neighbor in graph[nextNode]:
            
            #graph['nextNode'][neighbor]+costs['nextNode'] < costs['neighbor']
            if graph[nextNode][neighbor] + costs[nextNode] < costs[neighbor]:
                
                #Updating the value of costs[neighbor] with graph['nextNode'][neighbor]
                costs[neighbor] = graph[nextNode][neighbor] + costs[nextNode]
                
                #Specifing the current 'nextNode' as neighbor node's parent node, then put into parents array
                parents[neighbor] = nextNode
            
            #Delete graph[neighbor][nextNode], which means delete reverse orientation from this current 'nextNode'    
            del graph[neighbor][nextNode]
        
        #Delete 'nextNode' in cost[], which means this node has not been candidate, been specified parent node already.
        del costs[nextNode]
        
        #Determine the shortest path for choosing next Node, then forward to next Node
        nextNode = min(costs, key=costs.get) # Syntax: min(a,b,c...[, key=func]) -> value
        
    return parents



def reversepath(source, target, searchResult):
    
    node = target
    
    backpath = [target]
    #Prepare a list for return path
    path = []
    
    while node != source:
        #Put every node's parent into backpath list
        backpath.append(searchResult[node])
        #Updating current node as former's parent (orientation: from 'destination' to 'start') for iteration
        node = searchResult[node]
        
    for i in range(len(backpath)):
        #Make an order
        path.append(backpath[-i - 1])
        
    return path


# In[4]:


input1 = input("Enter the START node: ")
Input1 = input1.upper()
input2 = input("Enter the END node: ")
Input2 = input2.upper()
result = search(Input1, Input2, graph, costs, parents)
print('Parent dictionary: {}'.format(result))
print('The shortest path is: {}'.format(reversepath(Input1, Input2, result)))


# In[ ]:




