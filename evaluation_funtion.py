# -*- coding: cp936 -*-
import util
import random

def green_evaluation(current_situation):
    """the evaluation func for green hand strategy"""
    score = 0
    player = current_situation.current_player
    
    #for line in current_situation.chess_board.board:
    #    for point in line:
    #        if point == player:
    #            score += 1
    
    board = current_situation.chess_board.board

    for x in range(8):
        for y in range(8):
            if board[x][y] == player:
                if (x, y) == (0, 0) or (x, y) == (0, 7) or\
                   (x, y) == (7, 0) or (x, y) == (7, 7):
                    score += 10000
                elif x == 0 or x == 7 or y == 0 or y == 7:
                    score += 200
                else:
                    score += 50
            
            elif board[x][y] == -player:
                if (x, y) == (0, 0) or (x, y) == (0, 7) or\
                   (x, y) == (7, 0) or (x, y) == (7, 7):
                    score -= 10000
                elif x == 0 or x == 7 or y == 0 or y == 7:
                    score -= 200
                else:
                    score -= 50
            else:
                pass
                
    return score    

def greenHandStrategy(current_situation):
    legal_points = current_situation.get_legal_points_without_direction()
    score = util.Counter()
    player = current_situation.current_player
  
    for pos in legal_points:
        new_board = current_situation.try_it(pos)
        score[pos] += green_evaluation(new_board)

    return score.argMax(), score

def normalStrategy(current_situation):
  legal_points = current_situation.get_legal_points_without_direction()
  score = util.Counter()
  player = current_situation.current_player
  
  for pos in legal_points:
    new_board = current_situation.try_it(pos)
    for line in new_board.chess_board.board:
      for point in line:
          if point == player:
              score[pos] += 1
        
  for pos1 in legal_points:
    if pos1 == (0,0) or pos1 == (0,7) or pos1 == (7,0) or pos1 == (7,7):
      score[pos1] += 1000
    if pos1[0] == 0 or pos1[0] == 7 or pos1[1] == 0 or pos1[1] == 7:
      score[pos1] += 200
    if pos1 == (1,1) or pos1 == (1,6) or pos1 == (6,1) or pos1 == (6,6):
      score[pos1] -= 1000

    if pos1 == (1,0):
      if current_situation.chess_board.board[0][0] != -player:
          score[pos1] -= 1000
      else:
          i = 2
          flag = player
          while( i < 8 ):
            if current_situation.chess_board.board[i][0] != player:
              flag = current_situation.chess_board.board[i][0]
              break
            i = i + 1
          if flag == player or flag == 0:
            score[pos1] += 1000
          else:
            score[pos1] -= 1000

    if pos1 == (0,1):
      if current_situation.chess_board.board[0][0] != -player:
          score[pos1] -= 1000
      else:
          i = 2
          flag = player
          while( i < 8):
            if current_situation.chess_board.board[0][i] != player:
              flag = current_situation.chess_board.board[0][i]
              break
            i = i + 1
          if flag == player or flag == 0:
            score[pos1] += 1000
          else:
            score[pos1] -= 1000


    if pos1 == (6,0):
      if current_situation.chess_board.board[7][0] != -player:
          score[pos1] -= 1000
      else:
          i = 5
          flag = player
          while( i >= 0):
            if current_situation.chess_board.board[i][0] != player:
              flag = current_situation.chess_board.board[i][0]
              break
            i = i - 1
          if flag == player or flag == 0:
            score[pos1] += 1000
          else:
            score[pos1] -= 1000

    if pos1 == (0,6):
      if current_situation.chess_board.board[0][7] != -player:
          score[pos1] -= 1000
      else:
          i = 5
          flag = player
          while( i >= 0 ):
            if current_situation.chess_board.board[0][i] != player:
              flag = current_situation.chess_board.board[0][i]
              break
            i = i -1
          if flag == player or flag == 0:
            score[pos1] += 1000
          else:
            score[pos1] -= 1000

    if pos1 == (7,1):
      if current_situation.chess_board.board[7][0] != -player:
          score[pos1] -= 1000
      else:
          i = 2
          flag = player
          while( i < 8):
            if current_situation.chess_board.board[7][i] != player:
              flag = current_situation.chess_board.board[7][i]
              break
            i = i + 1
          if flag == player or flag == 0:
            score[pos1] += 1000
          else:
            score[pos1] -= 1000

    if pos1 == (1,7):
      if current_situation.chess_board.board[0][7] != -player:
          score[pos1] -= 1000
      else:
          i = 2
          flag = player
          while( i < 8 ):
            if current_situation.chess_board.board[i][7] != player:
              flag = current_situation.chess_board.board[i][7]
              break
            i = i + 1
          if flag == player or flag == 0:
            score[pos1] += 1000
          else:
            score[pos1] -= 1000

    if pos1 == (7,6):
      if current_situation.chess_board.board[7][7] != -player:
          score[pos1] -= 1000
      else:
          i = 5
          flag = player
          while( i >= 0):
            if current_situation.chess_board.board[7][i] != player:
              flag = current_situation.chess_board.board[7][i]
              break
            i = i -1
          if flag == player or flag == 0:
            score[pos1] += 1000
          else:
            score[pos1] -= 1000

    if pos1 == (6,7):
      if current_situation.chess_board.board[7][7] != -player:
          score[pos1] -= 1000
      else:
          i = 5
          flag = player
          while( i >= 0 ):
            if current_situation.chess_board.board[i][7] != player:
              flag = current_situation.chess_board.board[i][7]
              break
            i = i -1
          if flag == player or flag == 0:
            score[pos1] += 1000
          else:
            score[pos1] -= 1000

    if pos1[0] == 1 or pos1[1] == 6:
      score[pos1] -= 200
    new_board = current_situation.try_it(pos1)

    newPieces = []
    newPieces = new_board.new_pieces
    for piece in newPieces:  
      if piece[0] > 0 and piece[0] < 7 and piece[1] > 0 and piece[1] < 7:
        if (new_board.chess_board.board[piece[0] - 1] != player and new_board.chess_board.board[piece[0] + 1] != player):
          score[pos1] += 50
        if (new_board.chess_board.board[piece[1] - 1] != player and new_board.chess_board.board[piece[1] + 1] != player):
          score[pos1] += 50
      if (piece[0] == 0 or piece[0] == 7) and piece[1] > 0 and piece[1] < 7:
        if (new_board.chess_board.board[piece[1] - 1] != player and new_board.chess_board.board[piece[1] + 1] != player):
           score[pos1] += 50
      if (piece[1] == 0 or piece[1] == 7) and piece[0] > 0 and piece[0] < 7:
        if (new_board.chess_board.board[piece[0] - 1] != player and new_board.chess_board.board[piece[0] + 1] != player):
          score[pos1] += 50
          
  return score.argMax(), score



