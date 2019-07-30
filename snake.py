import turtle
import random #We'll need this later in the lab

turtle.tracer(1,0) #This helps the turtle move more smoothly

food_num = 1

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window  
                             #size.    
turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 12
time_step = 100


#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("circle")

#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()


#Function to draw a part of the snake on the screen

def new_stamp():
    snake_pos = snake.pos() #Get snake’s position
    #Append the position tuple to pos_list
    pos_list.append(snake_pos) 
    #snake.stamp() returns a stamp ID. Save it in some variable         
    x = snake.stamp()
    #append that stamp ID to stamp_list.     
    stamp_list.append(x)

#Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e. START_LENGTH)
for i  in range(START_LENGTH) :
    x_pos=snake.pos()[0] #Get x-position with snake.pos()[0]
    y_pos=snake.pos()[1] 

    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?    
    # You're RIGHT!
    x_pos+=SQUARE_SIZE 

    snake.goto(x_pos,y_pos) #Move snake to new (x,y)
   
    #Now draw the new snake part on the screen (hint, you have a 
    #function to do this
    new_stamp()

def remove_tail():
    old_stamp = stamp_list.pop(0) # last piece of tail
    snake.clearstamp(old_stamp) # erase last piece of tail
    pos_list.pop(0) # remove last piece of tail's position


snake.direction = "Up"
up_edge = 250
down_edge = -250
right_edge = 400
left_edge = -400

def up():
    snake.direction="Up" #Change direction to up
    
def down():
    snake.direction="Down" #Change direction to up
    
def right():
    snake.direction="Right" #Change direction to up
   
def left():
    snake.direction="Left" #Change direction to up
   


#2. Make functions down(), left(), and right() that change snake.direction
####WRITE YOUR CODE HERE!!

turtle.onkeypress(up, "Up") # Create listener for up key
turtle.onkeypress(down, "Down")
turtle.onkeypress(right, "Right")
turtle.onkeypress(left, "Left")

#3. Do the same for the other arrow keys
####WRITE YOUR CODE HERE!!

turtle.listen()

#ADD THE LINES BELOW

turtle.register_shape("trash.gif") #Add trash picture
                      # Make sure you have downloaded this shape 
                      # from the Google Drive folder and saved it
                      # in the same folder as this Python script

food = turtle.clone()
food.shape("trash.gif") 
#Locations of food
food_pos = []
food_stamps = []

# Write code that:
#1. moves the food turtle to each food position
#2. stamps the food turtle at that location
#3. saves the stamp by appending it to the food_stamps list using
# food_stamps.append(    )
#4. Don't forget to hide the food turtle!


def make_food():
    #The screen positions go from -SIZE/2 to +SIZE/2
    #But we need to make food pieces only appear on game squares
    #So we cut up the game board into multiples of SQUARE_SIZE.
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)-1
    
    #Pick a position that is a random multiple of SQUARE_SIZE
    

    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE

    food_pos.append((food_x, food_y))
    
    
    ####WRITE YOUR CODE HERE!!
    food.goto(food_x, food_y)
    y = food.stamp()
    food_stamps.append(y)

        ##1.WRITE YOUR CODE HERE: Make the food turtle go to the randomly-generated
        ##                        position 
        ##2.WRITE YOUR CODE HERE: Add the food turtle's position to the food positions list
        ##3.WRITE YOUR CODE HERE: Add the food turtle's stamp to the food stamps list


def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    
    #If snake.direction is up, then we want the snake to change
    #it’s y position by SQUARE_SIZE
    if snake.direction == "Up":
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
    elif snake.direction=="Down":
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
    elif snake.direction == "Right":
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
    elif snake.direction == "Left":
        snake.goto(x_pos - SQUARE_SIZE, y_pos)

    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    if new_x_pos >= right_edge or new_x_pos <= left_edge or new_y_pos >= up_edge or new_y_pos <= down_edge:
        print("You hit the edge! GAME OVER!!!")
        quit()


    #4. Write the conditions for RIGHT and LEFT on your own
    ##### YOUR CODE HERE

    #Make the snake stamp a new square on the screen
    #Hint - use a single function to do this
    new_stamp()

    ######## SPECIAL PLACE - Remember it for Part 5

    if len(food_stamps) < food_num:
        make_food()

    
    if snake.pos() in food_pos:
        food_index = food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_index])
        food_pos.pop(food_index)
        food_stamps.pop(food_index)
        

    else:
        remove_tail()
    

    if snake.pos() in pos_list[:-1]:
        quit()
    
    #remove the last piece of the snake (Hint Functions are FUN!)
    

    turtle.ontimer(move_snake, time_step)


move_snake()


turtle.mainloop()
