## 2. Heap Inserts ##

class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        # Helpful method to keep track of Node values.
        return "<Node: {}>".format(self.value)    

class MaxHeap:
    def __init__(self):
        self.root = None
    
    def insert(self,value):
        node = Node(value)
        if not self.root:
            self.root = node
        elif not self.root.left:
            self.root.left = node
            node.parent = self.root
            if value > node.parent.value:
                old_root = self.root
                self.root = node
                node.left = old_root
                old_root.parent = node
        elif not self.root.right:
            self.root.right = node
            node.parent = self.root
            if value > node.parent.value:
                old_root = self.root
                old_left = self.root.left
                self.root = node
                node.right = old_root
                node.left = old_left
                old_root.parent = node
                old_left.parent = node 
        return node
                
heap = MaxHeap()

heap.insert(3)
heap.insert(9)
heap.insert(11)

root = heap.root.value
left = heap.root.left.value
right = heap.root.right.value

## 3. Speed Up Insert ##

from math import floor

class MaxHeap:
    def __init__(self):
        self.nodes = []
        
    def insert(self,value):
        self.nodes.append(value)
        index = len(self.nodes)-1
        if index>0:
            parent_index = floor((index-1)/2)
            if value>self.nodes[parent_index]:
                old_parent = self.nodes[parent_index]
                self.nodes[parent_index] = value
                self.nodes[index] = old_parent           
    
    # Add your new `insert` method here.
    
heap = MaxHeap()

heap.insert(3)
heap.insert(9)
heap.insert(11)

nodes = heap.nodes

## 4. Get the Max Integer ##

class MaxHeap(BaseMaxHeap):
    def insert_multiple(self,values):
        for value in values:
            self.insert(value)
     
    def max(self):
        return max(self.nodes)
    
heap = MaxHeap()
heap.insert_multiple(heap_list)
heap_max = heap.max()

## 5. Pop the Root Value ##

class MaxHeap(BaseMaxHeap):
    def pop(self):
        root = self.nodes[0]
        self.nodes[0] = self.nodes[-1]
        self.nodes = self.nodes[:-1]
        index = 0
        
        while max(2*index+1,2*index+2) < len(self.nodes) - 1:
            if self.nodes[2*index+1] == max(self.nodes[2*index+1],self.nodes[2*index+2]):
                swap_index = 2*index+1
                self.nodes[index], self.nodes[swap_index] = self.nodes[swap_index], self.nodes[index]
                index = swap_index
            elif self.nodes[2*index+2]==max(self.nodes[2*index+1],self.nodes[2*index+2]):
                swap_index = 2*index+2
                self.nodes[index], self.nodes[swap_index] = self.nodes[swap_index], self.nodes[index]
                index = swap_index
        return root
        
        
        
    
heap = MaxHeap()
heap.insert_multiple(heap_list)
heap_max = heap.pop()

## 6. Grab the Top N Elements ##

class MaxHeap(BaseMaxHeap):
    
    def top_n_elements(self,n):
        lista = []
        for i in range(n):
            lista.append(self.pop())
        return lista
       
heap = MaxHeap()
heap.insert_multiple(heap_list)
top_100 = heap.top_n_elements(100)


## 7. Using Python's Heap ##

import csv
import heapq

f = open("amounts.csv","r")
reader = csv.reader(f)

amounts = [line for line in reader]

top_100 = heapq.nlargest(100,amounts[1:], key=lambda x: x[1])

## 8. Analyzing the Heap ##

heap_list = list(range(10 * 100 * 5000))
random.shuffle(heap_list)
    
start = time.time()
sorted(heap_list, reverse=True)[:100]
print("Sorting search took: {} seconds".format(time.time() - start))
print(time.time() - start)
print(" ")
start = time.time()
heapq.nlargest(100, heap_list)
print("Heap search took: {} seconds".format(time.time() - start))
print(time.time() - start)