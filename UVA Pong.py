import pygame
import sys

pygame.init()

# Screen
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('UVA Pong Game')

# Colors (UVA Theme)
BLUE = (35, 45, 75)
ORANGE = (229, 114, 0)
WHITE = (255, 255, 255)

paddle_width, paddle_height = 10, 100
paddle_speed = 5

ball_radius = 7
ball_speed_x, ball_speed_y = 3, 3

# Paddles and Ball positions
left_paddle = pygame.Rect(30, height // 2 - paddle_height // 2, paddle_width, paddle_height)
right_paddle = pygame.Rect(width - 40, height // 2 - paddle_height // 2, paddle_width, paddle_height)
ball = pygame.Rect(width // 2, height // 2, ball_radius * 2, ball_radius * 2)

# Scoring
left_score = 0
right_score = 0
winning_score = 3

# Font for displaying score
font = pygame.font.Font(None, 74)


def draw_score():
    left_text = font.render(str(left_score), True, ORANGE)
    right_text = font.render(str(right_score), True, ORANGE)
    screen.blit(left_text, (width // 4, 20))
    screen.blit(right_text, (width * 3 // 4, 20))


def reset_ball():
    ball.x, ball.y = width // 2, height // 2
    pygame.time.delay(500)


def check_winner():
    if left_score == winning_score or right_score == winning_score:
        winner_text = font.render('Player 1 Wins!' if left_score == winning_score else 'Player 2 Wins!', True, ORANGE)
        screen.fill(BLUE)
        screen.blit(winner_text, (width // 4, height // 2 - 50))
        pygame.display.flip()
        pygame.time.delay(2000)  # Pause for 2 seconds
        return True
    return False


# Running Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Paddle movement for P1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= paddle_speed
    if keys[pygame.K_s] and left_paddle.bottom < height:
        left_paddle.y += paddle_speed

    # Paddle movement for P2
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= paddle_speed
    if keys[pygame.K_DOWN] and right_paddle.bottom < height:
        right_paddle.y += paddle_speed

    # Ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Collisions
    if ball.top <= 0 or ball.bottom >= height:
        ball_speed_y *= -1

    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_speed_x *= -1

    # Score
    if ball.left <= 0:
        right_score += 1
        reset_ball()

    if ball.right >= width:
        left_score += 1
        reset_ball()

    # Winning Condition
    if check_winner():
        left_score, right_score = 0, 0  # Reset scores after win

    # UVA Theme
    screen.fill(BLUE)
    pygame.draw.rect(screen, ORANGE, left_paddle)
    pygame.draw.rect(screen, ORANGE, right_paddle)
    pygame.draw.ellipse(screen, ORANGE, ball)

    # Draw scoreboard
    draw_score()

    # Display update
    pygame.display.flip()
    pygame.time.Clock().tick(60)
