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
    ListNode* reverse(ListNode* head){
        ListNode* prev = nullptr;
        ListNode* curr = head;
        while(curr!=nullptr){
            ListNode* temp = curr->next;
            curr->next = prev;
            prev=curr;
            curr=temp;
        }
        return prev;
    }

    void reorderList(ListNode* head) {
        ListNode* ans = head;
        ListNode* slow = head;
        ListNode* fast = head;
        while(fast!=nullptr && fast->next!=nullptr){
            slow = slow->next;
            fast=fast->next->next;
        }
        ListNode* head2 = slow->next;
        slow->next = nullptr;
        ListNode* rh2 = reverse(head2);
        while(rh2 != nullptr){
            ListNode* temp = head->next;
            head->next = rh2;
            ListNode* temp2 = rh2->next;
            rh2->next = temp;
            rh2 = temp2;
            head = temp;
        }
    }
};
