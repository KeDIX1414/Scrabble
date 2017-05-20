import random


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
        self.board = ([BoardSquare()] * 15) * 15
        self.player_hand = [None] * 7
        self.computer_hand = [None] * 7
        self.player_score = 0
        self.computer_score = 0
        self.bag = ["e" * 12, "a" * 9, "i" * 9, "o" * 8, "n" * 6, "r" * 6, "t" * 6, "l" * 4,
                    "s" * 4, "u" * 4, "d" * 4, "g" * 3, "p" * 2, "m" * 2, "c" * 2, "b" * 2,
                    "y" * 2, "w" * 2, "v" * 2, "h" * 2, "f" * 2, "blank" * 2, "k", "x", "j", "q", "z"]

    def create_board(self):
        pass

    def add_word(self, word, square, direction):
        pass

    def get_tiles(self, opponent, number):
        new_tiles = []
        for x in range(number):
            new_tiles.append(self.bag.remove(random.randrange(0, len(self.bag))))
        if opponent == "player":
            self.player_hand.extend(new_tiles)
        else:
            self.computer_hand.extend(new_tiles)

    def put_tiles(self, tiles):
        self.bag.extend(tiles)

    def update_score(self, opponent, addition):
        if opponent == "player":
            self.player_score += addition
        else:
            self.computer_score += addition


class BoardSquare(object):
    def __init__(self, dictionary, square_type=None):
        self.letter = None
        self.square_type = square_type
        self.cross_checks = {'North': ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
                                       "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
                             'South': ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
                                       "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
                             'East': ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
                                      "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
                             'West': ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
                                      "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]}

        self.is_anchor = False


class Dictionary(object):
    def __init__(self, dictionary):
        self.head = Node()
        for word in dictionary:
            self.add(word)

    def add(self, word):
        curr = self.head
        for letter in word:
            if letter == word[-1]:
                curr = curr.add_child(letter, True)
            else:
                curr = curr.add_child(letter, False)

    def contains(self, word):
        curr = self.head
        for letter in word:
            next_node = curr.get_child(letter)
            if next_node is None:
                return False
            curr = next_node
        return curr.value[1]


class Node(object):
    def __init__(self, value=[None, False]):
        self.value = value
        self.children = [None] * 26

    def get_child(self, letter):
        return self.children[get_index_mapping(letter)]

    def add_child(self, letter, position):
        if self.children[get_index_mapping(letter)] is not None:
            if position:
                self.children[get_index_mapping(letter)].value[1] = True
            return self.children[get_index_mapping(letter)]
        new_node = Node([letter, position])
        self.children[get_index_mapping(letter)] = new_node
        return new_node

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return self.value[0]
