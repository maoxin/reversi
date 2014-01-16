# -*- coding: cp936 -*-
import util
import random

def greenHandStragity(current_situation):
  legal_points = current_situation.get_legal_points_without_direction()
  score = util.Counter()
  player = current_situation.current_player
  
  for pos in legal_points:
    new_board = current_situation.try_it(pos)
    for line in new_board.chess_board.board:
      for point in line:
          if point == player:
              score[pos] += 1

  return score.argMax(), score

def normalStragity(current_situation):
  legal_points = current_situation.get_legal_points_without_direction()
  score = util.Counter()
  player = current_situation.current_player
  
  for pos in legal_points:
    new_board = current_situation.try_it(pos)
    bd = new_board.chess_board.board      
    for x in range(8):
        for y in range(8):
            if bd[x][y] != 0:
                if (x, y) == (0, 0) or (x, y) == (0, 7) or (x, y) == (7, 0) or (x, y) == (7, 7):
                    if bd[x][y] == player:
                        score[(x, y)] += 1000
                    else:
                        score[(x, y)] -= 1000
                elif x == 0 or x == 7 or y == 0 or y == 7:
                    if bd[x][y] == player:
                        score[(x, y)] += 400
                    else:
                        score[(x, y)] -= 400
                else:
                    if bd[x][y] == player:
                        score[(x, y)] += 50
                    else:
                        score[(x, y)] -= 50
          
          # if point == player:
              # score[pos] += 1
        
  # for pos1 in legal_points:
  #   if pos1 == (0,0) or pos1 == (0,7) or pos1 == (7,0) or pos1 == (7,7):
  #     score[pos1] += 1000
  #   if pos1[0] == 0 or pos1[0] == 7 or pos1[1] == 0 or pos1[1] == 7:
  #     score[pos1] += 200
  #   if pos1 == (1,1) or pos1 == (1,6) or pos1 == (6,1) or pos1 == (6,6):
  #     score[pos1] -= 1000
  # 
    # if pos1 == (1,0):
    #   if current_situation.chess_board.board[0][0] != -player:
    #       score[pos1] -= 1000
    #   else:
    #       i = 2
    #       flag = player
    #       while( i < 8 ):
    #         if current_situation.chess_board.board[i][0] != player:
    #           flag = current_situation.chess_board.board[i][0]
    #           break
    #         i = i + 1
    #       if flag == player or flag == 0:
    #         score[pos1] += 1000
    #       else:
    #         score[pos1] -= 1000

    # if pos1 == (0,1):
    #   if current_situation.chess_board.board[0][0] != -player:
    #       score[pos1] -= 1000
    #   else:
    #       i = 2
    #       flag = player
    #       while( i < 8):
    #         if current_situation.chess_board.board[0][i] != player:
    #           flag = current_situation.chess_board.board[0][i]
    #           break
    #         i = i + 1
    #       if flag == player or flag == 0:
    #         score[pos1] += 1000
    #       else:
    #         score[pos1] -= 1000


    # if pos1 == (6,0):
    #   if current_situation.chess_board.board[7][0] != -player:
    #       score[pos1] -= 1000
    #   else:
    #       i = 5
    #       flag = player
    #       while( i >= 0):
    #         if current_situation.chess_board.board[i][0] != player:
    #           flag = current_situation.chess_board.board[i][0]
    #           break
    #         i = i - 1
    #       if flag == player or flag == 0:
    #         score[pos1] += 1000
    #       else:
    #         score[pos1] -= 1000

    # if pos1 == (0,6):
    #   if current_situation.chess_board.board[0][7] != -player:
    #       score[pos1] -= 1000
    #   else:
    #       i = 5
    #       flag = player
    #       while( i >= 0 ):
    #         if current_situation.chess_board.board[0][i] != player:
    #           flag = current_situation.chess_board.board[0][i]
    #           break
    #         i = i -1
    #       if flag == player or flag == 0:
    #         score[pos1] += 1000
    #       else:
    #         score[pos1] -= 1000

    # if pos1 == (7,1):
    #   if current_situation.chess_board.board[7][0] != -player:
    #       score[pos1] -= 1000
    #   else:
    #       i = 2
    #       flag = player
    #       while( i < 8):
    #         if current_situation.chess_board.board[7][i] != player:
    #           flag = current_situation.chess_board.board[7][i]
    #           break
    #         i = i + 1
    #       if flag == player or flag == 0:
    #         score[pos1] += 1000
    #       else:
    #         score[pos1] -= 1000

    # if pos1 == (1,7):
    #   if current_situation.chess_board.board[0][7] != -player:
    #       score[pos1] -= 1000
    #   else:
    #       i = 2
    #       flag = player
    #       while( i < 8 ):
    #         if current_situation.chess_board.board[i][7] != player:
    #           flag = current_situation.chess_board.board[i][7]
    #           break
    #         i = i + 1
    #       if flag == player or flag == 0:
    #         score[pos1] += 1000
    #       else:
    #         score[pos1] -= 1000
    # 
    # if pos1 == (7,6):
    #   if current_situation.chess_board.board[7][7] != -player:
    #       score[pos1] -= 1000
    #   else:
    #       i = 5
    #       flag = player
    #       while( i >= 0):
    #         if current_situation.chess_board.board[7][i] != player:
    #           flag = current_situation.chess_board.board[7][i]
    #           break
    #         i = i -1
    #       if flag == player or flag == 0:
    #         score[pos1] += 1000
    #       else:
    #         score[pos1] -= 1000
    # 
    # if pos1 == (6,7):
    #   if current_situation.chess_board.board[7][7] != -player:
    #       score[pos1] -= 1000
    #   else:
    #       i = 5
    #       flag = player
    #       while( i >= 0 ):
    #         if current_situation.chess_board.board[i][7] != player:
    #           flag = current_situation.chess_board.board[i][7]
    #           break
    #         i = i -1
    #       if flag == player or flag == 0:
    #         score[pos1] += 1000
    #       else:
    #         score[pos1] -= 1000

    # if pos1[0] == 1 or pos1[1] == 6:
      # score[pos1] -= 200
    # new_board = current_situation.try_it(pos1)

    # newPieces = []
    # newPieces = new_board.new_pieces
    # for piece in newPieces:  
      # if piece[0] > 0 and piece[0] < 7 and piece[1] > 0 and piece[1] < 7:
        # if (new_board.chess_board.board[piece[0] - 1] != player and new_board.chess_board.board[piece[0] + 1] != player):
          # score[pos1] += 50
        # if (new_board.chess_board.board[piece[1] - 1] != player and new_board.chess_board.board[piece[1] + 1] != player):
          # score[pos1] += 50
      # if (piece[0] == 0 or piece[0] == 7) and piece[1] > 0 and piece[1] < 7:
        # if (new_board.chess_board.board[piece[1] - 1] != player and new_board.chess_board.board[piece[1] + 1] != player):
           # score[pos1] += 50
      # if (piece[1] == 0 or piece[1] == 7) and piece[0] > 0 and piece[0] < 7:
        # if (new_board.chess_board.board[piece[0] - 1] != player and new_board.chess_board.board[piece[0] + 1] != player):
          # score[pos1] += 50
          
  return score.argMax(), score

