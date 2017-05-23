from game_model import *


def valid_placement(board, word, position, direction):
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
            elif letter not in board[x + 1][y].cross_checks['North'] or letter not in board[x - 1][y].cross_checks[
                'South']:
                return False
        else:
            if y == 0 and letter not in board[x][y + 1].cross_checks['West']:
                return False
            elif y == len(board[x]) - 1 and letter not in board[x][y - 1].cross_checks['East']:
                return False
            elif letter not in board[x][y + 1].cross_checks['West'] and letter not in board[x][y - 1].cross_checks[
                'East']:
                return False
        if direction == "across":
            y += 1
        else:
            x += 1
    return True


def is_anchor(board, position):
    x = position[0]
    y = position[1]
    if x == 0 and y == 0:
        return board[x + 1][y].letter is not None or board[x][y + 1].letter is not None
    elif x == len(board) - 1 and y == 0:
        return board[x - 1][y].letter is not None or board[x][y + 1].letter is not None
    elif x == 0 and y == len(board) - 1:
        return board[x + 1][y].letter is not None or board[x][y - 1].letter is not None
    elif x == len(board) - 1 and y == len(board) - 1:
        return board[x - 1][y].letter is not None or board[x][y - 1].letter is not None
    elif x == 0:
        return board[x + 1][y].letter is not None or board[x][y - 1].letter is not None or \
               board[x][y + 1].letter is not None
    elif y == 0:
        return board[x + 1][y].letter is not None or board[x - 1][y].letter is not None or \
               board[x][y + 1].letter is not None
    else:
        return board[x + 1][y].letter is not None or board[x - 1][y].letter is not None or \
               board[x][y + 1].letter is not None or board[x][y - 1].letter is not None


def calculate_score():
    pass


def computer_turn():
    pass


def player_turn(game, word, position, direction):
    if not game.dictionary.contains(game.board, word):
        return "invalid word"
    if not valid_placement(word, position, direction):
        return "invalid placement"
    else:
        return "approved"


def get_best_words():
    pass


def find_anchors():
    pass


def find_cross_checks():
    pass