def end_judge(current_situation):
    if current_situation.no_way == 2:
        score = util.Counter()
        player = current_situation.current_player
        
        for line in current_situation.chess_board.board:
            for point in line:
                if point == player:
                    score[player] += 1
                if point != player:
                    score[-player] += 1
        
        if score[player] > score[-player]:
            return 10000
        
        else:
            return -10000
            
    else:
        return 'not_end'

def MaxValue(current_situation, currentDepth, alpha, beta, depth=1):
    
    end = end_judge(current_situation)
    if end != 'not_end':
        return end
    else:
        pass
        
    if currentDepth == depth:
        return evaluationFunction(current_situation)
        
    else:
        v = -10000
        legal_points = current_situation.get_legal_points_without_direction()
    
        if len(legal_points) == 0:
            v = -10000
            return v
    
        for point in legal_points:
            v = max(v, MinValue(current_situation.try_it(point) ,currentDepth + 1, alpha, beta, depth))
    
            if v >= beta:
                return v
            else:
                pass
            
            alpha = max( alpha, v)
    
        return v

def MinValue(current_situation, currentDepth, alpha, beta, depth):
    
    end = end_judge(current_situation)
    if end != 'not_end':
        return end
    else:
        pass
      
    v = 10000
    legal_points = current_situation.get_legal_points_without_direction()
    
    if len(legal_points) == 0:
        v = 10000
        return v
    
    else:
        for point in legal_points:
            v = min(v, MaxValue(current_situation.try_it(point) ,currentDepth + 1, alpha, beta, depth))
        
            if v <= alpha:
                return v
            else:
                pass
        
            beta = min(beta, v)

        return v

