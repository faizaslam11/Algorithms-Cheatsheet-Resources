# Python3 program to implement Tree Sort 

class Node: 

def __init__(self,item = 0): 
	self.key = item 
	self.left,self.right = None,None


# Root of BST 
root = Node() 

root = None

def insert(key): 
global root 
root = insertRec(root, key) 


def insertRec(root, key): 


if (root == None): 
	root = Node(key) 
	return root 

if (key < root.key): 
	root.left = insertRec(root.left, key) 
elif (key > root.key): 
	root.right = insertRec(root.right, key) 

# return the root 
return root 

def inorderRec(root): 
if (root != None): 
	inorderRec(root.left) 
	print(root.key ,end = " ") 
	inorderRec(root.right) 
	
def treeins(arr): 
for i in range(len(arr)): 
	insert(arr[i]) 

# Driver Code 
arr = [5, 4, 7, 2, 11] 
treeins(arr) 
inorderRec(root) 

