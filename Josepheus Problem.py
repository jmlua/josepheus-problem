'''Solve the Josepheus problem using a circular linked list'''

class SinglyNode:
    def __init__(self, item, link = None):
        self.item = item
        self.next = link
    
    def toString(self):
        """Print the Node's item and a "->" if the next reference is valid."""
        return "[{}]".format(self.item) + ("->" if self.next != None else "")

class Josephine:
    def __init__(self, N):

        """ Initialize the circle of [N] princes. N > 0.
        """
        self._tail = None
        self._size = 0
        self._initialize(N)

    def _insert(self, item):
        newPtr = SinglyNode(item)

        if self._size == 0: #only tail in the list
            self._tail = newPtr
            self._tail.next = newPtr

        else:
            newPtr.next = self._tail.next
            self._tail.next = newPtr
            self._tail = newPtr

        self._size += 1
        return True

    def _initialize(self, n):
        for i in range(n):
            self._insert(i+1)
        return ''

    def toString(self):
        curr = self._tail.next
        if curr is None:
            print('List is empty')
        print('Nodes of the linked list are:')
        for i in range(self._size):
            print(curr.item)
            curr = curr.next
        return ''
    
    def chosenOne(self, K):
        """ Return a list of princes in the order they are removed.

            e.g. [2, 4, 3, 1] with N = 4, K = 2, the last prince is the chosen one.
        """
        output = []
        prev = self._tail
        curr = prev.next
        while self._size > 0:
            for i in range(1, K):   #traverse to kth item
                prev = curr
                curr = curr.next
            output.append(curr.item)    #append to list
            if curr == self._tail:      #removal
                prev.next = curr.next
                curr = curr.next 
                self._tail = prev
            else:
                prev.next = curr.next
                curr = curr.next 
            self._size -=1
        return output


def main():    
    N = int(input("N = "))
    K = int(input("K = "))

    j = Josephine(N)
    print(j.toString())

    print(j.chosenOne(K))


if __name__ == "__main__":
    main()
