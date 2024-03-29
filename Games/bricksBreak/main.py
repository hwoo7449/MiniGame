import pygame
import random
import time
import Modules.Functions as F

def main():
    pygame.init() 

    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)
    large_font = pygame.font.SysFont("malgungothic", 72)
    small_font = pygame.font.SysFont("malgungothic", 36)
    screen_width = 800
    screen_height = 500
    screen = pygame.display.set_mode((screen_width, screen_height)) 

    clock = pygame.time.Clock() 

    Font = pygame.font.SysFont("malgungothic", 30)
    

    def runGame():
        score = 0
        missed = 3
        SUCCESS = 1
        FAILURE = 2
        game_over = 0

        bricks = []
        COLUMN_COUNT = 11
        ROW_COUNT = 7
        for column_index in range(COLUMN_COUNT):
            for row_index in range(ROW_COUNT):
                brick = pygame.Rect(column_index * (60 + 10) + 35, row_index * (16 + 5) + 35, 60, 16)
                bricks.append(brick)      

        ball = pygame.Rect(screen_width // 2 - 16 // 2, screen_height // 2 - 16 // 2, 16, 16)
        ball_dx = 3
        ball_dy = -3

        paddle = pygame.Rect(screen_width // 2 - 80 // 2, screen_height - 16, 80, 16)
        paddle_dx = 0

        running = True
        while running: 
            clock.tick(60)
            screen.fill(BLACK) 

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        paddle_dx = -7
                    elif event.key == pygame.K_RIGHT:
                        paddle_dx = 7
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        paddle_dx = 0
                    elif event.key == pygame.K_RIGHT:
                        paddle_dx = 0        

            paddle.left += paddle_dx

            ball.left += ball_dx
            ball.top  += ball_dy

            if ball.left <= 0:
                ball.left = 0
                ball_dx = -ball_dx
            elif ball.left >= screen_width - ball.width: 
                ball.left = screen_width - ball.width
                ball_dx = -ball_dx
            if ball.top < 0:
                ball.top = 0
                ball_dy = -ball_dy
            elif ball.top >= screen_height:
                missed -= 1
                ball.left = screen_width // 2 - ball.width // 2
                ball.top = screen_height // 2 - ball.width // 2
                ball_dy = -ball_dy 

            if missed <= 0:
                game_over = FAILURE 

            if paddle.left < 0:
                paddle.left = 0
            elif paddle.left > screen_width - paddle.width:
                paddle.left = screen_width - paddle.width

            for brick in bricks:
                if ball.colliderect(brick):
                    bricks.remove(brick)
                    ball_dy = -ball_dy
                    score += 1
                    break

            if ball.colliderect(paddle):
                ball_dy = -ball_dy
                if ball.centerx <= paddle.left or ball.centerx > paddle.right:
                    ball_dx = ball_dx * -1

            if len(bricks) == 0:
                print('success')
                game_over = SUCCESS

            #화면 그리기

            for brick in bricks:
                pygame.draw.rect(screen, GREEN, brick)

            if game_over == 0:
                pygame.draw.circle(screen, WHITE, (ball.centerx, ball.centery), ball.width // 2)

            pygame.draw.rect(screen, BLUE, paddle)

            score_image = small_font.render('점수 {}'.format(score), True, YELLOW)
            screen.blit(score_image, (10, 10))

            missed_image = small_font.render('목숨 {}'.format(missed), True, YELLOW)
            screen.blit(missed_image, missed_image.get_rect(right=screen_width - 10, top=10))

            if game_over > 0:
                if game_over == SUCCESS:
                    success_image = large_font.render('성공', True, RED)
                    screen.blit(success_image, success_image.get_rect(centerx=screen_width // 2, centery=screen_height // 2))
                elif game_over == FAILURE:
                    failure_image = large_font.render('실패', True, RED)
                    screen.blit(failure_image, failure_image.get_rect(centerx=screen_width // 2, centery=screen_height // 2))

                    while True:
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                running = False
                                return

            pygame.display.update()

        
    runGame()

if __name__ == "__main__":
    main()


