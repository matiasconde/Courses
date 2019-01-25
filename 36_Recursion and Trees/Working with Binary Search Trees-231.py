## 1. Introduction to Binary Search Trees ##

class Node:
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value
    
    def __str__(self):
        return "<Node: {}>".format(self.value)

class BST:
    def __init__(self):
        self.node = None
    
    def inorder(self,tree):
        if not tree or not tree.node:
            return []
        return (self.inorder(tree.node.left) + [tree.node.value] + self.inorder(tree.node.right))        
        
    def insert(self,value):
        node = Node(value=value)
        if not self.node:
            self.node = node
            self.node.left = BST()
            self.node.right = BST()
            return 
        if value > self.node.value: 
            #if self.node.right:
            self.node.right.insert(value)
            return
        
        if value <= self.node.value:
           #3if self.node.left:
            self.node.left.insert(value)
            return
        
    def inorder(self, tree):
        if not tree or not tree.node:
            return []
        return (
            self.inorder(tree.node.left) +
            [tree.node.value] +
            self.inorder(tree.node.right)
        )
    

bst = BST()
for i in [4,2,1,5,3]: 
    bst.insert(i)

sorted_order = bst.inorder(bst)
root = bst.node.value       
"""
bst = BST()
bst.node = Node(1)
bst.node.right = BST()
bst.node.right.node = Node(333)
print(bst.node.right.node)
if bst.node.right: print(444)
else: 
    bst.node.right.node = Node(4)
    print(bst.node.right.node)"""

## 2. Insert Multiple and Sorted Order ##

class BST(BaseBST):
    def inorder(self,tree):
        if not tree or not tree.node:
            return []
        return (self.inorder(tree.node.left) + [tree.node.value] + self.inorder(tree.node.right))     
    
    def insert_multiple(self,values):
        for value in values: 
            self.insert(value)
            
bst = BST()
bst.insert_multiple(bst_values)
sorted_inorder = bst.inorder(bst)


## 3. Searching the BST ##

class BST(BaseBST):
    def search(self,value):
        node = self.node
        if not node: 
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return node.left.search(value)
        else: 
            return node.right.search(value)
        

bst = BST()
bst.insert_multiple(bst_values)
does_exist_1 = bst.search(1)
does_exist_75 = bst.search(75)
does_exist_101 = bst.search(101)

## 4. Why We Need a Balanced BST ##

class BST(BaseBST):
    def depth(self,node):
        if not node: 
            return 0
        if not node.left and not node.right:
            return 1
        if not node.left: node.left = BST()
        if not node.right: node.right = BST()
            
        return 1 + max(self.depth(node.left.node),self.depth(node.right.node))
        
    def is_balanced(self):
        if not self.node: 
            return True
        
        left_subtree = self.node.left
        right_subtree = self.node.right
        
        if not left_subtree: left_subtree = BST()
        if not right_subtree: right_subtree = BST()        
        
        if abs(left_subtree.depth(left_subtree.node) - right_subtree.depth(right_subtree.node))<2:
            return True and (left_subtree.is_balanced()) and (right_subtree.is_balanced())
        return False
        

bst = BST()
bst.insert_multiple(bst_values)
balanced = bst.is_balanced()
"""
bst = BST()

bst.insert(1)
bst.insert(2)
bst.insert(3)
bst.insert(0)
print(bst.depth(bst.node))
balanced = bst.is_balanced()
"""

## 5. Maintaining a Balance (Part 1) ##

class BST(BaseBST):
    def left_rotate(self):
        old_node = self.node
        new_node = self.node.right.node
        if not new_node:
            return
        
        new_right_subnode = new_node.left.node
        self.node = new_node
        new_node.left.node = old_node
        old_node.right.node = new_right_subnode
        
    def right_rotate(self):
        old_node = self.node
        new_node = self.node.left.node
        if not new_node: 
            return
        new_left_subnode = new_node.right.node
        self.node = new_node
        new_node.right.node = old_node
        old_node.left.node = new_left_subnode


bst = BST()
bst.insert_multiple(bst_values)
bst.left_rotate()
print(bst.inorder(bst))
left_balanced = bst.is_balanced()
bst.right_rotate()
print(bst.inorder(bst))
right_balanced = bst.is_balanced()