def MaxValue(current_situation, currentDepth, alpha, beta, depth=1):
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
        
    if currentDepth == depth:
      return evaluationFunction(current_situation)
    v = - 10000
    legal_points = current_situation.get_legal_points_without_direction()
    if len(legal_points) == 0:
      v = -10000
      return v
    for point in legal_points:
      v = max(v, MinValue(current_situation.try_it(point) ,currentDepth + 1, alpha, beta))
      if v >= beta:
        return v
      alpha = max( alpha, v)
    return v

def MinValue(current_situation, currentDepth, alpha, beta):
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
      
    v = 10000
    legal_points = current_situation.get_legal_points_without_direction()
    if len(legal_points) == 0:
      v = 10000
      return v
    for point in legal_points:
      v = min(v, MaxValue(current_situation.try_it(point) ,currentDepth + 1, alpha, beta))
      if v <= alpha:
        return v
      beta = min(beta, v)
    return v

def evaluationFunction(current_situation):
  legal_points = current_situation.get_legal_points_without_direction()
  if len(legal_points) == 0:
    return -10000
  arg_max, score = normalStragity(current_situation)
  # arg_max, score = greenHandStragity(current_situation)
  
  return score[arg_max]
    # return current_situation.get_legal_points_without_direction()[0]

def mediumStragity(current_situation):
    legal_points = current_situation.get_legal_points_without_direction()     
    for pos1 in legal_points:
      if pos1 == (0,0) or pos1 == (0,7) or pos1 == (7,0) or pos1 == (7,7):
        return pos1, [1000]
    if len(current_situation.black_sequence) + len(current_situation.white_sequence) > 56:
        scores = [MaxValue(current_situation.try_it(point), 1, -100000, 100000, 5) for point in legal_points]  
    elif len(current_situation.black_sequence) + len(current_situation.white_sequence) < 1:
        scores = [MaxValue(current_situation.try_it(point), 1, -100000, 100000, 1) for point in legal_points]
    else:
        scores = [MaxValue(current_situation.try_it(point), 1, -100000, 100000, 3) for point in legal_points]
    bestScore = min(scores)
    bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
    chosenIndex = random.choice(bestIndices) # Pick randomly among the best

    return legal_points[chosenIndex], scores

def cp_determine(grade, current_situation):
    """make determination"""
    if grade == 'greenhand':
        c_p = greenHandStragity
    elif grade == 'normal':
        c_p = normalStragity
    else:
        c_p = mediumStragity
    
    
    current_situation.determine( c_p(current_situation)[0] )
  
     
