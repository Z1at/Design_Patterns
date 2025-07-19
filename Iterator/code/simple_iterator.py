class NumberIterator:
    def __init__(self, numbers):
        self._numbers = numbers
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._numbers):
            result = self._numbers[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration


numbers = [1, 2, 3, 4, 5]
iterator = NumberIterator(numbers)

for number in iterator:
    print(number)
