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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if(list1==nullptr)return list2;
        if(list2==nullptr)return list1;
        ListNode* temp1=list1;
        ListNode* temp2=list2;
        ListNode* head = list1->val <= list2->val ? list1 : list2;
        if(head==list1)temp1=temp1->next;
        else temp2=temp2->next;
        ListNode* nest=head;
        while(temp1!=nullptr&&temp2!=nullptr){
            if(temp1->val<=temp2->val){
                nest->next=temp1;
                temp1=temp1->next;
            }else{
                nest->next=temp2;
                temp2=temp2->next;
            }
            nest=nest->next;
        }
        if(temp1==nullptr){
            nest->next=temp2;
        }else if(temp2==nullptr){
            nest->next=temp1;
        }
        return head;
    }
};
