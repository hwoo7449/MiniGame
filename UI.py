import sys
import pygame
from random import randint
from pygame.locals import *
import Modules.Functions as F
import Games.bricksBreak.main as bricksBreak
import Games.bomb_Game.main as bomb_Game
import Games.minesweeper.main as minesweeper
import Games.Omok.main as Omok

pygame.init()


FPS = 30
clock = pygame.time.Clock()


BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)


Title_Font = pygame.font.SysFont("malgungothic", 40)
Font = pygame.font.SysFont("malgungothic", 30)
screen_width = 800
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mini Game")
      

def randomColor():
    return (randint(0, 255), randint(0, 255), randint(0, 255))

def dark_randomColor():
    return (randint(0, 200), randint(0, 200), randint(0, 200))

def Check_mouse_pos(mouse_pos, Rect):
    if mouse_pos[0] > Rect.left and mouse_pos[0] < Rect.right and mouse_pos[1] > Rect.top and mouse_pos[1] < Rect.bottom:
        return True
    else:
        return False

Title = F.Text("Mini Game", Title_Font)
Title.rect.centerx = round(screen_width / 2)
Title.rect.y = 50

Game_Start = F.Text("게임 시작", Font)
Game_Start.rect.centerx = round(screen_width / 2)
Game_Start.rect.centery = round(screen_height / 2)

Game_List = F.Text("게임 목록", Font)
Game_List.rect.centerx = round(screen_width / 2)
Game_List.rect.centery = round(screen_height * (1/10))

Game1 = F.Text("벽돌깨기", Font, dark_randomColor())
Game1.rect.centerx = round(screen_width * (3/10))
Game1.rect.centery = round(screen_height * (3/10))

Game2 = F.Text("폭탄 피하기", Font, dark_randomColor())
Game2.rect.centerx = round(screen_width * (7/10))
Game2.rect.centery = round(screen_height * (3/10))

Game3 = F.Text("지뢰찾기", Font, dark_randomColor())
Game3.rect.centerx = round(screen_width * (3/10))
Game3.rect.centery = round(screen_height * (7/10))

Game4 = F.Text("오목", Font, dark_randomColor())
Game4.rect.centerx = round(screen_width * (7/10))
Game4.rect.centery = round(screen_height * (7/10))

Page = 1
running = True
while running:
    screen.fill(WHITE)

    if Page == 1:
        Title.Draw(screen)
        Game_Start.Draw(screen)
    elif Page == 2:
        Game_List.Draw(screen)
        Game1.Draw(screen)
        Game2.Draw(screen)
        Game3.Draw(screen)
        Game4.Draw(screen)

    pygame.display.update()
    for event in pygame.event.get():
        mouse_pos = pygame.mouse.get_pos()
        if event.type == QUIT:
            running = False

        if Page == 1:
            if event.type == MOUSEBUTTONDOWN:
                if Check_mouse_pos(mouse_pos, Game_Start.rect):
                    Page += 1
                    
                    
        
        if Page == 2:
            if event.type == MOUSEBUTTONDOWN:
                if Check_mouse_pos(mouse_pos, Game1.rect):
                    bricksBreak.main()
                    screen = pygame.display.set_mode((screen_width, screen_height))
                elif Check_mouse_pos(mouse_pos, Game2.rect):
                    bomb_Game.main()
                    screen = pygame.display.set_mode((screen_width, screen_height))
                elif Check_mouse_pos(mouse_pos, Game3.rect):
                    minesweeper.main()
                    screen = pygame.display.set_mode((screen_width, screen_height))
                elif Check_mouse_pos(mouse_pos, Game4.rect):
                    Omok.main()
                    screen = pygame.display.set_mode((screen_width, screen_height))



    clock.tick(FPS)


pygame.quit() 
sys.exit()