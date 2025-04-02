import pgzrun
from random import randint

timer = 3

apple = Actor("apple")
orange = Actor("orange")
pineapple = Actor("pineapple")

score = 0

def draw():
    screen.clear()
    apple.draw()
    orange.draw()
    orange.pos = -100, -100
    pineapple.draw()
    pineapple.pos = -100, -100
    screen.draw.text('Time: ' + str(round(timer)), (330,10), color=(255,255,255), fontsize=30)

def update():
    global timer
    timer -= 1 / 60

    if timer <= 0:
        print("Out of Time!")
        print("You hit " + str(score) + " apple" + "s!" if  score > 1 else "!")
        quit()

def place_orange():
    orange.x = randint(10, 800)
    orange.y = randint(10, 600)

def place_pineapple():
    pineapple.x = randint(10, 800)
    pineapple.y = randint(10, 600)

def place_apple():
    if score > 4:
        place_orange()
    if score > 9:
        place_pineapple()

    apple.x = randint(10, 800)
    apple.y = randint(10, 600)

    while apple.x == orange.x or apple.x == pineapple.x:
        apple.x = randint(10, 800)
    while apple.y == orange.y or apple.y == pineapple.y:
        apple.y = randint(10, 600)

def on_mouse_down(pos):
    if orange.collidepoint(pos):
        print("On no! You shot the orange!")
        print("You hit " + str(score) + " apple" + "s!" if  score > 1 else "!")
        quit()
    elif pineapple.collidepoint(pos):
        print("On no! You shot the pineapple!")
        print("You hit " + str(score) + " apple" + "s!" if  score > 1 else "!")
        quit()
    elif apple.collidepoint(pos):
        print("Good shot!")
        global score
        score += 1
        global timer
        timer = 3
        if score > 14:
            timer = 2
        if score > 24:
            timer = 1
        place_apple() 
    else:
        print("You missed!")
        print("You hit " + str(score) + " apple" + "s!" if  score > 1 else "!")
        quit()

place_apple()

pgzrun.go()
