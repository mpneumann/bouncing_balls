import pygame
import random
import sys

pygame.init()

#window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("mason's bouncing balls game")

clock = pygame.time.Clock()
fps = 60

class Ball:
    def __init__(self, x, y, r, color, speed_x, speed_y):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.speed_x = speed_x
        self.speed_y = speed_y

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        #walls bouncing 
        if self.x - self.r < 0 or self.x + self.r >= width:
            self.speed_x *= -1
        if self.y - self.r < 0 or self.y + self.r >= height:
            self.speed_y *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

#random ball gen 
balls = []

def create_balls(num_balls):
    global balls
    balls = []
    for _ in range(num_balls):
        r = random.randint(10, 30)
        x = random.randint(r, width - r)
        y = random.randint(r, height - r)
        color = random.choice([
            (255, 0, 0),  # red
            (0, 255, 0),
            (0, 0, 255),
            (255, 255, 0),
            (255, 0, 255),
            (0, 255, 255)
        ])
        speed_x = random.uniform(-5, 5)
        speed_y = random.uniform(-5, 5)
        balls.append(Ball(x, y, r, color, speed_x, speed_y))

is_running = False
start_stop_key = pygame.K_SPACE #key

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == pygame.KEYDOWN:
        if event.key == start_stop_key:
            is_running = not is_running

def get_ball_count_input():
    font = pygame.font.Font(None, 36)
    input_box = pygame.Rect(width // 2 - 100, height // 2 - 20, 200, 40)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos): #click on active rec
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            elif event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        done = True
                        return int(text) if text.isdigit() else 10
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
        screen.fill((30, 30, 30))
        txt_surface = font.render(text, True, color)
        width_box = max(200, txt_surface.get_width() + 10)
        input_box.w = width_box

        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()
        clock.tick(30)

num_balls = get_ball_count_input()
create_balls(num_balls)

def draw_speed_slider(speed_factor):
    pygame.draw.rect(screen, (200, 200, 200), (50, height - 50, width - 100, 10))
    pos_x = 50 + (width - 100) * (speed_factor / 10)
    pygame.draw.circle(screen, (255, 0, 0), (int(pos_x), height - 45), 10)

def get_speed_factor():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if 40 <= mouse_y <= height - 40:
        return None
    speed_factor = ((mouse_x - 50) / (width - 100)) * 10
    speed_factor = max(0.1, min(speed_factor, 10))
    return speed_factor

def handle_collisions():
    for i in range(len(balls)):
        for j in range(i + 1, len(balls)):
            ball1 = balls[i]
            ball2 = balls[j]
            dx = ball1.x - ball2.x
            dy = ball1.y - ball2.y
            distance = (dx**2 + dy**2) ** 0.5
            if distance < ball1.r + ball2.r:
                ball1.speed_x, ball2.speed_x = ball2.speed_x, ball1.speed_x
                ball1.speed_y, ball2.speed_y = ball2.speed_y, ball1.speed_y

antigravity = False
antigravity_timer = 5000
last_switch = pygame.time.get_ticks()

while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == start_stop_key:
                is_running = not is_running
    speed_factor = 1

    if pygame.mouse.get_pressed()[0]:
        new_speed = get_speed_factor()
        if new_speed:
            speed_factor = new_speed

    if is_running:
        for ball in balls:
            ball.speed_x *= speed_factor
            ball.speed_y *= speed_factor
            ball.move()
            ball.speed_x /= speed_factor
            ball.speed_y /= speed_factor
        handle_collisions()

    for ball in balls:
        ball.draw(screen)

    draw_speed_slider(speed_factor)

    current_time = pygame.time.get_ticks()
    if current_time - last_switch >= antigravity_timer:
        antigravity = not antigravity
        last_switch = current_time
        for ball in balls:
            ball.speed_y *= -1

    pygame.display.flip()
    clock.tick(fps)
