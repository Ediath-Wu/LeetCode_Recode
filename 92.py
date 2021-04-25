# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution():
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        c=right-left
        if divmod(c,2)[1] == 0:
            for i in range((c+1)/2):
                a=head[right-i-1]
                b=head[left+i-1]
                head[left+i-1],head[right-i-1]=a,b
        else:
            for i in range(c/2):
                a=head[right-i-1]
                b=head[left+i-1]
                head[left+i-1],head[right-i-1]=a,b
        return head
    
    soaaa=Solution()
    print(soaaa.)