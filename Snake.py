from turtle import *
from random import randrange
from freegames import square, vector
import random


food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def colorRand(init):
    "Randomizes the colors"
    
    val=random.randrange(1,6) #Genera un número del 1 al 5 aleatoriamente 
    if val==1: #En caso de que sea 1
        color = 'cyan' 
    if val==2: #En caso de que sea 2
        color = 'black'
    if val==3: #En caso de que sea 3
        color = 'green'
    if val==4: #En caso de que sea 4
        color =  'purple'
    if val==5: #En caso de que sea 5
        color = 'orange'
    if color==init:
        color=colorRand(color)
    return color
        
snakeColor=colorRand('red') #Se especificca el color de la serpiente
foodColor=colorRand(snakeColor) #Se especifica el color de la comida


def foodRand():
    "Change food random position"

    val = random.randrange(1,5) #Genera un número del 1 al 4

    if val == 1: #Si el número aleatorio generado es 1
        if food.x <= 190: #Si la comida está casi en la orilla derecha, ya no tomará esta opción
            food.x += 10 #La comida se moverá una unidad a la derecha

    if val == 2: #Si el número aleatorio generado es 2
        if food.x >= -190: #Si la comida está casi en la orilla izquierda, ya no tomará esta opción
            food.x -= 10 #La comida se moverá una unidad a la izquierda

    if val == 3: #Si el número aleatorio generado es 3
        if food.y <= 190: #Si la comida está casi en la parte superior, ya no tomará esta opción
            food.y += 10 #La comida se moverá una unidad hacia arriba

    if val == 4: #Si el número aleatorio generado es 4
        if food.y >= -190: #Si la comida está casi en la parte inferior, ya no tomará esta opción
            food.y -= 10 #La comida se moverá una unidad hacia abajo
    

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, snakeColor) #Se utiliza la variable del color de la serpiente 

    square(food.x, food.y, 9, foodColor) #Se utiliza la variable del color de la comida
    foodRand() #Inicializa el método para mover la comida de manera aleatoria
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()