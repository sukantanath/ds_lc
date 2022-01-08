# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#preorder is root -> left -> right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        listofNodes = []
        #recursive approach
        if root is None:
            print("reached leaf node")
        else:
            print("currently at: ",root.val)
            listofNodes.append(root.val) #root node processed
            listofNodes += self.preorderTraversal(root.left) #recursion with left node to process all left sub trees
            listofNodes += self.preorderTraversal(root.right) #recorsion with right node to process all right sub trees
        
        return(listofNodes)
      
      
      
  def preorderTraversalIterative(self, root: TreeNode) -> List[int]:
        listofNodes = []
        #iterative approach
        if root is None:
            print("Do nothing")
        else:
            visitedNodeStack = []
            visitedNodeStack.append(root) #root node processed 
            while (len(visitedNodeStack) > 0):
                curr_node = visitedNodeStack.pop()
                listofNodes += [curr_node.val]
                if curr_node.right is not None:
                    visitedNodeStack.append(curr_node.right)
                if curr_node.left is not None:
                    visitedNodeStack.append(curr_node.left) #left node is insrted in stack at the end as stack is LIFO
        return(listofNodes)
