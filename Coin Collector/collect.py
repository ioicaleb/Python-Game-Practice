import pgzrun
from random import randint

game_over = False

fox = Actor("fox")
fox.pos = 100, 100

coin = Actor("coin")
coin.pos = 200, 200

hedgehog = Actor("hedgehog")
hedgehog.pos = 300, 300

WIDTH = 400
HEIGHT = 400

score = 0

timer = 120

def draw():
    screen.fill("green")

    fox.draw()
    coin.draw()
    hedgehog.draw()

    screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))
    screen.draw.text('Time: ' + str(round(timer)), (150, 10), color="black")

    if game_over:
        screen.fill("pink")
        screen.draw.text("Final Score: " + str(score), topleft=(10, 10), fontsize=60)

def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))

def time_up():
    global game_over
    game_over = True

def update():
    global score

    if keyboard.left:
        fox.x -= 2
    if keyboard.right:
        fox.x += 2
    if keyboard.up:
        fox.y -= 2
    if keyboard.down:
        fox.y += 2
    
    if fox.x > (WIDTH - 20):
         fox.x = WIDTH - 20
    elif fox.x < 20:
         fox.x = 20
    if fox.y > (HEIGHT - 20):
         fox.y = HEIGHT - 20
    elif fox.y < 20:
         fox.y = 20

    coin_collected = fox.colliderect(coin)

    if coin_collected:
        score += 10
        place_coin()

    hedgehog_direction = randint(0,3)

    if hedgehog_direction == 0:
            hedgehog.x -= 5
    elif hedgehog_direction == 1:
            hedgehog.x += 5
    elif hedgehog_direction == 2:
            hedgehog.y -= 5
    elif hedgehog_direction == 3:
            hedgehog.y += 5
    
    if hedgehog.x > (WIDTH - 20):
         hedgehog.x = WIDTH - 20
    elif hedgehog.x < 20:
         hedgehog.x = 20
    if hedgehog.y > (HEIGHT - 20):
         hedgehog.y = HEIGHT - 20
    elif hedgehog.y < 20:
         hedgehog.y = 20

    if fox.colliderect(hedgehog):
        time_up()

    global timer
    timer -= 1 / 60

clock.schedule(time_up, 120.0)

place_coin()

pgzrun.go()