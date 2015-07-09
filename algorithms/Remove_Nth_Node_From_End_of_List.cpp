/*
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
*/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if (head==NULL){
            return NULL;
        }
        ListNode *cur=head;
        int len=1;
        while(cur->next!=NULL){
            len+=1;
            cur=cur->next;
        }
        
        int pos=len-n;
        if(pos<0){
            return head;
        }
        if(pos==0){
            return head->next;
        }
        
        cur=head;
        while(pos>1 && cur!=NULL){
            cur=cur->next;
            pos--;
        }
        
        ListNode* p=cur->next;
        cur->next=cur->next->next;
        delete p;
        return head;
    }
};
