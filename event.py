import pygame, sys
from pygame.locals import *
from board_space import *

def event_handler(a_timer):
    """dealing with event"""
    for event in pygame.event.get():
        if event.type == QUIT:
            a_timer.terminal = True
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            a_timer.terminal = True
            sys.exit()
            
        else:
            if event.type == MOUSEBUTTONDOWN:
                board_pos = pygame.mouse.get_pos()
                pos = board2virtual(board_pos)
                if pos:
                    return pos
    
        return False