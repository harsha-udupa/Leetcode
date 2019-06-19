import random

class Tree(object):

    def __init__(self,val):

        self.left=None
        self.val=val
        self.right=None

def print_tree(root):

    if not root:
        return

    print_tree(root.left)
    print root.val
    print_tree(root.right)

def make_tree(arr,start,end):
    if end<start:
        return
    mid=(start+end)/2
    node=Tree(arr[mid])
    node.left=make_tree(arr,start,mid-1)
    node.right=make_tree(arr,mid+1,end)
    return node

bst=[]
for i in range(1,51):
    bst.append(i)

node=make_tree(bst,0,len(bst)-1)

print_tree(node)
