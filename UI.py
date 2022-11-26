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
Test = Font.render("MING", True, BLACK)
Test.get_rect()
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

class MovingBox:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.size_width = randint(20, 100)
        self.size_height = randint(20, 100)
        self.pos_x = (screen.get_width() + self.size_width)
        self.pos_y = randint(10, screen.get_height() - self.size_height)
        self.rect = [ self.pos_x, self.pos_y, self.size_width, self.size_height ]

    def Draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

Title = Text("Mini Game", font=Title_Font)
Title.rect.centerx = round(screen_width / 2)
Title.rect.y = 50

Box1 = MovingBox(screen)

Page = 1
running = True
while running:
    screen.fill(WHITE)



    if Page == 1:
        Box1.Draw()
        screen.blit(Title.text, Title.rect)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    FramePerSec.tick(FPS)


pygame.quit()
sys.exit()