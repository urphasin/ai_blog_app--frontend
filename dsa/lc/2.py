class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def addTwoNumbers(l1: ListNode, l2: ListNode):
    pass


M_0 = ListNode(2)
M_1 = ListNode(4)
M_2 = ListNode(3)

N_0 = ListNode(5)
N_1 = ListNode(6)
N_2 = ListNode(4)


M_0.next = M_1
M_1.next = M_2

N_0.next = N_1
N_1.next = N_2


if __name__ == "__main__":
    addTwoNumbers(M_0, N_0)