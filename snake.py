import turtle
import random

turtle.tracer(1,0)
#the size of the snake field
SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X,SIZE_Y)

turtle.penup()

SQUARE_SIZE=20
START_LENGTH=1

#all of the lists i will use in the snake game
pos_list=[]#list of the snake positions(where is the snake)
stamp_list=[]#number of square stamps which the snake is made of  
food_pos=[]#list of food position(where is the food)
food_stamps=[]#number of food stamps

snake=turtle.clone()
snake.shape('square')
snake.color('blue')
turtle.bgcolor('black')
turtle.color('white')


turtle.hideturtle()#in order for the snake wont leave a marks behinde it

for i in range(START_LENGTH):
    x_pos=snake.pos()[0]
    y_pos=snake.pos()[1]

    x_pos+=SQUARE_SIZE

    my_pos=(x_pos,y_pos)
    snake.goto(x_pos,y_pos)

    pos_list.append(my_pos)

    my_stamp1=snake.stamp()
    stamp_list.append(my_stamp1)

UP_ARROW='Up'
LEFT_ARROW='Left'
DOWN_ARROW='Down'
RIGHT_ARROW='Right'
TIME_STEP=100

SPACEBAR='space'

UP=0
LEFT=1
DOWN=2
RIGHT=3

direction=UP

UP_EDGE=250
DOWN_EDGE=-250
LEFT_EDGE=-400
RIGHT_EDGE=400
#make the snake move according to the arrows on the keyboard
def up():
    global direction
    if direction!=DOWN:
        direction=UP
    print('you pressed the up key')

def down():
    global direction
    if direction!=UP:
        direction=DOWN
    print('you pressed the down key')
    
def left():
    global direction
    if direction!=RIGHT:
        direction=LEFT
    print('you pressed the left key')
    
def right():
    global direction
    if direction!=LEFT:
        direction=RIGHT
    print('you pressed the right key')

turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)

turtle.listen()
#make new food at random places
def make_food():
    min_x=-int(SIZE_X/2.5/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2.5/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2.5/SQUARE_SIZE)+1
    max_y=int(SIZE_Y/2.5/SQUARE_SIZE)-1
    food_x=random.randint(min_x,max_x)*SQUARE_SIZE
    food_y=random.randint(min_y,max_y)*SQUARE_SIZE
    
    food.goto(food_x,food_y)
    food_pos.append((food_x,food_y))
    my_food_stamp=food.stamp()
    food_stamps.append(my_food_stamp)
     
    
                          
#maoves the snake randomly
def move_snake():
    my_pos=snake.pos()
    x_pos=my_pos[0]
    y_pos=my_pos[1]

    
    
    if snake.pos() in pos_list[0:-2]:
        print('you comitted suicide')
        quit()
        
    if direction==RIGHT:
        snake.goto(x_pos+SQUARE_SIZE,y_pos)
        print('you moved right')
    elif direction==LEFT:
        snake.goto(x_pos-SQUARE_SIZE,y_pos)
        print('you moved left')     
    elif direction==UP:
        snake.goto(x_pos,y_pos+SQUARE_SIZE)
        print('you moved up')
    elif direction==DOWN:
        snake.goto(x_pos,y_pos-SQUARE_SIZE)
        print('you moved down')
                
    my_pos=snake.pos()
    pos_list.append(my_pos)
    my_stamp2=snake.stamp()
    stamp_list.append(my_stamp2)

    global food_stamps,food_pos
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_ind])
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        my_stamp1=snake.stamp()
        make_food()
        pos_list.append(snake.pos())
        stamp_list.append(my_stamp1)
        print('you have eaten the food')
        print(len(stamp_list)-2)
      
    
    my_stamp1=stamp_list.pop(0)
    snake.clearstamp(my_stamp1)
    pos_list.pop(0)
                
    new_pos=snake.pos()
    new_x_pos=new_pos[0]
    new_y_pos=new_pos[1]

    if new_x_pos>=RIGHT_EDGE:
        print('you hit the right edge! game over!')
        quit()
    if new_x_pos<=LEFT_EDGE:
        print('you hit the left edge! game over!')
        quit()
    if new_y_pos>=UP_EDGE:
      print('you hit the up edge! game over!')
      quit()
    if new_y_pos<=DOWN_EDGE:
      print('you hit the down edge! game over!')
      quit()
   
    TIME_STEP=100
    turtle.ontimer(move_snake,TIME_STEP)


food=turtle.clone()
food.shape('turtle')
food_pos=[(100,100)]
food_stamps=[]

food.hideturtle()
for this_food_pos in food_pos:
    food.goto(this_food_pos)
    my_food_stamp=food.stamp()
    food_stamps.append(my_food_stamp)


turtle.goto(-400,-250)
turtle.pendown()
turtle.goto(-400,250)
turtle.goto(400,250)
turtle.goto(400,-250)
turtle.goto(-400,-250)
turtle.penup()
        
  
move_snake()
   
    
    
turtle.mainloop()    
    
