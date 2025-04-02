import pgzrun

WIDTH = 1280
HEIGHT = 720

main_box = Rect(50, 40, 820, 240)
timer_box = Rect(990, 40, 240, 240)
answer_1 = Rect(50, 358, 495, 165)
answer_2 = Rect(735, 358, 495, 165)
answer_3 = Rect(50, 538, 495, 165)
answer_4 = Rect(735, 538, 495, 165)

answer_boxes = [answer_1, answer_2, answer_3, answer_4]

score = 0
timer = 10

q1 = ["What is the capital of France?", "London", "Paris",  "Berlin", "Tokyo", 2]
q2 = ["What is 5 + 7?", "12", "10",  "14", "8", 1]
q3 = ["What is the seventh month of the year?", "April", "May",  "June", "July", 4]
q4 = ["Which planet is closest to the sun?", "Saturn", "Neptune",  "Mercury", "Venus", 3]
q5 = ["Where are the Great Pyramids of Giza?", "India", "Egypt",  "Morocco", "Saudi Arabia", 2]
q6 = ["What is a quarter of 200?", "50", "100",  "25", "150", 1]
q7 = ["Which is the largest state in the USA?", "Wyoming", "Alaska",  "Texas", "Florida", 2]
q8 = ["How many wives did Henry VIII have?", "8", "4",  "6", "1", 3]

questions = [q1, q2, q3, q4, q5, q6, q7, q8]

question = questions.pop(0)

def draw():
    screen.fill("fire brick")
    screen.draw.filled_rect(main_box, "light cyan")
    screen.draw.filled_rect(timer_box, "light cyan")

    for box in answer_boxes:
        screen.draw.filled_rect(box, "gold")
    
    screen.draw.textbox(str(timer), timer_box, color = ("black"))
    screen.draw.textbox(question[0], main_box, color = ("black"))

    i = 1
    for box in answer_boxes:
        screen.draw.textbox(question[i], box, color = ("black"))
        i += 1

def game_over():
    global question, timer
    message = "Game over. You got %s questions correct!" % str(score)
    question = [message, "-", "-", "-", "-", 5]
    timer = 0

def correct_answer():
    global question, timer, score
    score += 1
    if questions:
        question = questions.pop(0)
        timer = 10
    else:
        print("End of questions")
        game_over()

def on_mouse_down(pos):
    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            print("Clicked on answer " + str(index))
            if index == question[5]:
                print("Correct!")
                correct_answer()
            else:
                print("Incorrect!")
                game_over()
        index += 1

def update_timer():
    global timer
    if timer:
        timer = timer - 1
    else:
        game_over()

clock.schedule_interval(update_timer, 1.0)

pgzrun.go()