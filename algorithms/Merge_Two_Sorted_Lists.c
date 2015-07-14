/*
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode* head , *h;
    
    if (l1==NULL){
        return l2;
    }
    if (l2==NULL){
        return l1;
    }
    
    if(l1->val <= l2->val ){
        head=l1;
        l1=l1->next;
    }else{
        head=l2;
        l2=l2->next;
    }
    
    h=head;
    while(l1 && l2){
        if(l1->val <= l2->val){
            h->next=l1;
            l1=l1->next;
        }else{
            h->next=l2;
            l2=l2->next;
        }
        h=h->next;
    }
    
    while(l1){
        h->next=l1;
        h=l1;
        l1=l1->next;
    }
    
    while(l2){
        h->next=l2;
        h=l2;
        l2=l2->next;
    }
    
    return head;
}
