class DynamicArray:
    def __init__(self, capacity: int = 1):
        # Start with at least 1 capacity
        self._capacity = max(1, capacity)
        self._elements = [None] * self._capacity
        # Track the actual number of elements
        self._size = 0

    def get(self, i: int) -> int:
        # Check if index is valid
        if 0 <= i < self._size:
            return self._elements[i]
        raise IndexError("Index out of bounds")

    def set(self, i: int, n: int) -> None:
        # Check if index is valid
        if 0 <= i < self._size:
            self._elements[i] = n
        else:
            raise IndexError("Index out of bounds")

    def pushback(self, n: int) -> None:
        # Resize if we've reached capacity
        if self._size == self._capacity:
            self.resize()

        # Add element and increment size
        self._elements[self._size] = n
        self._size += 1

    def popback(self) -> int:
        # Check if array is empty
        if self._size == 0:
            raise IndexError("Cannot pop from empty array")

        # Decrease size and return last element
        self._size -= 1
        return self._elements[self._size]

    def resize(self) -> None:
        # Double the capacity
        new_capacity = self._capacity * 2
        # Create a new array with doubled capacity
        new_elements = [None] * new_capacity

        # Copy existing elements
        for i in range(self._size):
            new_elements[i] = self._elements[i]

        # Update internal state
        self._elements = new_elements
        self._capacity = new_capacity

    def getSize(self) -> int:
        # Simply return the tracked size
        return self._size

    def getCapacity(self) -> int:
        return self._capacity
