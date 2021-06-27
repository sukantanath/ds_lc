# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        listofNodes = []
        #recursive approach
        if root is None:
            print("reached leaf node")
        else:
            print("currently at: ",root.val)
            listofNodes.append(root.val)
            listofNodes += self.preorderTraversal(root.left)
            listofNodes += self.preorderTraversal(root.right)
        
        return(listofNodes)
      
      
      
  def preorderTraversalIterative(self, root: TreeNode) -> List[int]:
        listofNodes = []
        #iterative approach
        if root is None:
            print("Do nothing")
        else:
            visitedNodeStack = []
            visitedNodeStack.append(root)
            while (len(visitedNodeStack) > 0):
                curr_node = visitedNodeStack.pop()
                listofNodes += [curr_node.val]
                if curr_node.right is not None:
                    visitedNodeStack.append(curr_node.right)
                if curr_node.left is not None:
                    visitedNodeStack.append(curr_node.left)
        return(listofNodes)