def evaluationFunction(current_situation):
    legal_points = current_situation.get_legal_points_without_direction()
    
    if len(legal_points) == 0:
        return -10000

    arg_max, score = greenHandStrategy(current_situation)
  
    return score[arg_max]

def mediumStrategy(current_situation):
    legal_points = current_situation.get_legal_points_without_direction()     
    for pos1 in legal_points:
      if pos1 == (0,0) or pos1 == (0,7) or pos1 == (7,0) or pos1 == (7,7):
        return pos1, [1000]
    if len(current_situation.black_sequence) + len(current_situation.white_sequence) > 56:
        scores = [MaxValue(current_situation.try_it(point), 1, -100000, 100000, 5) for point in legal_points]  
    else:
        scores = [MaxValue(current_situation.try_it(point), 1, -100000, 100000, 2) for point in legal_points]
    bestScore = min(scores)
    bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
    chosenIndex = random.choice(bestIndices) # Pick randomly among the best

    return legal_points[chosenIndex], scores

def cp_determine(grade, current_situation):
    """make determination"""
    if grade == 'greenhand':
        c_p = greenHandStrategy
    elif grade == 'normal':
        c_p = normalStrategy
    else:
        c_p = medium_strategy
    
    if current_situation.current_player == 1:
        current_situation.determine(normalStrategy(current_situation)[0])
    else:
        current_situation.determine( c_p(current_situation)[0] )
  
 
 
def evaluation_function(current_situation):
    if len(current_situation.legal_points) == 0:
        return -10000
        
    else:
        next_situations = \
            [current_situation.try_it(point)
             for point in current_situation.legal_points]
             
        return [green_evaluation(next_st) for next_st in next_situations]
 
def max_value(current_situation, current_step, alpha, beta, depth=1):
    
    end = end_judge(current_situation)
    if end != 'not_end':
        return end
    else:
        pass
    
    if current_step == 0:
        best_index = []
        best_score = -100000
    else:
        pass
        
    if current_step / 2 == depth:
        return max(evaluation_function(current_situation))
        
    else:
        value = -10000
        legal_points = current_situation.get_legal_points_without_direction()
    
        if len(legal_points) == 0:
            value = -10000
            return value
    
        for point in legal_points:
            value = max(value, min_value(current_situation.try_it(point), \
                                         current_step + 1, alpha, beta, depth))
            
            if current_step == 0:
                if best_score < value:
                    best_score = value
                    best_index = [legal_points.index(point)]
                    best_point = [point]
                elif best_score == value:
                    best_index.append(legal_points.index(point))
                    best_point.append(point)
                else:
                    pass
            
            if value >= beta:
                return value
            
            else:
                alpha = max(alpha, value)
        
        if current_step == 0:
            return best_score, best_point        
        else:
            return value 

def min_value(current_situation, current_step, alpha, beta, depth):
    
    end = end_judge(current_situation)
    if end != 'not_end':
        return end
    else:
        pass
      
    value = 10000
    legal_points = current_situation.get_legal_points_without_direction()
    
    if len(legal_points) == 0:
        value = 10000
        return value
    
    else:
        for point in legal_points:
            value = min(value, max_value(current_situation.try_it(point), \
                                        current_step + 1, alpha, beta, depth))
        
            if value <= alpha:
                return value
            else:
                beta = min(beta, value)

        return value   


def medium_strategy(current_situation):
    """MiniMax for the game agent"""
    
    legal_points = current_situation.get_legal_points_without_direction()     
    
    for pos in legal_points:
        if pos == (0,0) or pos == (0,7) or pos == (7,0) or pos == (7,7):
            return pos, [1000]
        else:
            pass
    
    if len(current_situation.black_sequence) + len(current_situation.white_sequence) > 56:
        score, index = max_value(current_situation, 0, -100000, 100000, 8)
    
    else:
        score, index = max_value(current_situation, 0, -100000, 100000, 2)
    
    chosen_index = random.choice(index)
    chosen_point = random.choice(index)
    
    # return legal_points[chosen_index], score   
    # print score
    return chosen_point, score
    
    