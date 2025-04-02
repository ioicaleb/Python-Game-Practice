import pgzrun
from random import randint

WIDTH = 800
HEIGHT = 600

dots = []
lines = []
red_dots = []

level = 1
timer = 30
game_over = False

def place_dots():
    global dots
    global lines
    global red_dots
    global timer
    timer += level * 5
    dots = []
    lines = []
    dots_per_level = 4 * level
    red_dots_per_level = level - 3
    if red_dots_per_level < 1:
        red_dots_per_level = 0
    for dot in range(0, dots_per_level):
        actor = Actor('dot', pos=(randint(20, (WIDTH - 20)), randint(20, (HEIGHT - 20))))
        dots.append(actor)
    for dot in range(0, red_dots_per_level):
        actor = Actor('red-dot', pos=(randint(20, (WIDTH - 20)), randint(20, (HEIGHT - 20))))
        red_dots.append(actor)

def draw():
    screen.fill("black")
    number = 1

    screen.draw.text('Time: ' + str(round(timer)), (150, 10), color="white")

    for dot in dots:
        screen.draw.text(str(number), (dot.pos[0], dot.pos[1] + 12))
        dot.draw()
        number += 1

    for dot in red_dots:
        dot.draw()
    
    for line in lines:
        screen.draw.line(line[0], line[1], (100, 0, 0))
    
    if game_over:
        screen.fill("red")
        screen.draw.text("Time out!\nGame Over!", (150, 50), fontsize=60)

def on_mouse_down(pos):
    global next_dot
    global lines
    clicked_red = False
    for dot in red_dots:
        if dot.collidepoint(pos):
            clicked_red = True
    if dots[next_dot].collidepoint(pos):
        if next_dot:
            lines.append((dots[next_dot - 1].pos, dots[next_dot].pos))
        next_dot += 1
    elif clicked_red:
        global timer
        timer -= 5
    else:
        lines = []
        next_dot = 0

def time_up():
    global game_over
    game_over = True

def update():
    global timer
    global next_dot
    global level 
    timer -= 1 / 60

    if timer <= 0:
        time_up()

    if next_dot == dots.__len__():
        level += 1
        next_dot = 0
        place_dots()

next_dot = 0

place_dots()

pgzrun.go()