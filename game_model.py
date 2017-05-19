def get_letter_value(letter):
    return {
        'l': 1,
        'n': 1,
        'o': 1,
        'a': 1,
        'e': 1,
        's': 1,
        'r': 1,
        'i': 1,
        'u': 1,
        't': 1,
        'g': 2,
        'd': 2,
        'b': 3,
        'c': 3,
        'm': 3,
        'p': 3,
        'f': 4,
        'h': 4,
        'v': 4,
        'w': 4,
        'y': 4,
        'k': 5,
        'j': 8,
        'x': 8,
        'q': 10,
        'z': 10
    }.get(letter, 0)


def get_index_mapping(letter):
    return {
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
        'e': 4,
        'f': 5,
        'g': 6,
        'h': 7,
        'i': 8,
        'j': 9,
        'k': 10,
        'l': 11,
        'm': 12,
        'n': 13,
        'o': 14,
        'p': 15,
        'q': 16,
        'r': 17,
        's': 18,
        't': 19,
        'u': 20,
        'v': 21,
        'w': 22,
        'x': 23,
        'y': 24,
        'z': 25
    }.get(letter, -1)


class Game(object):
    def __init__(self):
        self.board = ([None] * 15) * 15
        self.player_hand = [None] * 7
        self.computer_hand = [None] * 7
        self.player_score = 0
        self.computer_score = 0
        self.bag = [None] * 100

    def create_board(self):
        pass

    def create_bag(self):
        pass

    def add_word(self, word, start, direction):
        pass

    def get_tiles(self, opponent):
        pass

    def remove_tiles(self, opponent):
        pass

    def update_score(self, opponent):
        pass


class Lexicon(object):
    def __init__(self, dictionary):
        self.head = Node()
        for word in dictionary:
            self.add(word)

    def add(self, word):
        curr = self.head
        for letter in word:
            curr = curr.add_child(letter, curr.value[1] + get_letter_value(letter))

    def contains_word(self, word):
        curr = self.head
        for letter in word:
            next_node = curr.get_child(letter)
            if next_node is None:
                return False
            curr = next_node
        return True


class Node(object):
    def __init__(self, value=(None, 0)):
        self.value = value
        self.children = [None] * 26

    def get_child(self, letter):
        return self.children[get_index_mapping(letter)]

    def add_child(self, letter, score):
        if self.children[get_index_mapping(letter)] is not None:
            return self.children[get_index_mapping(letter)]
        new_node = Node((letter, score))
        self.children[get_index_mapping(letter)] = new_node
        return new_node
