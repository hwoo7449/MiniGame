import sys
import pygame
from random import randint
from pygame.locals import *

pygame.init()


FPS = 30
FramePerSec = pygame.time.Clock()


BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)


Title_Font = pygame.font.SysFont("malgungothic", 40)
Font = pygame.font.SysFont("malgungothic", 30)
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mini Game")


class Text:
    def __init__(self, text, color = BLACK, font = Font):
        self.font = font
        self.color = color
        self.text = font.render(text, True, color)
        self.rect = self.text.get_rect()

Box_list = []
class MovingBox:
    global Box_list

    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.color = randomColor()
        self.size_width = 10
        self.size_height = 10
        self.pos_x = (screen.get_width() + self.size_width)
        self.pos_y = randint(10, screen.get_height() - self.size_height)
        self.rect = [ self.pos_x, self.pos_y, self.size_width, self.size_height ]
        self.dx = -randint(5, 15)

    def Add(self):
        Box_list.append(self)

    def Del(self):
        Box_list.remove(self)
        del self
        return

    def Draw(self):
        if self.rect[0] < -self.size_width:
            self.Del()
            return

        pygame.draw.rect(self.screen, self.color, self.rect)

    def Move(self):
        self.rect[0] += self.dx

def randomColor():
    return (randint(0, 255), randint(0, 255), randint(0, 255))

def CheckBox():
    #if len(Box_list) < 10:
        Box_list.append(MovingBox(screen))

def AllBoxMove():
    for i in Box_list:
        i.Move()
        i.Draw()


Title = Text("Mini Game", BLACK, Title_Font)
Title.rect.centerx = round(screen_width / 2)
Title.rect.y = 50

Page = 1
running = True
while running:
    screen.fill(WHITE)

    CheckBox()
    AllBoxMove()

    if Page == 1:
        screen.blit(Title.text, Title.rect)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    FramePerSec.tick(FPS)


pygame.quit()
sys.exit()