import turtle
import random #We'll need this later in the lab

turtle.tracer(1,0) #This helps the turtle move more smoothly

SIZE_X=1000
SIZE_Y=1000
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window  
                             #size.    
turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 6
TIME_STEP = 100

#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
turtle.register_shape("pac.gif")
snake.shape("pac.gif")
snake.color("turquoise")

#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()

#Function to draw a part of the snake on the screen

def new_stamp():
    snake_pos = snake.pos() #Get snake’s position
    #Append the position tuple to pos_list
    pos_list.append(snake_pos) 
   #snake.stamp() returns a stamp ID. Save it in some variable       
    id1 = snake.stamp()
    #append that stamp ID to stamp_list.     
    stamp_list.append(id1)

#Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e. START_LENGTH)
for number in range(5) :
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

UP_EDGE = 600
DOWN_EDGE = -600
RIGHT_EDGE = 600
LEFT_EDGE = -600

def up():
    snake.direction="Up" #Change direction to up 
    print("You pressed the up key!")

#2. Make functions down(), left(), and right() that change snake.direction
####WRITE YOUR CODE HERE!!
def down():
    snake.direction="Down" #Change direction to up
    print("You pressed the down key!")

def right():
    snake.direction="Right" #Change direction to up
    print("You pressed the right key!")

def left():
    snake.direction="Left" #Change direction to up
    print("You pressed the left key!")


turtle.onkeypress(up, "Up") # Create listener for up key

#3. Do the same for the other arrow keys
####WRITE YOUR CODE HERE!!
turtle.onkeypress(down, "Down")
turtle.onkeypress(right, "Right")
turtle.onkeypress(left, "Left")
turtle.listen()


turtle.register_shape("donuty1.gif") #Add trash picture
                      # Make sure you have downloaded this shape 
                      # from the Google Drive folder and saved it
                      # in the same folder as this Python script

food = turtle.clone()
food.shape("donuty1.gif") 

#Locations of food
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []

# Write code that:
#1. moves the food turtle to each food position
#2. stamps the food turtle at that location
#3. saves the stamp by appending it to the food_stamps list using
# food_stamps.append(    )
#4. Don't forget to hide the food turtle!


for this_food_pos in food_pos :
    ####WRITE YOUR CODE HERE!!
    food.goto(this_food_pos)
    id2=food.stamp()
    food_stamps.append(id2)
    food.hideturtle()



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

        ##1.WRITE YOUR CODE HERE: Make the food turtle go to the randomly-generated
        ##                        position 
        ##2.WRITE YOUR CODE HERE: Add the food turtle's position to the food positions list
        ##3.WRITE YOUR CODE HERE: Add the food turtle's stamp to the food stamps list
    food.goto(food_x,food_y)
    food_pos.append(food.pos())
    food_stamps.append(food.stamp())

    

turtle.register_shape("bomby.gif") 
                    
bombs = turtle.clone()
bombs.shape("bomby.gif") 



#Locations of bombs
bombs_pos = [(200,200), (-200,200), (-200,-200), (200,-200)]
bombs_stamps = []




for this_bombs_pos in bombs_pos :
    ####WRITE YOUR CODE HERE!!
    bombs.goto(this_bombs_pos)
    id7=bombs.stamp()
    bombs_stamps.append(id7)
    bombs.hideturtle()



def make_bombs():
    #The screen positions go from -SIZE/2 to +SIZE/2
    #But we need to make food pieces only appear on game squares
    #So we cut up the game board into multiples of SQUARE_SIZE.
    min2_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max2_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min2_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
    max2_y=int(SIZE_Y/2/SQUARE_SIZE)-1
    
    #Pick a position that is a random multiple of SQUARE_SIZE
    bombs_x = random.randint(min2_x,max2_x)*SQUARE_SIZE
    bombs_y = random.randint(min2_y,max2_y)*SQUARE_SIZE

        ##1.WRITE YOUR CODE HERE: Make the food turtle go to the randomly-generated
        ##                        position 
        ##2.WRITE YOUR CODE HERE: Add the food turtle's position to the food positions list
        ##3.WRITE YOUR CODE HERE: Add the food turtle's stamp to the food stamps list
    food.goto(food_x,food_y)
    food_pos.append(food.pos())
    food_stamps.append(food.stamp())
    


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

    #4. Write the conditions for RIGHT and LEFT on your own
    ##### YOUR CODE HERE
    elif snake.direction=="Right":
        snake.goto(x_pos+SQUARE_SIZE,y_pos)
    elif snake.direction=="Left":
        snake.goto(x_pos-SQUARE_SIZE,y_pos)

 
    #Make the snake stamp a new square on the screen
    #Hint - use a single function to do this
    new_stamp()



    ######## SPECIAL PLACE - Remember it for Part 5
    #If snake is on top of food item
    if snake.pos() in food_pos:
        food_index=food_pos.index(snake.pos()) #What does this do?
        food.clearstamp(food_stamps[food_index]) #Remove eaten food stamp
        food_pos.pop(food_index) #Remove eaten food position
        food_stamps.pop(food_index) #Remove eaten food stamp
        print("You have eaten the food!")
    
    #HINT: This if statement may be useful for Part 8
        new_stamp()

    ...
    #Don't change the rest of the code in move_snake() function:
    #If you have included the timer so the snake moves 
    #automatically, the function should finish as before with a 
    #call to ontimer()
    #<--Last line of function
    if snake.pos() in bombs_pos:
        print("you have touched a bomb! Game Over!")
        quit()
    



    #remove the last piece of the snake (Hint Functions are FUN!)
    remove_tail()


    
    
    

    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    # The next three lines check if the snake is hitting the 
    # right edge.
    if new_x_pos >= RIGHT_EDGE:
         print("You hit the right edge! Game over!")
         quit()


    elif new_y_pos >= UP_EDGE:
         print("You hit the up edge! Game over!")
         quit()

    
    elif new_y_pos <= DOWN_EDGE:
         print("You hit the down edge! Game over!")
         quit()

    
    elif new_x_pos <= LEFT_EDGE:
         print("You hit the left edge! Game over!")
         quit()
    



    if len(food_stamps) <= 6:
       make_food()




    if snake.pos() in pos_list[:-2]:
        print("Your head touched a part of your body! Game over!")
        quit()
        

    turtle.ontimer(move_snake,TIME_STEP)
move_snake()

  
    

turtle.mainloop()
