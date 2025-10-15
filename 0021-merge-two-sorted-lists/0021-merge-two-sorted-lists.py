# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        #brute force
        if not list1 and not list2:
            return None 
        arr= []
        while list1:
            arr.append(list1.val)
            list1= list1.next 
        while list2:
            arr.append(list2.val)
            list2= list2.next 
        arr.sort()

        res = ListNode()
        dummy = res
        for i in range(len(arr)):
            res.next = ListNode(arr[i])
            res = res.next 
        return dummy.next 
        """

        dummy_node = ListNode()
        temp = dummy_node
        while( list1 and  list2):
            if list1.val < list2.val:
                temp.next = list1
                temp = list1
                list1 = list1.next 
            else:
                temp.next = list2
                temp = list2
                list2 = list2.next
        if list1:
            temp.next = list1
        else:
            temp.next = list2
        return dummy_node.next  

         
            


        
        
        