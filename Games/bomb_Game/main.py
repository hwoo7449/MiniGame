import pygame
import os
import random
import Modules.Functions as F

Img_Dir = 'Resource/bomb_Game/'


def main():

    pygame.init()

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    size = [800, 500]
    screen = pygame.display.set_mode(size) 

    Font = pygame.font.SysFont("malgungothic", 30)

    clock = pygame.time.Clock()

    def runGame():

        bomb_image = pygame.image.load(Img_Dir + 'bomb.png')
        bomb_image = pygame.transform.scale(bomb_image, (50, 50))
        bombs = []

        for i in range(5):
            rect = pygame.Rect(bomb_image.get_rect())
            rect.left = random.randint(0, size[0])
            rect.top = -100
            dy = random.randint(3, 9)
            bombs.append({'rect': rect, 'dy': dy})

        person_image = pygame.image.load(Img_Dir + 'person.png')
        person_image = pygame.transform.scale(person_image, (100, 100))
        person = pygame.Rect(person_image.get_rect())
        person.left = size[0] // 2 - person.width // 2
        person.top = size[1] - person.height
        person_dx = 0
        person_dy = 0

        done = False
        running = True
        while running:
            clock.tick(30)
            screen.fill(BLACK)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        person_dx = -5
                    elif event.key == pygame.K_RIGHT:
                        person_dx = 5
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        person_dx = 0
                    elif event.key == pygame.K_RIGHT:
                        person_dx = 0

            for bomb in bombs:
                bomb['rect'].top += bomb['dy']
                if bomb['rect'].top > size[1]:
                    bombs.remove(bomb)
                    rect = pygame.Rect(bomb_image.get_rect())
                    rect.left = random.randint(0, size[0])
                    rect.top = -100
                    dy = random.randint(3, 9)
                    bombs.append({'rect': rect, 'dy': dy})

            person.left = person.left + person_dx

            if person.left < 0:
                person.left = 0
            elif person.left > size[0] - person.width:
                person.left = size[0] - person.width

            screen.blit(person_image, person)

            for bomb in bombs:
                if bomb['rect'].colliderect(person):
                    done = True
                screen.blit(bomb_image, bomb['rect'])
            
            if done:
                GO = F.Text("Game Over", Font, WHITE)
                GO.rect.centerx = round(size[0] / 2)
                GO.rect.centery = round(size[1] / 2)

                while True:
                    GO.Draw(screen)
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                            return

            pygame.display.update()

    runGame()

if __name__ == "__main__":
    main()