## 1. Introduction ##

class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root
    
    def insert(self,value):
        if self.root == None:
            self.root = Node(value=value)
        elif self.root.left == None:
            self.root.left = Node(value=value)
        elif self.root.right == None: 
            self.root.right = Node(value=value)

tree = BinaryTree(root = Node(value=1))

for i in range(2,5):
    tree.insert(i)

root = tree.root.value
left = tree.root.left.value
right = tree.root.right.value
            

## 2. Multiple Inserts ##

level_order = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        # Helpful method to keep track of Node values.
        return "<Node: {}>".format(self.value)    

class BinaryTree:
    def __init__(self, values=None):
        self.root = None
        if values:
            self.insert(values)
    
    def insert(self,values,index=0):
        node = None
        if index < len(values):
            node = Node(values[index])
            if self.root == None:
                self.root = node
            node.left = self.insert(values,index = 2*index + 1)
            node.right = self.insert(values,index = 2*index + 2)
        return node
    
tree = BinaryTree(level_order)
root = tree.root.value
child = tree.root.left.right.left.value


## 3. Interior, Child, and Parent Nodes ##

level_order = [1, 2, 3, 4, 5]

class BinaryTree(BaseBinaryTree):
    pass  # no-op method that let's us declare our tree.
    
    def is_parent(self,node):
        if self.root == node:
            return True
        if node.right or node.left: 
            return True
        else: 
            return False
        
    def is_interior(self,node):
        if self.root == node: 
            return False
        if self.root and (node.left or node.right):
            return True
        else: 
            return False
        
    def is_leaf(self,node):
        if (node.left == None) and (node.right == None):
            return True
        else: 
            return False
        
tree = BinaryTree(level_order)

root_parent = tree.is_parent(tree.root)
parent = tree.is_parent(tree.root.left)
interior = tree.is_interior(tree.root.left)
root_leaf = tree.is_leaf(tree.root)
leaf = tree.is_leaf(tree.root.left.left)

## 4. Traversing the Tree ##

level_order = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

class BinaryTree(BaseBinaryTree):
    def preorder_traverse(self, node):
        if not node:
            return []
        lista_de_nodos = [node.value]
        lista_de_nodos += self.preorder_traverse(node.left)
        lista_de_nodos += self.preorder_traverse(node.right)
        return lista_de_nodos
    
    def inorder_traverse(self,node):
        if not node:
            return []       
        return (self.preorder_traverse(node.left) + [node.value] + self.preorder_traverse(node.right))

    def inorder_traverse_v2(self,node):
        if not node:
            return []       
        return (self.inorder_traverse_v2(node.left) + [node.value] + self.inorder_traverse_v2(node.right))
    
    def postorder_traverse(self,node):
        if not node:
            return []
        return (self.postorder_traverse(node.left) + self.postorder_traverse(node.right) + [node.value])
    
        
tree = BinaryTree(level_order)
preorder = tree.preorder_traverse(tree.root)
inorder = tree.inorder_traverse(tree.root)
postorder = tree.postorder_traverse(tree.root)
inorder_v2 = tree.inorder_traverse_v2(tree.root)

## 5. Finding Total Nodes and Depth ##

class BinaryTree(BaseBinaryTree):
    def depth(self,node):
        if not node:
            return 0
        return max(self.depth(node.left),self.depth(node.right)) + 1
    
    def num_nodes(self,node):
        return len(self.preorder_traverse(node))
    
tree = BinaryTree(level_order)
depth = tree.depth(tree.root)
num_nodes = tree.num_nodes(tree.root)

## 6. Types of Trees ##

class BinaryTree(BaseBinaryTree):
    def is_balanced(self,node):
        if not node: 
            return True
        
        sub_tree_left = node.left
        sub_tree_right = node.right
        
        if abs(self.depth(sub_tree_left) - self.depth(sub_tree_right)) <= 1:
            return True and (self.is_balanced(sub_tree_left) and                         self.is_balanced(sub_tree_right))
        else: 
            return False      

tree = BinaryTree(level_order)
balanced = tree.is_balanced(tree.root)

tree2 = BinaryTree([1,2,3])
      
tree2.root.left.left = Node(4)
tree2.root.left.left.left = Node(5)
tree2.root.right.right = Node(6)
tree2.root.right.left = Node(7)
tree2.root.left.right = Node(8)


print(tree2.is_balanced(tree2.root))