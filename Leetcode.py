# 53 optumized one 

def max(num):
        nums=[]
        max_sum=nums[0]
        current_sum=nums[0]

        for i in range(1,len(nums)):

            num  =nums[i]
            if current_sum<0:

                current_sum=num
            else:

                current_sum+=num

        if current_sum>max_sum:
            max_sum=current_sum

            return max_sum
            

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(max(nums))


#hackerrank
#insert into tail of node


class Node:
    def __init__(self, data):
            self.data=data 
            self.next=next

def insertattail(head, data):
     new_node=Node(data)
     if head is None:
          return new_node
     current=head

     while current.next is not None:
          current=current.next
     current.next=new_node

     return head

def insertathead(head, data):
     new_node=Node(data)
     new_node.next=head
     return new_node

def printdata(head):
     current=head
     while current is not None:
            print(current.data)
            current=current.next



def deletenode(head, data):
        if head is None:
            return None
        if head.data==data:
            return head.next
        current=head
        while current.next is not None:
            if current.next.data==data:
                current.next=current.next.next
                return head
            current=current.next
        return head


# merge two sorted linked listk
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next

            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 if list1 else list2

        return dummy.next
        
#  110. Balanced Binary Tree
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(node):
            if not node:
                return 0
            
            # 1. Check left subtree balance and height
            left_height = dfs(node.left)
            if left_height == -1:
                return -1
                
            
            right_height = dfs(node.right)
            if right_height == -1:
                return -1
            
            # 3. Check current node balance
            if abs(left_height - right_height) > 1:
                return -1
                
            # 4. Return actual height to parent node
            return 1 + max(left_height, right_height)
            
        return dfs(root) != -1
        