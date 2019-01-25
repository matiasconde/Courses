## 1. Introduction ##

import csv
import linecache
import timeit

def brute_search(): 
    f = open("amounts.csv","r")
    reader = csv.reader(f)
    list_of_rows = []
    for i,line in enumerate(reader): 
        if i == 3 or i == 41230 or i == 284399:
            list_of_rows.append(line)
    return list_of_rows 

def cache_search():
    list_of_rows = []
    row1 = linecache.getline("amounts.csv",4)
    row41231 = linecache.getline("amounts.csv",41231)
    row284400 = linecache.getline("amounts.csv",284400)
    row_data1 = list(csv.reader([row1]))
    row_data2 = list(csv.reader([row41231]))
    row_data3 = list(csv.reader([row284400]))
    return row_data1 + row_data2 + row_data3

print(timeit.timeit('brute_search()','from __main__ import brute_search',number=50))
print(timeit.timeit('cache_search()','from __main__ import cache_search',number=50))

brute = brute_search()
cache = cache_search()
    
                                  

## 2. B-Tree Nodes ##

class Node:
    def __init__(self, keys=None, children=None):
        self.keys = keys
        self.children = children

    def __repr__(self):
        # Helpful method to keep track of Node keys.
        return "<BNode: {}>".format(self.keys)  
    
    def is_leaf(self):
        if not self.children:
            return True
        return False
 
class BTree:
    def __init__(self,degree=2):
        self.root = None
        self.degree=degree
        
b_node = Node(keys=[1,4,8])
node_is_leaf = b_node.is_leaf()
btree = BTree(degree=3)
btree.root = b_node

keys = btree.root.keys

## 3. Inserting into a Non-Full Node ##

class Node:
    def __init__(self, keys=None, children=None):
        self.keys = keys or []
        self.children = children or []
    
    def is_leaf(self):
        return len(self.children) == 0

    def __repr__(self):
        # Helpful method to keep track of Node keys.
        return "<Node: {}>".format(self.keys)    

class BTree:
    def __init__(self, t):
        self.t = t
        self.root = None
        
    def insert(self, key):
        # `insert` is given to you.
        self.insert_non_full(self.root, key)
    
    def insert_non_full(self,node,key):
        
        if node.is_leaf():
            if len(node.keys)>2*self.t-1:
                return
            
            index = 0
            for k in node.keys:
                if key > k: index += 1
                else: break
            node.keys.insert(index, key)
            return
        
        else:
            index = 0
            for k in node.keys:
                if key>k:
                    index += 1
                else: 
                    break
            self.insert_non_full(node.children[index],key)

# We have initialized a sample BTree for you.
btree = BTree(4)
b_node = Node(keys=[8, 16])
b_node.children.append(Node(keys=[2, 3, 5, 7]))
b_node.children.append(Node(keys=[9, 10, 11, 12]))
b_node.children.append(Node(keys=[17, 20, 44]))
btree.root = b_node

for i in [1,4,6,-1,13]:
    btree.insert(i)
child_keys = btree.root.children[1].keys

## 4. Inserting into a Full Node ##

class BTree(BaseBTree):
    def insert_non_full(self, node, key):
        if node.is_leaf():
            if len(node.keys) > 2*self.t - 1:
                # If it will exceed the maximum
                # don't add the key.
                return
            
            index = 0
            for k in node.keys:
                if key > k: index += 1
                else: break
            node.keys.insert(index, key)
            return
        
        index = 0
        for k in node.keys:
            if key > k: index += 1
            else: break
        
        if len(node.children[index].keys) == 2*self.t-1:
            left_node, right_node, key2 = self.split(node.children[index])
            node.keys.insert(index,key2)
            node.children[index]=left_node
            node.children.insert(index+1,right_node)
            if key > key2:
                index += 1
            
        self.insert_non_full(node.children[index], key)

    def split(self,node):
            keys = node.keys
            children = node.children
            left_node = Node(keys=keys[:len(keys)//2], children=children[:len(children)//2+1])
            right_node = Node(keys=keys[len(keys)//2:], children=children[len(children)//2+1:])
            key = right_node.keys.pop(0)
            return left_node, right_node, key
            
        
    
# We have initialized a sample BTree for you.
btree = BTree(4)
b_node = Node(keys=[8, 18])
b_node.children.append(Node(keys=[-3, -2, -1, 2, 3, 5, 7]))
b_node.children.append(Node(keys=[9, 10, 11, 12, 14, 18, ]))
b_node.children.append(Node(keys=[17, 20, 44]))
btree.root = b_node

for i in [1,4,6,13,17,22]:
    btree.insert(i)

child_keys = btree.root.children[1].keys

## 5. Expanding the Tree ##

class BTree(BaseBTree):
    def insert(self, key):
        if not self.root:
            self.root = Node(keys = [key], children = [])
            return 
        if len(self.root.keys) == 2*self.t-1:
            left_node, right_node, new_key = self.split(self.root)
            new_root = Node(keys = [new_key], children = [left_node,right_node])
            self.root = new_root
        self.insert_non_full(self.root, key)
                            
    def insert_multiple(self,keys):
        for key in keys:
            self.insert(key)
            
btree = BTree(5)
btree.insert_multiple(btree_keys)
child_keys = btree.root.children[-1].children[0].keys
                            

## 7. Searching the B-Tree ##

class BTree(BaseBTree):
    def search(self, node, term):
        if not self.root:
            return False
        index = 0
        for key in node.keys:
            if key == term:
                return True
            if term > key:
                index += 1
        if node.is_leaf():
            return False
        
        return self.search(node.children[index], term)
    
btree = BTree(4)
btree.insert_multiple(btree_keys)
search_6 = btree.search(btree.root,6)
search_73 = btree.search(btree.root,73)
search_101 = btree.search(btree.root,101)
        