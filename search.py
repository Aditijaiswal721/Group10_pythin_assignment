import time as t
from abc import ABC, abstractmethod

# Abstract base class for search algorithms
class Search(ABC):

    def __init__(self, items):
        self._items = items

    @abstractmethod
    def _search(self, b):
        pass

    def get_items(self):
        return self._items

    # Measure the time it takes to perform a search
    def _time(self, m):
        start_time = t.time()
        self._search(m)
        end_time = t.time()
        return end_time - start_time

# class implementing linear search inheriting Search Class
class Linear_Search(Search):
    def _search(self, b):
        d = False
        for i in range(len(self._items)):
            if b == self._items[i]:
                print("FOUND!!!!!! index =", i)
                d = True
        if not d:
            print("We are sorry to inform you that the search resulted in NOTHING!")
# Class implementing binary search inheriting Search Class
class Binary_Search(Search):
    def _search(self, b):
        left, right = 0, len(self._items) - 1
        found = False

        while left <= right:
            mid = (left + right) // 2
            if self._items[mid] == b:
                print("FOUND!!!!!! using Binary Search index =", mid)
                found = True
                break
            elif self._items[mid] < b:
                left = mid + 1
            else:
                right = mid - 1

        if not found:
            print("We are sorry to inform you that the Binary Search resulted in NOTHING!")
if __name__ == '__main__':
    try:
        # Input the size of the list
        n = int(input("Enter the size of the list: "))
        g = []
        
        # Input the elements of the list
        for i in range(n):
            g.append(int(input("Enter the content for the list: ")))
        
        # Input the value to be searched
        m = int(input("Enter the value to be searched: "))
        
        # Create an instance of Linear_Search and perform the search
        s1 = Linear_Search(g)
        print("The time taken for the interations in Linear Search",s1._time(m)," sec")
        s2 = Binary_Search(g)
        print("The time taken for the iterations in Binary Search:", s2._time(m), "sec")
    except ValueError:
        print("Please enter valid integers for the list size and search value.")
