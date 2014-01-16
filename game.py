#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import threading, time
import util
from evaluation_funtion import *
from chess_obj import *
from load import *
from board_space import *
from event import *


st = time.time()
pygame.init()
size = width, height = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Reversi')


background, back_rect = load_image('棋盘.png')
black_piece, black_rect = load_image('叉.png')
white_piece, white_rect = load_image('圆.png')
pygame.mixer.music.load( os.path.join('music', 'violin.ogg') )
pygame.mixer.music.play(-1)

if pygame.font:
    font_time = pygame.font.Font('/Library/Fonts/Zapfino.ttf', 20)
    text_time = font_time.render("0", 1, (10, 10, 10))
    text_tm_pos = text_time.get_rect(centerx=background.get_width()/2 - 30, centery=60)
    
    font_title = pygame.font.Font('/Library/Fonts/Herculanum.ttf', 36)
    text_title = font_title.render("REVERSI", 1, (10, 10, 10))
    text_t_pos = text_title.get_rect(centerx=background.get_width()/2)
    background.blit(text_title, text_t_pos)
    
    font_black = pygame.font.Font('/Library/Fonts/Brush Script.ttf', 30)
    text_black = font_black.render("Cross", 1, (10, 10, 10))
    score_black = font_black.render("2", 1, (10, 10, 10))
    text_b_pos = text_black.get_rect(centerx=96, centery=214)
    score_b_pos = score_black.get_rect(centerx=96, centery=268)
    background.blit(text_black, text_b_pos)
    
    font_white = pygame.font.Font('/Library/Fonts/Brush Script.ttf', 30)
    text_white = font_white.render("Circle", 1, (10, 10, 10))
    score_white = font_white.render("2", 1, (10, 10, 10))
    text_w_pos = text_white.get_rect(centerx=704, centery=214)
    score_w_pos = score_white.get_rect(centerx=704, centery=268)
    background.blit(text_white, text_w_pos)

screen.blit(background, (0, 0))
pygame.display.flip()
v_2_b = virtual2board()

game = CurrentSituation()
game_config = {}

def config(game_config):
    """configure the game, change the player and grade"""
    
    # mode = raw_input("PVP or PVE or EVE? ").lower()
    mode = 'eve'
    player = None
    grade = 'medium'
    # if mode == 'pve':
        # player = raw_input("Black or White? ").lower()
    # if mode != 'pvp':
        # print "Grade - greenhand, normal, medium: "
        # grade = raw_input().lower()
    # else:
        # grade = None
    
    game_config = {
        'mode': mode,
        'player': player,
        'grade': grade
    }
    
    return game_config

def update(current_situation, current_player, timer):
    """refresh the board image based on current situation"""
    screen.blit(background, (0, 0))
    time_min, time_sec = str(timer.timed / 60), str(timer.timed % 60)
    text_time = font_time.render(time_min + " : " + time_sec, 1, (10, 10, 10))
    screen.blit(text_time, text_tm_pos)
    
    score_black = font_black.render(str(len(current_situation.black_sequence)), 1, (10, 10, 10))
    screen.blit(score_black, score_b_pos)
    score_white = font_black.render(str(len(current_situation.white_sequence)), 1, (10, 10, 10))
    screen.blit(score_white, score_w_pos)
    
    mouse_pos = pygame.mouse.get_pos()
    
    if game_config['mode'] == 'pvp' or game_config['player'] == current_player:
        if current_player == 'black':
            black_rect.center = mouse_pos
            screen.blit(black_piece, black_rect)
        else:
            white_rect.center = mouse_pos
            screen.blit(white_piece, white_rect)
            
    
    black_poses, white_poses = current_situation.piece_sequence
    black_poses = [(pos[0]+1, pos[1]+1) for pos in black_poses]
    white_poses = [(pos[0]+1, pos[1]+1) for pos in white_poses]
    
    for pos in black_poses:
        board_pos = v_2_b[pos]['center']
        black_rect.centerx, black_rect.centery = board_pos
        screen.blit(black_piece, black_rect)
        
    for pos in white_poses:
        board_pos = v_2_b[pos]['center']
        white_rect.centerx, white_rect.centery = board_pos
        screen.blit(white_piece, white_rect)
    
    pygame.display.flip()
    
    if current_situation.no_way == 2:
        return False
    
    return True    

game_config = config(game_config)
game_on = True

def cp_play(player, game):
    cp_determine(game_config['grade'], game)
    
    return 0
    

class Timer(object):
    """docstring for Timer"""
    def __init__(self):
        self.timed = 0
        self.terminal = False
    
    def time_now(self, start_time):
        while not self.terminal:
            current_time = time.time()
            if current_time - start_time > self.timed + 1:
                self.timed += 1
            
        return 0    

all_start_time = time.time()   
game_timer = Timer()            
g_timer = threading.Thread(target=game_timer.time_now, args=(all_start_time,))
# g_timer.start()

class Update_machine(object):
    """docstring for Update_machine"""
    def __init__(self):
        self.terminal = False

    def update_machine(self):
        if game.current_player == game.black_sign:
            player = 'black'
        else:
            player = 'white'
        
        while not self.terminal:
            update(game, player, game_timer)
            time.sleep(1)

# update_mc = Update_machine()    
# update_machine_thread = threading.Thread(target=update_mc.update_machine, args=())
# update_machine_thread.start()
   
while True:     
    if game.current_player == game.black_sign:
        player = 'black'
    else:
        player = 'white'
        
    game_on = update(game, player, game_timer)
    
    if game_config['mode'] == 'pvp':
        pos = event_handler(game_timer)    
        if pos:
            game.determine( (pos[0]-1, pos[1]-1) )
    
    elif game_config['mode'] == 'pve':
        cp = threading.Thread(target=cp_play, args=(player, game))
        
        if player != game_config['player']:
            cp.start()
            
            while cp.is_alive():
                pass
               
            game_on = update(game, player, game_timer) 
        
        pos = event_handler(game_timer)    
        if pos:
            game.determine( (pos[0]-1, pos[1]-1) )
            if game_config['grade'] != 'medium':
                begin_time = time.time()
                while time.time() - begin_time <0.5:
                    game_on = update(game, player, game_timer)
                
    else:
        cp_determine(game_config['grade'] ,game)
        event_handler(game_timer)
        game_on = update(game, player, game_timer)
    
    if not game_on:
        score = game.update_chess_piece_sequence()
        print "X:", score[0]
        print "O:", score[1]
        if score[0] > score[1]:
            print "X win!"
        elif score[0] < score[1]:
            print "O win!"
        else:
            print "Tie.."
        
        game_timer.terminal = True
        # update_mc.terminal = True
        break
ed = time.time()    
# print ed - st    
# raw_input("input any to quit.")