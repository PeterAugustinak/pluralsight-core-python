from fractions import Fraction

class RationaRange:

    def __init__(self, start, stop, num_steps):
        if num_steps != int(num_steps):
            raise ValueError(f"num_steps {num_steps} does not have integral"
                             f"value.")
        if num_steps < 1:
            raise ValueError(f"num_steps {num_steps} is not positive.")
        self._start = start
        self._num_steps = num_steps
        self._step = Fraction(stop - start, num_steps)

    def __getitem__(self, index):
        if not (0 <= index < self._num_steps):
            raise IndexError
        return self._start + index * self._step


r = RationaRange(5, 13, 6)
# as __iter__ is not created, it checks __getitem__ and creates iterator
iterator = iter(r)
next(iterator)
next(iterator)
next(iterator)
next(iterator)
next(iterator)
next(iterator)

# it is iterable so we can use it in a for loop:
for i in r:
    print(i, end=" ")

# we can use (reconstructed) iterator instead of original object as well
print()
iterator = iter(r)
for i in iterator:
    print(i, end=" ")

# or list comprehension as a float
print()
x = [float(item) for item in r]
print(x)
print(sum(r))
