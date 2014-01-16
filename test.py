from evaluation_funtion import *
from chess_obj import *

def print_board(board):
    """print the board"""
    print "X\Y 1  2  3  4  5  6  7  8"
    crd = 1
    sentence = ' 1 '
    for line in board:
        for piece in line:
            if piece > 0:
                sentence += (' O ')
            elif piece < 0:
                sentence += (' X ')
            else:
                sentence += (' . ')
        
        print sentence
        
        crd += 1
        sentence = ' ' + str(crd) + ' '
        
    return 0

game = CurrentSituation()
legal_points = game.legal_points
while legal_points:
    
    if game.current_player == game.black_sign:
        print "player: X\n"
    else:
        print "player: O\n"
        
    print_board(game.chess_board.board)
    greenHandStragity(game)
    legal_points = game.legal_points
    print
    print_board(game.chess_board.board)
    
    if game.current_player == game.black_sign:
        print "player: X\n"
    else:
        print "player: O\n"
    decision = raw_input()
    decision = (int(decision[0])-1, int(decision[2])-1)
    game.determine(decision)
    legal_points = game.legal_points
    print

count = game.update_chess_piece_sequence()
print count
    