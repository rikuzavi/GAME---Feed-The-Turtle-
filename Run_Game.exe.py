import turtle
import random

screen = turtle.Screen()
screen.setup(700, 500)
screen.bgcolor("black")

tr = turtle.Turtle()
wn = turtle.Screen()
wn.addshape('image_turtle.gif')
tr.shape('image_turtle.gif')
tr.speed(1)
tr.setpos(0,150)


start_text = turtle.Turtle()
start_text.hideturtle()
start_text.penup()
start_text.color("#16FF00")
start_text.setpos(-125, -70)
start_text.write(" \n         WELCOME TO\n     FEED THE TURTLE\n               PRESS\n\n* ENTER to start game\n* ESC to exit\n* SPACE to pause while gaming", font=("Arial", 15, "bold"))

rule = turtle.Turtle()
rule.hideturtle()
rule.penup()
rule.color("#16FF00")
rule.setpos(-340, -240)
rule.write("TASK: Try to beat the high score. Speed and size will increase upto level 6.\nRULE: failed to catch food 5 times in total means GAME OVER", font=("Arial", 10, "bold"))


with open("high","r") as f:
    high_score=f.read()
high = turtle.Turtle()
high.hideturtle()
high.penup()
high.color("#16FF00")
high.setpos(-340, 200)
high.write(f"High Score: {high_score}",font=("Arial", 10, "bold"))

missed=0
def start():
    global score,level
    screen.onkey(None, "r")
    wn.clear()
    wn.bgcolor("black")
    tr.clear()

    start_text.clear()
    start_text.setpos(-340, 225)
    start_text.write("FEED THE TURTLE", font=("Arial", 13, "bold"))
    screen.onkey(None, "Return")

    high.write(f"High Score: {high_score}", font=("Arial", 10, "bold"))

    score = 0
    score_display = turtle.Turtle()
    score_display.hideturtle()
    score_display.penup()
    score_display.color("#16FF00")
    score_display.setpos(230, 220)
    score_display.write(f"Score: {score}", font=("Arial", 12, "bold"))

    level = 1
    lvl = turtle.Turtle()
    lvl.hideturtle()
    lvl.penup()
    lvl.color("#16FF00")
    lvl.setpos(160, 220)
    lvl.write(f"Lvl: {level}", font=("Arial", 12, "bold"))

    miss=0
    food_missed = turtle.Turtle()
    food_missed.hideturtle()
    food_missed.penup()
    food_missed.color("#16FF00")
    food_missed.setpos(-85, 220)
    food_missed.write(f"Food Missed : {miss}", font=("Arial", 11, "bold"))

    player = turtle.Turtle()
    player.hideturtle()
    player.penup()
    player.shape("turtle")
    player.shapesize(1, 1, 1)
    player.color("#16FF00")
    player.sety(-200)
    player.showturtle()
    player.setheading(90)
    player.speed(10)

    object = turtle.Turtle()
    object.hideturtle()
    object.penup()
    object.shape("circle")
    object.shapesize(stretch_wid=0.5, stretch_len=0.5)
    object.color("red")
    object.setpos(random.randint(-225, 225), 300)
    object.showturtle()

    def game_over():
        object.clear()
        object.ht()
        player.clear()
        player.ht()
        score_display.clear()
        start_text.clear()
        start_text.setpos(-100, 0)
        start_text.color("#16FF00")
        start_text.write("GAME OVER\nTotal food missed : 5\n\n\npress R to restart", font=("Arial", 15, "bold"))

    paused = False
    def move_circular():
        L = [i * 10 for i in range(1, 501)]
        nonlocal paused
        global score,level,missed,miss
        base_speed=6
        if level <= 5:
            speed = base_speed + (level - 1) * 1
        else:
            speed = base_speed + 4 * 1
        if not paused:
            object.sety(object.ycor() - speed)
            if object.ycor() < -250:
                missed += 1
                miss=missed
                food_missed.clear()
                food_missed.write(f"Food Missed : {miss}", font=("Arial", 11, "bold"))
                score-=1
                if missed>=5:
                    game_over()
                    score=0
                    level=1
                    missed=0
                    update_level()
                    screen.onkeypress(start, "r")
                    return False
                object.hideturtle()
                object.setpos(random.randint(-225, 225), 300)
                object.showturtle()
                update_score()
                update_level()
            elif player.distance(object) < 21:
                score+=1
                if score in L:
                    level+=1
                    update_level()
                object.hideturtle()
                object.setpos(random.randint(-225, 225), 300)
                object.showturtle()
                update_score()
                update_level()
        screen.ontimer(move_circular, 15)
    move_circular()

    def update_score():
        global high_score
        score_display.clear()
        score_display.write(f"Score: {score}", font=("Arial", 12, "bold"))
        if score>int(high_score):
            high_score = score
            high.clear()
            high.write(f"High Score: {high_score}", font=("Arial", 10, "bold"))
            with open("high","w") as fr:
                fr.write(str(high_score))

    def update_level():
        global level
        L = [i * 10 for i in range(1, 501)]
        for i in range(len(L)):
            if score < L[i]:
                level = i + 1
                break
        else:
            level = len(L) + 1
        lvl.clear()
        lvl.write(f"Lvl: {level}",font=("Arial", 12, "bold"))
        increase_turtlesize()

    def increase_turtlesize():
        L = [i * 10 for i in range(1, 501)]
        global level
        if level > 1 and level<=5:
            player_size = 1 + (level - 1) * 0.2
            player.shapesize(player_size, player_size, player_size)

    def toggle_pause():
        nonlocal paused
        paused = not paused
        start_text.clear()
        if paused:
            player.hideturtle()
            start_text.write("GAME PAUSED\npress SPACE to resume", font=("Arial", 15, "bold"))
        else:
            start_text.write("FEED THE TURTLE", font=("Arial", 13, "bold"))
            player.showturtle()

    def move_left():
        if player.xcor() > -325:
            player.setx(player.xcor() - 10)

    def move_right():
        if player.xcor() < 325:
            player.setx(player.xcor() + 10)

    def cheatcode():
        player.showturtle()

    screen.onkeypress(move_left, "Left")
    screen.onkeypress(move_right, "Right")
    screen.onkeypress(cheatcode, "`")
    screen.onkeypress(toggle_pause, "space")
    screen.onkey(exit, "Escape")
    screen.listen()

screen.onkey(start, "Return")
screen.onkey(exit, "Escape")
screen.listen()
turtle.mainloop()

