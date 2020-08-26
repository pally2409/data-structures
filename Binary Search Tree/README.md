# Binary Search Tree

Binary Search Trees (BST) are also referred to as ordered binary tree. They are ordered in a manner that allows for faster addition, removal and lookup of nodes. The basic properties of a BST are:

* Left subtree of a node contains node that contains keys lesser than the current node's key
* Right subtree of a node contains node that contains keys greater than the current node's key

![Binary Search Tree](https://upload.wikimedia.org/wikipedia/commons/d/da/Binary_search_tree.svg)

## List of Problems

| Problem                                        | Link |
|------------------------------------------------|------|
| [Insert into a Binary Search Tree](#inserting-a-node-into-bst)               | [LeetCode](https://leetcode.com/problems/insert-into-a-binary-search-tree/)|
| [Delete Node in a BST](#deleting-a-particular-node-in-bst)                           | [LeetCode](https://leetcode.com/problems/delete-node-in-a-bst/)|
| Lowest Common Ancestor of a Binary Search Tree | [LeetCode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)     |
| Inorder Successor in BST                       | [GeeksForGeeks](https://practice.geeksforgeeks.org/problems/inorder-successor-in-bst/1)|
| Kth Smallest Element in BST                    | [LeetCode](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)    |

## Walkthrough

### Inserting a node into BST

[LeetCode](https://leetcode.com/problems/insert-into-a-binary-search-tree/)

The first thing one must do while tackling a BST problem is simply check whether a tree exists. We can do so by checking whether the root is null or not. If a tree doesn't already exist, then we know that the inserted value is the root of the tree and the only element of the tree.

```python
if root == None:
  return TreeNode(val)
```
Now, as mentioned earlier, we know that the left subtree of a node contains all elements whose values are lesser than the current node and the right subtree contains elements whose values are greater than the current node. This gives us an intuition as to how to approach the problem. All we have to do is traverse our tree by checking whether the current node is lesser than or greater than the element we would like to insert. 

In our while loop, we set the condition that the loop will run till the loop is not equals to none meaning that we cannot go further in our tree. Inside, we simply check whether the current node is lesser than the value we have to insert, if so, we move towards our right subtree. If the right subtree does not exist, we insert our value here and return our root with the inserted node. Similarly, if the current node value is greater than the value we have to insert, we move towards the left subtree and insert accordingly. 

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            return TreeNode(val)
        else:
            og = root
            while(root!=None):
                if root.val < val:
                    if root.right:
                        root = root.right
                    else:
                        root.right = TreeNode(val)
                        break
                else:
                    if root.left:
                        root = root.left
                    else:
                        root.left = TreeNode(val)
                        break
            return og
```

### Deleting a particular node in BST

Deleting a node, given a key, may not be as straightforward as insertion, however, the intuition is the same. You recursively traverse the tree till you come across the node that you have to delete and then tackle the following cases:
* Node does not have left or right subtree, you can simply return null
* Node only has right subtree, then you return the right subtree
* Node only has left subtree, then you return the left subtree
* Node has both left and right subtree, then you return the next inorder successor of the right subtree (i.e the minimum element on the right subtree)

Given the following tree, lets look at how to tackle each of the scenarios described above using the following code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root == None:
            return None
        else:
            if root.val > key:
                root.left = self.deleteNode(root.left, key)
            elif root.val < key:
                root.right = self.deleteNode(root.right, key)
            else:
                if root.left == None:
                    temp = root.right
                    root = None
                    return temp
                elif root.right == None:
                    temp = root.left
                    root = None
                    return temp
                temp = self.inOrderSuccessor(root.right)
                root.val = temp.val
                root.right = self.deleteNode(root.right, temp.val)
            return root
    
    def inOrderSuccessor(self, root):
        if root == None:
            return None
        while(root.left):
            root = root.left
        return root                   
```

![Binary Search Tree](https://upload.wikimedia.org/wikipedia/commons/d/da/Binary_search_tree.svg)

1. Node to be deleted is a leaf node

  Suppose you have to delete 1. We call our function deleteNode(root, 1), 
  
  1. In our first recursive call, the function sees that the root value (8) is greater than our key, then we know that we have to traverse the left subtree
  2. In our next recursive call, the function sees that the root value (3) is also greater than our key, we know that we have to again traverse the left subtree
  3. In the next recursive call, since we have reached the node to be deleted, our node doesn't meet any of the if conditions, so, in the else statement, we check whether the root.left is null, which indeed it is, so we return the right subtree which is also null in this case.
  
  Our final recursive statement returns a null, which meets the first condition, that is root == null, and hence, the left subtree of the node value 3 is set to null. Once, this happens, the function moves towards the next statement which is simply to return the root and so on.
 
2. Node to be deleted has a single child

  Suppose you have to delete 3. We call our function deleteNode(root, 3), 
  
  1. In our first recursive call, the function sees that the root value (8) is greater than our key, then we know that we have to traverse the left subtree
  2. In the next recursive call, since we have reached the node to be deleted, our node doesn't meet any of the if conditions, so, in the else statement, we check whether the root.left is null, which is not, so we move on to check whether root.right is null, which it is, so we move on to return the left subtree. 
  
  Our final recursive statement returns the node with the value 1 and hence, the left subtree of the node with value 8 is updated to have a 1. 
  
2. Node to be deleted has both left and right children

  Suppose you have to the root node 8, 
  
  1. In our first recursive call, since we have reached the node to be deleted, our node doesn't meet any of the if conditions, so, in the else statement, we check whether the root.left is null and whether the root.right is null, since the tree has both left and right children we don't meet any of these conditions. We move on to the next line of the function which finds a suitable replacement for the current node. The most suitable replacement for the current node has to be a node for which the left subtree values will be lesser than the node and the right subtree values will all be greater than the node. This value is the minimum element of the right subtree of the node to be deleted. 
  
  We find the minimum value of the right subtree, which is the in order successor of the right subtree, and replace the current value with this value and recursively delete that value from the right subtree.
 

 
 



