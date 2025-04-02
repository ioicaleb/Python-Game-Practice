import pgzrun
import random

FONT_COLOR = (255, 255, 255)
WIDTH = 1200
HEIGHT = 900
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
CENTER = (CENTER_X, CENTER_Y)
FINAL_LEVEL = 20
START_SPEED = 20
LOSE_COLORS = ["green", "blue"]

game_over = False
game_complete = False
current_level = 1

stars = []
animations = []

def handle_game_over():
    global game_over
    game_over = True

def get_colors(extra_stars):
    colors = ["red"]

    for i in range(0, extra_stars):
        random_color = random.choice(LOSE_COLORS)
        colors.append(random_color)
    
    return colors

def create_stars(colors):
    new_stars = []

    for color in colors:
        star = Actor(color + "-star")
        new_stars.append(star)
    
    return new_stars

def layout_stars(stars):
    gaps = len(stars) + 1
    gap_size = WIDTH / gaps
    random.shuffle(stars)
    for index, star in enumerate(stars):
        x = (index + 1) * gap_size
        star.x = x

def animate_stars(stars):
    for star in stars:
        duration = START_SPEED - current_level
        star.anchor = ("center", "bottom")
        animation = animate(star, duration = duration, on_finished = handle_game_over, y = HEIGHT)
        animations.append(animation)

def make_stars(level):
    colors = get_colors(level)
    new_stars = create_stars(colors)
    layout_stars(new_stars)
    animate_stars(new_stars)

    return new_stars

def draw():
    global stars, current_level, game_over, game_complete
    screen.clear()
    screen.blit("space", (0, 0))

    if game_over:
        display_message("GAME OVER!", "Try Again.")
    elif game_complete:
        display_message("YOU WON!", "Well Done.")
    else:
        for star in stars:
            star.draw()

def stop_animations(animations):
    for animation in animations:
        if animation.running:
            animation.stop()

def display_message(heading, subheading):
    screen.draw.text(heading, fontsize = 60, color = FONT_COLOR, center = CENTER)
    screen.draw.text(subheading, fontsize = 30, center = (CENTER_X, CENTER_Y + 30), color = FONT_COLOR)

def red_star_click():
    global current_level, stars, animations, game_complete
    stop_animations(animations)

    if current_level == FINAL_LEVEL:
        game_complete = True
    else:
        current_level += 1
        stars = []
        animations = []

def on_mouse_down(pos):
    global stars, current_level

    for star in stars:
        if star.collidepoint(pos):
            if "red" in star.image:
                red_star_click()
            else:
                handle_game_over()

def update():
    global stars
    if len(stars) == 0:
        stars = make_stars(current_level)

pgzrun.go()