"""
You are given two linked lists representing two non-negative numbers. 
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        
        result=ListNode(0)
        p = result
        p1=l1
        p2=l2
        k=0
        while(p1!=None or p2!=None or k):
            p.next=ListNode(0)
            p=p.next
            
            if (p1!=None) :
                p.val += p1.val
                p1=p1.next
            if (p2!=None):
                 p.val+=p2.val
                 p2=p2.next
            
           
            p.val,k =(p.val+k)%10 , (p.val+k)/10
  
             
             
        return result.next