## 7. Maintaining a Balance (Part 3) ##

class BST(BaseBST):
    def insert(self, value=None):
        node = Node(value=value)
        if not self.node:
            self.node = node
            self.node.left = BST()
            self.node.right = BST()
            return
        
        if value > self.node.value:
            if self.node.right:
                self.node.right.insert(value=value)
            else: # este else en realidad nunca se alcanza
                self.node.right.node = node
        else:
            if self.node.left:
                self.node.left.insert(value=value) 
            else: # este else en realidad nunca se alcanza
                self.node.left.node = node
            
        difference = self.depth(self.node.left.node) - self.depth(self.node.right.node)
        
        if difference > 1: # para entrar acá está desbalanceado a izquierda
            # Left-right case.
            if value > self.node.left.node.value: # si el valor último insertado es mayor al nodo izquierdo quiere decir que tenemos el caso left-right, hay que rotar a izquierda, y luego a derecha.
                self.node.left.left_rotate()
            # Left-left case.
            self.right_rotate()
            
        # Right side case.
        if difference < -1: # para entrar acá está desbalanceado a izquierda
            # Right-left case.
            if value <= self.node.right.node.value: # si el valor último insertado es mayor al nodo derecho quiere decir que tenemos el caso right-left, hay que rotar a derecha, y luego a izquierda.
                self.node.left.right_rotate()
            self.left_rotate()
                
bst = BST()

bst.insert_multiple(bst_values)
"""
bst.insert(9)
bst.insert(10)
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(8)
bst.insert(11)
bst.insert(12)
bst.insert(13)
bst.insert(14)
bst.insert(15)
"""
inorder = bst.inorder(bst)
is_bst_balanced = bst.is_balanced()

## 8. Enhancing the Node and BST Class ##

class BST(BaseBST):
    def __init__(self, index=None):
        self.node = None
        self.index = index
        
    def search(self,key):
        node = self.node
        if not node: 
            return False
        if key == node.value.key:
            return True
        elif key < node.value.key:
            return node.left.search(key)
        else: 
            return node.right.search(key)
        
    def insert(self, value=None):
        key = value
        if self.index:
            key = value[self.index]            
        node = Node(key=key,value=value)
        if not self.node:
            self.node = node
            self.node.left = BST(index = self.index)
            self.node.right = BST(index = self.index)
            return
        
        if key > self.node.key:
            if self.node.right:
                self.node.right.insert(value=value)
            else: # este else en realidad nunca se alcanza
                self.node.right.node = node
        else:
            if self.node.left:
                self.node.left.insert(value=value) 
            else: # este else en realidad nunca se alcanza
                self.node.left.node = node
            
        difference = self.depth(self.node.left.node) - self.depth(self.node.right.node)
        
        if difference > 1: 
            if key > self.node.left.node.key: 
                self.node.left.left_rotate()
            # Left-left case.
            self.right_rotate()
            
        # Right side case.
        if difference < -1: 
            # Right-left case.
            if key <= self.node.right.node.key: 
                self.node.left.right_rotate()
            self.left_rotate()
            
  
bst = BST()
bst.insert_multiple(bst_values)
inorder = bst.inorder(bst)

bst_list = BST(index=2)
bst_list.insert_multiple(bst_list_values)
inorder_list = bst.inorder(bst_list)

## 9. Adding the Range Query ##

class BST(BaseBST):
    def greater_than(self,key):
        if not self.node: 
            return []
        if self.node.key > key:
            return self.node.left.greater_than(key) + self.node.right.greater_than(key) + [self.node.value]
        return self.node.left.greater_than(key) + self.node.right.greater_than(key)
        
bst = BST()
bst.insert_multiple(bst_values)
greater = bst.greater_than(5)

bst_list = BST(index=2)
bst_list.insert_multiple(bst_list_values)
greater_list = bst_list.greater_than(5)

## 10. Range Querying a CSV ##

# The BST and Node class is given to you.
bst = BST()  # Change the index here.

f = open("amounts.csv","r")
csvreader = csv.reader(f)
amount_rows = []
for line in list(csvreader)[1:]:
    amount_rows.append((line[0],float(line[1])))
bst = BST(index=1)
bst.insert_multiple(amount_rows)
csv_query = bst.greater_than(10)