from abc import ABC, abstractmethod
import time

class Sort(ABC):

    def __init__(self, items):
        self._items = items

    @abstractmethod
    def _sort(self):
        pass

    def get_items(self):
        return self._items

    def _time(self):
        start_time = time.time()
        self._sort()
        end_time = time.time()
        return end_time - start_time

class BubbleSort(Sort):

    def _sort(self):
        for j in range(len(self._items)):
            for i in range(len(self._items) - 1):
                if self._items[i] > self._items[i + 1]:
                    self._items[i], self._items[i + 1] = self._items[i + 1], self._items[i]

def main():
    a = int(input("Enter the size of the list:"))
    print("Enter the list:")
    b = []
    for i in range(a):
        b.append(int(input()))
    
    bubble_sorter = BubbleSort(b.copy())
    bubble_time = bubble_sorter._time()
    print(f"Bubble Sort took {bubble_time} seconds to sort the list.")
    print("Sorted List (Bubble Sort):", bubble_sorter.get_items())


if __name__ == "__main__":
    main()
