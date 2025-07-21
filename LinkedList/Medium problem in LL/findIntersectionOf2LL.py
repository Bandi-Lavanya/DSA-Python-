'''List1: 1->3->1->2->4
List2: 3->2->4
The intersection point is 2
The intersection point is 2
The intersection point is 2
The intersection point is 2'''
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# utility function to insert node at the end of the linked list
def insertNode(head, val):
    newNode = Node(val)
    if head == None:
        head = newNode
        return head
    temp = head
    while temp.next != None:
        temp = temp.next
    temp.next = newNode
    return head




# utility function to check presence of intersection
def intersectionPresent1(head1, head2):
    while head2 != None:
        temp = head1
        while temp != None:
            # if both nodes are same
            if temp == head2:
                return head2
            temp = temp.next
        head2 = head2.next
    # intersection is not present between the lists
    return None


def intersectionPresent2(head1, head2):
    st = set()
    while head1 != None:
        st.add(head1)
        head1 = head1.next
    while head2 != None:
        if head2 in st:
            return head2
        head2 = head2.next
    return None

def getDifference(head1, head2):
    len1 = 0
    len2 = 0
    while head1 != None or head2 != None:
        if head1 != None:
            len1 += 1
            head1 = head1.next
        if head2 != None:
            len2 += 1
            head2 = head2.next
    # if difference is neg-> length of list2 > length of list1 else vice-versa
    return len1 - len2




# utility function to check presence of intersection
def intersectionPresent_better(head1, head2):
    diff = getDifference(head1, head2)
    if diff < 0:
        while diff != 0:
            head2 = head2.next
            diff += 1
    else:
        while diff != 0:
            head1 = head1.next
            diff -= 1
    while head1 != None:
        if head1 == head2:
            return head1
        head2 = head2.next
        head1 = head1.next
    return head1

# utility function to check presence of intersection
def intersectionPresent_optimal(head1, head2):
    d1 = head1
    d2 = head2
    while d1 != d2:
        d1 = head2 if d1 == None else d1.next
        d2 = head1 if d2 == None else d2.next
    return d1

# utility function to print linked list created
def printList(head):
    while head.next != None:
        print(head.val, end='->')
        head = head.next
    print(head.val)




if __name__ == '__main__':
    head = None
    head = insertNode(head, 1)
    head = insertNode(head, 3)
    head = insertNode(head, 1)
    head = insertNode(head, 2)
    head = insertNode(head, 4)
    head1 = head
    head = head.next.next.next
    headSec = None
    headSec = insertNode(headSec, 3)
    head2 = headSec
    headSec.next = head
    print('List1: ', end='')
    printList(head1)
    print('List2: ', end='')
    printList(head2)
    answerNode = intersectionPresent1(head1, head2)
    if answerNode == None:
        print('No intersection')
    else:
        print('The intersection point is', answerNode.val)
    
    answerNode1 = intersectionPresent2(head1, head2)
    if answerNode1 == None:
        print('No intersection')
    else:
        print('The intersection point is', answerNode1.val)

    answerNode2 = intersectionPresent_better(head1, head2)
    if answerNode2 == None:
        print('No intersection')
    else:
        print('The intersection point is', answerNode2.val)

    answerNode3 = intersectionPresent_optimal(head1, head2)
    if answerNode3 == None:
        print('No intersection')
    else:
        print('The intersection point is', answerNode3.val)

