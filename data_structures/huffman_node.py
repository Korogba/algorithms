# implementation by @kaba_y, https://korogba.github.io


class HuffmanNode:
    """Representation of a huffman node with a 'key' property to be used in heaps included"""

    def __init__(self, value):
        self.value = value
        self.key = value
        self.code_length = 0
        self.left_node = None
        self.right_node = None

    def __eq__(self, other) -> bool:
        assert isinstance(other, HuffmanNode)
        return self.value == other.value and self.left_node == other.left_node and self.right_node == other.right_node

    def __lt__(self, other) -> bool:
        assert isinstance(other, HuffmanNode)
        return self.key < other.key
