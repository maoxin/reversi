import copy
import random

class ChessBoard(object):
    """the chessboard and chess piece on it"""
    def __init__(self, old_board=None):
        super(ChessBoard, self).__init__()
        if old_board:
            self.board = copy.deepcopy(old_board)
        else:
            self.board = map(lambda x: list(x), [(0, ) * 8] * 8)
                    
            self.board[3][3] = self.board[4][4] =  1
            self.board[3][4] = self.board[4][3] = -1
            
            
class CurrentSituation(object):
    """
    The current chessboard, current player, legal positions of current player.
    And the interface open to player to operate the chessboard.
    """
    def __init__(self, old_board=None, no_way=None, current_player=None):
        super(CurrentSituation, self).__init__()
        self.black_sign = -1
        self.white_sign = +1
        self.no_way = 0
        self.current_player = self.black_sign
        self.direction = {
            'left' : (-1,  0),
            'right': ( 1,  0),
            'up'   : ( 0,  1),
            'down' : ( 0, -1),
            'l_u'  : (-1,  1),
            'r_u'  : ( 1,  1),
            'l_d'  : (-1, -1),
            'r_d'  : ( 1, -1)  
        }
        
        if old_board:
            self.no_way = no_way
            self.current_player = current_player
            self.chess_board = ChessBoard(old_board)
        else:
            self.chess_board = ChessBoard()
        
        self.black_sequence = [] 
        self.white_sequence = []
        self.piece_sequence = [self.black_sequence, self.white_sequence]
        self.update_chess_piece_sequence()
        self.new_pieces = []
        
        self.legal_points = []
        self.get_legal_points()
    
    def update_chess_piece_sequence(self):
        """update where the black/white chess pieces in"""
        self.black_sequence = []
        self.white_sequence = []
        self.piece_sequence = [self.black_sequence, self.white_sequence]
        
        for x in range(8):
            for y in range(8):
                if self.chess_board.board[x][y] == self.black_sign:
                    self.black_sequence.append( (x, y) )
                elif self.chess_board.board[x][y] == self.white_sign:
                    self.white_sequence.append( (x, y) )
                else: pass
                     
        return (len(self.black_sequence), len(self.white_sequence))
    
    def get_chance(self, pos, player, anti, direction):
        new_pos = (pos[0] + direction[0], pos[1] + direction[1])
        
        if new_pos[0] < 0 or new_pos[0] >= 8 or \
           new_pos[1] < 0 or new_pos[1] >= 8:
            return False
        
        elif new_pos in self.piece_sequence[anti]:
            return self.get_chance(new_pos, player, anti, direction)
        
        elif new_pos not in self.piece_sequence[player]:
            return new_pos
                        
        else:
            return False
                    
        
    def get_legal_points(self):
        """return the legal points of current player"""
        self.legal_points = []
        
        if self.current_player == self.black_sign:
            player = 0
        else:
            player = 1
            
        for pos in self.piece_sequence[player]:
            for key in self.direction.keys():
                direction = self.direction[key]
                candidate = self.get_chance(pos, player, (player+1) % 2, direction)
                if candidate and candidate != (pos[0] + direction[0], pos[1] + direction[1]):
                    if candidate not in self.piece_sequence[player]:
                        self.legal_points.append((candidate, direction))
                        # the [0] is the legal pos and the [1] is the direction to it 
                    
        return copy.deepcopy(self.legal_points)
    
    def get_legal_points_without_direction(self):
        return [x[0] for x in self.legal_points]
    
    def next_player(self):
        if self.current_player == self.black_sign:
            self.current_player = self.white_sign
        else:
            self.current_player = self.black_sign
        
        legal_points = self.get_legal_points()
        if legal_points:
            self.no_way = 0
            return legal_points
        else:
            self.no_way += 1
            
            if self.no_way == 2:
                return False
            else:
                return self.next_player()
        
    def determine(self, pos):
        """place the piece and push the situation forward"""    
        self.new_pieces = []
        
        if pos not in self.get_legal_points_without_direction():
            return "Illegal Point!"
        
        if self.current_player == self.black_sign:
            player = 0
        else:
            player = 1
        
        count = 0
        
        actions = filter(lambda x: x[0] == pos, self.legal_points)
        self.chess_board.board[pos[0]][pos[1]] = self.current_player
        
        for act in actions:
            direction = (-act[1][0], -act[1][1])
            conquer_pos = (pos[0] + direction[0], pos[1] + direction[1])
            
            while conquer_pos not in self.piece_sequence[player]:
                self.new_pieces.append(conquer_pos)
                self.chess_board.board[conquer_pos[0]][conquer_pos[1]] = self.current_player
                conquer_pos = (conquer_pos[0] + direction[0], conquer_pos[1] + direction[1])
                count += 1
        
        self.update_chess_piece_sequence()
        return self.next_player()
        
    def try_it(self, pos):
        """create a dummy of current situation for agent to judge in"""
        dummy = CurrentSituation(self.chess_board.board, self.no_way, self.current_player)
        dummy.determine(pos)
        
        return dummy

