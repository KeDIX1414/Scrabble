from game_model import *


def check_placement(board, word, position, direction):
    x = position[0]
    y = position[1]
    # check if first square is an anchor
    if not board[position[0]][position[1]].is_anchor:
        return False
    for letter in word:
        # make sure that the letter is a valid crosscheck
        if direction == "across":
            if x == 0 and letter not in board[x + 1][y].cross_checks['North']:
                return False
            elif x == len(board) - 1 and letter not in board[x - 1][y].cross_checks['South']:
                return False
            elif letter not in board[x + 1][y].cross_checks['North'] or letter not in board[x - 1][y].cross_checks['South']:
                return False
        else:
            if y == 0 and letter not in board[x][y + 1].cross_checks['West']:
                return False
            elif y == len(board[x]) - 1 and letter not in board[x][y - 1].cross_checks['East']:
                return False
            elif letter not in board[x][y + 1].cross_checks['West'] and letter not in board[x][y - 1].cross_checks['East']:
                return False
        if direction == "across":
            y += 1
        else:
            x += 1
    return True


def computer_turn(board):
    pass


def get_best_words(board, dictionary):
    pass


def find_anchors(board):
    pass


def find_cross_checks(board):
    pass

