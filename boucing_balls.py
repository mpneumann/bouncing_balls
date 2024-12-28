import pygame
import random
import sys
import csv
from datetime import datetime

pygame.init()

width, height = 1000, 600  
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("SPY Stats - Bouncing Balls")

clock = pygame.time.Clock()
fps = 60

props = []

max_chg = 0
min_chg = float('inf')

with open('Download Data - FUND_US_ARCX_SPY (1).csv', 'r') as f:
    rows = list(csv.DictReader(f))[:60]  
    for row in rows:
        dt = datetime.strptime(row['Date'], '%m/%d/%Y')
        op = float(row['Open'].replace(',', ''))
        cl = float(row['Close'].replace(',', ''))

        chg = cl - op
        pct = (chg / op) * 100
        abs_pct = abs(pct)

        if abs_pct > max_chg:
            max_chg = abs_pct
        if abs_pct < min_chg:
            min_chg = abs_pct

        clr = (0, 255, 0) if chg > 0 else (255, 0, 0)

        props.append({
            'Date': dt,
            'Open_Price': op,
            'Close_Price': cl,
            'Price_Change': chg,
            'Percent_Price_Change': pct,
            'Ball_Size': 15,
            'Color': clr,
        })

min_spd = 1
max_spd = 10

for p in props:
    abs_pct = abs(p['Percent_Price_Change'])
    if max_chg == min_chg:
        spd = (min_spd + max_spd) / 2
    else:
        spd = min_spd + (abs_pct - min_chg) * (max_spd - min_spd) / (max_chg - min_chg)
    p['Speed'] = spd

class Ball:
    def __init__(self, x, y, r, clr, sx, sy, dt, cl, op, lbl):  
        self.x = x
        self.y = y
        self.r = r
        self.clr = clr
        self.sx = sx
        self.sy = sy
        self.dt = dt
        self.cl = cl
        self.op = op
        self.lbl = lbl

    def move(self):
        self.x += self.sx
        self.y += self.sy

        if self.x - self.r < 0:
            self.x = self.r
            self.sx *= -1
        elif self.x + self.r > width:
            self.x = width - self.r
            self.sx *= -1
        if self.y - self.r < 0:
            self.y = self.r
            self.sy *= -1
        elif self.y + self.r > height:
            self.y = height - self.r
            self.sy *= -1

    def draw(self, scr, fnt):
        pygame.draw.circle(scr, self.clr, (int(self.x), int(self.y)), self.r)
        lbl_surf = fnt.render(str(self.lbl), True, (255, 255, 255))  
        lbl_rect = lbl_surf.get_rect(center=(self.x, self.y))
        scr.blit(lbl_surf, lbl_rect)

    def clicked_on(self, pos):
        """ Check if the ball was clicked. """
        d = ((self.x - pos[0]) ** 2 + (self.y - pos[1]) ** 2) ** 0.5
        return d < self.r

balls = []

def create_balls(n):
    global balls
    balls = []
    fnt = pygame.font.Font(None, 24) 
    for i in range(min(n, len(props))):
        p = props[i]
        
        r = p['Ball_Size']
        x = random.randint(int(r), width - int(r))
        y = random.randint(int(r), height - int(r))

        clr = p['Color']
        sx = p['Speed'] * random.choice([-1, 1])
        sy = p['Speed'] * random.choice([-1, 1])
        dt = p['Date'].strftime('%m/%d/%Y')
        cl = p['Close_Price']
        op = p['Open_Price']
        
        lbl = i + 1
        balls.append(Ball(x, y, int(r), clr, sx, sy, dt, cl, op, lbl))

def handle_collisions():
    for i in range(len(balls)):
        for j in range(i + 1, len(balls)):
            b1 = balls[i]
            b2 = balls[j]
            dx = b1.x - b2.x
            dy = b1.y - b2.y
            d = (dx**2 + dy**2) ** 0.5
            md = b1.r + b2.r
            if d < md:
                ovr = 0.5 * (md - d)
                if d != 0:
                    b1.x += (ovr * dx) / d
                    b1.y += (ovr * dy) / d
                    b2.x -= (ovr * dx) / d
                    b2.y -= (ovr * dy) / d
                else:
                    b1.x += random.uniform(-ovr, ovr)
                    b1.y += random.uniform(-ovr, ovr)
                    b2.x += random.uniform(-ovr, ovr)
                    b2.y += random.uniform(-ovr, ovr)

                nx = dx / d if d != 0 else 1
                ny = dy / d if d != 0 else 0
                tx = -ny
                ty = nx

                t1 = b1.sx * tx + b1.sy * ty
                t2 = b2.sx * tx + b2.sy * ty

                n1 = b1.sx * nx + b1.sy * ny
                n2 = b2.sx * nx + b2.sy * ny

                b1.sx = tx * t1 + nx * n2
                b1.sy = ty * t1 + ny * n2
                b2.sx = tx * t2 + nx * n1
                b2.sy = ty * t2 + ny * n1

def show_spread(b, fnt):
    """ display the open-close spread for the clicked ball. """
    spd = b.cl - b.op
    txt = f"Open-Close Spread for {b.dt}: {spd:.2f}"
    surf = fnt.render(txt, True, (255, 255, 255))  
    screen.blit(surf, (10, height - 40)) 

run = True  
sel_ball = None

n_balls = 60  
create_balls(n_balls)

print(f"Number of balls created: {len(balls)}")

# Add a paused state variable
paused = False

while True:
    screen.fill((0, 0, 0))

    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evt.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for b in balls:
                if b.clicked_on(pos):
                    sel_ball = b
                    break  
            else:
                sel_ball = None
        elif evt.type == pygame.KEYDOWN:
            if evt.key == pygame.K_SPACE:
                paused = not paused  

    if not paused:
        for b in balls:
            b.move()
        handle_collisions()

    # Always draw the balls
    fnt = pygame.font.Font(None, 24) 
    for b in balls:
        b.draw(screen, fnt)

    if sel_ball:
        show_spread(sel_ball, fnt)

    pygame.display.flip()
    clock.tick(fps)
