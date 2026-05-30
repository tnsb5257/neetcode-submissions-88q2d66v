/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* a = head;
        int l=0;
        while(a){
            a=a->next;
            l++;
        }
        ListNode dummy(0);
        ListNode* temp = &dummy;
        temp->next=head;
        for(int i=0;i<(l-n);i++){
            temp=temp->next;
        }
        if(temp->next != nullptr){
            temp->next = temp->next->next;
        }
        return dummy.next;
    }
};
