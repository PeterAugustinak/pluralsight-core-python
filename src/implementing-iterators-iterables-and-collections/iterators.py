def _is_perfect_length(sequence):
    """
    True if sequence has length 2**n - 1, otherwise False
    """
    n = len(sequence)
    return ((n + 1) & n == 0) and (n != 0)


class LevelOrderIterator:


    def __init__(self, sequence):
        if not _is_perfect_length(sequence):
            raise ValueError(
                f"Sequence of length {len(sequence)} does not represent a "
                f"perfect binary tree with length 2**n -1")
        self._sequence = sequence
        self._index = 0

    def __next__(self):
        if self._index >= len(self._sequence):
            raise StopIteration
        result = self._sequence[self._index]
        self._index += 1
        return result

    def __iter__(self):
        return self


def _left_child(index):
    return 2 * index + 1

def _right_child(index):
    return 2 * index + 2


class PreOrderIterator:

    def __init__(self, sequence):
        if not _is_perfect_length(sequence):
            raise ValueError(
                f"Sequence of length {len(sequence)} does not represent a "
                f"perfect binary tree with length 2**n -1")
        self._sequence = sequence
        self._stack = [0]


    def __next__(self):
        if len(self._stack) == 0:
            raise StopIteration
        index = self._stack.pop()
        result = self._sequence[index]

        # pre-order: push right child first so left child is popped and
        # processed first. Last-in, first-out
        right_child_index = _right_child(index)
        if right_child_index < len(self._sequence):
            self._stack.append(right_child_index)

        left_child_index = _left_child(index)
        if left_child_index < len(self._sequence):
            self._stack.append(left_child_index)

        return result

    def __iter__(self):
        return self


class InOrderIterator:

    def __init__(self, sequence):
        if not _is_perfect_length(sequence):
            raise ValueError(
                f"Sequence of length {len(sequence)} does not represent a "
                f"perfect binary tree with length 2**n -1")
        self._sequence = sequence
        self._stack = []
        self._index = 0

    def __next__(self):
        if (len(self._stack) == 0) and (self._index >= len(self._sequence)):
            raise StopIteration

        # push left children onto the stack while possible
        while self._index < len(self._sequence):
            self._stack.append(self._index)
            self._index = _left_child(self._index)

        # pop from stack and process, before moving to the right child
        index = self._stack.pop()
        result = self._sequence[index]
        self._index = _right_child(index)
        return result

    def __iter__(self):
        return self

missing = object()


class SkipMissingIterator:

    def __init__(self, iterable):
        self._iterator = iter(iterable)

    def __next__(self):
        while True:
            item = next(self._iterator)
            if item is not missing:
                return item

    def __iter__(self):
        return self


class TranslationIterator:

    def __init__(self, table, iterable):
        self._table = table
        self._iterator = iter(iterable)

    def __next__(self):
        item = next(self._iterator)
        return self._table.get(item, item)

    def __iter__(self):
        return self


class PerfectBinaryTree:

    def __init__(self, breadth_first_items):
        self._sequence = tuple(breadth_first_items)
        if not _is_perfect_length(self._sequence):
            raise ValueError(
                f"Sequence of length {len(self._sequence)} does not represent a "
                f"perfect binary tree with length 2**n -1")

    def __iter__(self):
        return SkipMissingIterator(PreOrderIterator(self._sequence))


# check perfect tree
perfect_tree = {i: _is_perfect_length(['x']* i) for i in range(0, 32)}
print(perfect_tree)

# (a + b) * (c + d)
# binary tree:
expression_tree = '* + - a b c d'.split()

# level order iterator -> * + - a b c d
iterator_level_order = LevelOrderIterator(expression_tree)
string_level_order = " ".join(iterator_level_order)
print(string_level_order)

# pre-order iterator -> * + a b - c d
iterator_pre_order = PreOrderIterator(expression_tree)
string_pre_order = " ".join(iterator_pre_order)
print(string_pre_order)

# in-order iterator -> a + b * c - d
iterator_in_order = InOrderIterator(expression_tree)
string_in_order = " ".join(iterator_in_order)
print(string_in_order)

# check handling missing iterators in imperfect binary tree -> r + p * q
expr_tree = ["+", "r", "*", missing, missing, "p", "q"]
iterator_skipping = SkipMissingIterator(expr_tree)

print(list(iterator_skipping))

iterator_skipping = SkipMissingIterator(InOrderIterator(expr_tree))
string_skipping = " ".join(iterator_skipping)
print(string_skipping)

# iterable changing iterator to symbols from table -> p * q - r / s + t
typesetting_table = {
    "-": "\u2212", # minus sign
    "*": "\u00D7", # multiplication sign
    "/": "\u00F7", # division sign
}

m = missing
expr_tree = [
                "-",
            "*",         "/",
        "p",    "q",    "r",    "+",
    m, m,       m, m,    m, m,    "s", "t"
]

iterator_translation = TranslationIterator(
    typesetting_table,
    SkipMissingIterator(InOrderIterator(expr_tree))
)
string_translation = " ".join(iterator_translation)
print(string_translation)


# PerfectBinaryTree test
tree = PerfectBinaryTree("+ * / u v w x".split())
iterator = iter(tree)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
for item in tree:
    print(item, end=" ") # same as ' '.join(tree)