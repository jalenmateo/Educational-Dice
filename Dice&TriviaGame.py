# Project title: Computational Thinking For Design (CDT) 1D Project. Dice Trivia Game
from tkinter import * 
from tkinter.ttk import * 
from tkinter import messagebox 
import random 

window = Tk() 
window.title("I AM NOT THE ROCK")
 
width_of_board = 600 
height_of_board = 600 
width_of_game = 900

rows = 15 
cols = 15 
 
# colour of object
RED_COLOR = "#EE4035" 
BLUE_COLOR_LIGHT = '#67B0CF' 

# colour of wall
BLUE_COLOR = "#0492CF" 
RED_COLOR_LIGHT = '#EE7E77' 

Green_color = "#7BC043" 
 
# dimensions of of game
canvas = Canvas(window, width=width_of_game, height=height_of_board) 
canvas.grid()

maze = Frame(window)

board = [] 

for i in range(rows): 
    for j in range(cols): 
        board.append((i, j)) 
 
    for i in range(rows): 
        # creating vertical lines 
        canvas.create_line( 
            i * height_of_board / rows, 0, i * height_of_board / rows, height_of_board, 
        ) 
 
    for i in range(cols): 
        # creating horizontal lines 
        canvas.create_line( 
            0, i * width_of_board / cols, width_of_board, i * width_of_board / cols, 
        ) 
print(set(board))
# Set a starting point for object
obj = canvas.create_rectangle(280,560,320,600, fill=RED_COLOR_LIGHT, outline=BLUE_COLOR) 
 

# function for generating wall 
def place_wall(): 
    occupied_cells=[(7,0), (7,1), (6,1), (5,1), (4, 1), (3, 1), (2, 1), 
    (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (1,7), (1,8), (1,9), (1,10),
    (1,11), (1,12), (1,13), (2,13), (3,13), (4,13), (5,13), (6,13),(7,13),(7,14)]
    unoccupied_cells = set(board)-set(occupied_cells)
    # randomising placement of wall
    wall_cell = (random.choice(list((unoccupied_cells)))) 
    row_h = int(height_of_board / rows) 
    col_w = int(width_of_board / cols) 

    while True:
        x1 = wall_cell[0] * row_h 
        y1 = wall_cell[1] * col_w 
        x2 = x1 + row_h 
        y2 = y1 + col_w
        wall_coord = x1,y1,x2,y2

        return wall_coord 
 
 
wall_coords = [] 
# generating multiple walls
for i in range(100): 
    wall_coord = place_wall() 
    char_obj = canvas.create_rectangle( 
    wall_coord[0], wall_coord[1], wall_coord[2], wall_coord[3], fill=BLUE_COLOR_LIGHT, outline=RED_COLOR,) 
    wall_coords.append(wall_coord) 


wall_borders = []
# functions for generating boarders aorund the maze
def place_border(x,y):
    row_h = int(height_of_board / rows) 
    col_w = int(width_of_board / cols) 

    # top left corner of maze
    wall_border = (0,0,40,40)
    x1b = wall_border[0]
    y1b = wall_border[1]
    canvas.create_rectangle( 
    wall_border[0], wall_border[1], wall_border[2], wall_border[3], fill=BLUE_COLOR_LIGHT, outline=RED_COLOR) 
    
    # creating baorders for 1st column and 1st row
    for n in range (14):
        x1b += x
        y1b += y
        x2b = x1b + row_h 
        y2b = y1b + col_w 
        wall_border= (x1b,y1b,x2b,y2b)

        # boarder not created at end point
        if wall_border == (280,0,320,40):
            continue
        canvas.create_rectangle( 
        wall_border[0], wall_border[1], wall_border[2], wall_border[3], fill=BLUE_COLOR_LIGHT, outline=RED_COLOR) 
        wall_borders.append(wall_border)

    #  bottom right corner of maze    
    wall_border = (560,560,600,600)
    x1b = wall_border[0]
    y1b = wall_border[1]
    canvas.create_rectangle( 
    wall_border[0], wall_border[1], wall_border[2], wall_border[3], fill=BLUE_COLOR_LIGHT, outline=RED_COLOR) 
    
    # creating baorders for last column and last row
    for n in range (15):
        x1b -= x
        y1b -= y
        x2b = x1b + row_h 
        y2b = y1b + col_w 
        wall_border = (x1b,y1b,x2b,y2b)

        # boarder not created at start point
        if wall_border == (280,560,320,600):
            continue
        canvas.create_rectangle( 
        wall_border[0], wall_border[1], wall_border[2], wall_border[3], fill=BLUE_COLOR_LIGHT, outline=RED_COLOR) 
        wall_borders.append(wall_border)

    return wall_borders
    
place_border(40,0)
place_border(0,40)


# function for movement of object
def obj_move(event): 
    row_h = int(height_of_board / rows) 
    col_w = int(width_of_board / cols) 
    al = canvas.coords(obj) 

    # moving left
    if event.keysym == "Left": 
        if ((al[0] - col_w , al[1] , al[2] - col_w , al[3]) in wall_coords or (al[0] - col_w , al[1] , al[2] - col_w , al[3]) in wall_borders) or move_count==0: 
            exit 
        else: 
            canvas.move(obj,-row_h,0) 
            move_check() 

    # moving right
    elif event.keysym == "Right": 
        if ((al[0] + col_w , al[1] , al[2] + col_w , al[3]) in wall_coords or (al[0] + col_w , al[1] , al[2] + col_w , al[3]) in wall_borders) or move_count==0: 
            exit 
        else: 
            canvas.move(obj,row_h,0) 
            move_check() 
    
    # moving up
    elif event.keysym == "Up": 
        if ((al[0] , al[1] - col_w , al[2] , al[3] - col_w) in wall_coords or (al[0] , al[1] - col_w , al[2] , al[3] - col_w) in wall_borders) or move_count==0: 
            exit 
        else: 
            canvas.move(obj,0,-col_w) 
            move_check() 

    # moving down
    elif event.keysym == "Down": 
        if ((al[0] , al[1] + col_w , al[2] , al[3] + col_w) in wall_coords or (al[0] , al[1] + col_w , al[2] , al[3] + col_w) in wall_borders) or move_count==0: 
            exit 
        else: 
            canvas.move(obj,0,col_w) 
            move_check() 

# binding keys to obj movement
window.bind("<Key>", obj_move) 


move_count = 0
woohoo = 0 
 
def roll_dice(): 
    # make a list for the dice faces (unicodes) 
     dice_codes = ['\u2680', '\u2681', 
                   '\u2682','\u2683', 
                   '\u2684','\u2685'] 
     # assign the dice faces to a value in a dictionary 
     numbers = {'\u2680':1, '\u2681':2, 
                '\u2682':3, '\u2683':4, 
                '\u2684':5, '\u2685':6} 
     
     # get a random dice face 
     d = random.choice(dice_codes) 
      
     global woohoo 
     global move_count 
 
     if move_count != 0: 
        return move_count 
 
     # return dice rolled number 
     if d in numbers.keys(): 
        d_number = numbers[d] 
 
     # for the dice number labels 
     dice1.config(text=d) 
 
     # for the dice faces 
     dice1_number.config(text=f'Dice Score: {d_number}') 
     
     move_count += d_number 
     woohoo += d_number 
 
     # configure and update total rolled number 
     total_numbers.config(text=f'Total Score: {woohoo}') 
      
# frame to display dice 
frame = Frame(window) 
frame.grid(row=0, column=1, pady=5, padx = 1) 
 # dice labels 
dice1 = Label(frame, font=('ariel', 50)) 
#dice1.grid(row=1, column=1, padx=1, columnspan=2, rowspan=2) 
dice1.grid(row = 0, column = 2, padx = 1, pady = 10) 
 
# dice number labels 
dice1_number = Label(frame, font=('ariel', 25)) 
dice1_number.grid(row=1, column=2, padx=5, pady = 10, columnspan=2, rowspan=2) 
 
# roll dice button 
button = Button(window, text='Roll Dice', command=roll_dice)#, state = DISABLED) 
 
button.grid(row=1, column=1, pady=10, padx = 5, columnspan=2) 
# total label 
 
total_numbers = Label(window, text='', font=('ariel', 25)) 
total_numbers.grid(row=0, column=1, pady=5, padx = 5) 
 
total_score = Label(window, text='', font=('ariel', 25)) 
total_score.grid(row=0, column=2,padx=5, pady = 5)

# binding spacebar to rolling dice 
window.bind("<space>", roll_dice)


# questions and options
q = [

# mathematics
# question 1
["Category: Mathematics", "What is the definition of the mean value theorem?", 
"One point at which the tangent to the arc is parallel to the secant through its endpoints", 
"Average value of a function", 
"Minimum value for linear function", 
"I do not know"],

# question 2
["Category: Mathematics", "Which of the following is the correct definition for the first principle of differentiation?", 
"The slope of a tangent line to the curve at any instant", 
"Antiderivative", 
"fg(x)", 
"f=ma"],

# question 3
["Category: Mathematics", "Quick Mafs: What is 78 * 44?",
"3432",
"3778",
"4882",
"2990"],

# question 4
["Category: Mathematics", "Which of the following is the correct differentiation, f’(x), of f(x) = 22ln(x-2)?",
"22/(x-2)",
"-22/(x-2)",
"22(x-2)",
"-22(x-2)"],

# question 5
["Category: Mathematics", "Which of the following is the correct differentiation, f’(x), of f(x) = (4x-9)^3?",
"12(4x-9)^2",
"16(4x-9)^2",
"12(4x-9)^3",
"16(4x-9)^3"],

# question 6
["Category: Mathematics", "Which of the following formulas give the volume of a curve when rotated about the x-axis?",
"Integral of pi*f(x)^2 wrt x",
"Integral of pi f-1(x)^2 wrt x",
"Integral of 1 + f(x)^2 wrt x",
"Integral of 1 + f-1(x)^2 wrt x"],

# question 7
["Category: Mathematics", "What is the formula for the volume of a sphere?",
"4/3 (pi*r^3)",
"2/3 (pi*r^3)",
"1/3 (pi*h*r^2)",
"4/3 (pi*h*r^2)"],

# physics
# question 8
["Category: Physics", "What is Archimedes’ principle?",
"The magnitude of the buoyant force acting on an object in a fluid is equal to the weight of the fluid displaced",
"Upthrust = weight of object",
"The pressure at any point in a liquid is dependent on its depth",
"An object only floats when its weight is equal to the upthrust acting on it"],

# question 9
["Category: Physics", "Which of the following gives the range of values for the wavelengths of visible light?",
"400 - 700 nanometres",
"300 - 500 micrometres",
"1-3 metres",
"100 - 500 nanometres"],

# question 10
["Category: Physics", "Give the expression for centripetal acceleration:",
"v^2/r",
"mv^2/r",
"ma",
"-v^2/r"],

# question 11
["Category: Physics", "Give the formula for kinetic energy:",
"½mv^2",
"mgh",
"mv^2",
"f/a"],

# question 12
["Category: Physics", "What are the conditions for equilibrium?",
"No net moments about a pivot and no net force in any direction",
"No net force in any direction and object is stationary",
"Object is stationary",
"Object is not moving"],

# CDT
# question 13
["Category: CDT", "How do you disconnect the wire in rhino grasshopper?",
"right click + disconnect",
"F4",
"CTRL + ALT + DEL",
"connect the components"],

# question 14
["Category: CDT", "Give the definition of a float:",
"A number with a decimal point",
"A variable with no assigned value",
"A series of characters",
"A orange inflatable you use for swimming"],

# HASS
# question 15
["Category: HASS", "Which city was Lycurgus the ruler of?",
"Sparta",
"Athens",
"Singapura",
"Germany"],

# question 16
["Category: HASS", "In which of the following books was the main message that women and men were equal?",
"Tao Yuan Ming",
"Sultana’s Dream",
"Swastika Night",
"Sultans and their folklore"],

# question 17
["Category: HASS", "In Swastika Night, was Hermann gay?",
"He was bisexual",
"Yes",
"No",
"Maybe"],

# question 18
["Category: HASS", "Which of the characters in Thomas More’s Utopia had actually been to Utopia?",
"Hythloday",
"Sister Sara",
"Thomas More",
"Rem"],

# question 19
["Category: HASS", "In Parallel Lives by Plutarch, which style of governance was present in Sparta?",
"Democracy",
"Oligarchy",
"Monarchy",
"Kentucky"],
]


# indicate end of game when obj moves to the ending point
def posi_check():
    if canvas.coords(obj) == [280,0,320,40]:
        messagebox.showinfo('END OF GAME','CONGRATULATIONS!\nYour total score is: {}'.format(woohoo))
        window.destroy()
    
# checking action against move count
def move_check():  
    global move_count  
    global button 
 
    move_count-=1  
    button.config(state = DISABLED) 
    posi_check()

    # roll dice button disabled when move count != 0
    if move_count != 0: 
        button.config(state = DISABLED) 

    # when move count = 0, generates a question
    else: 
        teehee = qn_random()
        q.remove(teehee)
        new_window(teehee)

# Create randomization for the questions given
def qn_random():
    global q
    y = random.choice(q)
    return y

# pop-up window for questions
def new_window(x):
    toplevel = Toplevel(window, bg="skyblue")  # create toplevel window
    toplevel.title(x[0])

    # create randomization for the positions
    def position_random():
        list_of_positions = [0, 1, 2, 3]
        random_list = random.sample(list_of_positions, k=len(list_of_positions))
        return random_list
    randomized_alist = position_random()

    # Create Image Frame widget
    image_frame = Frame(toplevel, width=800, height=400)
    image_frame.grid(row=0, column=0, padx=10, pady=10)

    # Load image to be "edited"
    image = PhotoImage(file="peekaboo.png")
    original_image = image.subsample(1,1) # resize image using subsample
    Label(image_frame, image=original_image).grid(row=0, column=0, padx=0, pady=0)


    # Create Question Frame widget
    questions_frame = Frame(toplevel, width=800, height=100)
    questions_frame.grid(row=1, column=0, padx=10, pady=10)

    # Create Questions above the tool_bar
    Label(questions_frame, font=("Helvetica", 18), text= x[1]).grid(row=1, column=0, padx=5, pady=5)

    # messaage box for correct answer
    def correct():
        MsgBox = messagebox.showinfo('Correct', 'Good Job!')
        toplevel.destroy()
        button.config(state = ACTIVE)

    # messaage box for wrong answer
    def wrong():
        MsgBox = messagebox.showinfo('Wrong', "Correct answer is: {}\nBetter luck next time!".format(x[2]), icon = 'error')
        global woohoo
        woohoo += 5 
        total_numbers.config(text=f'Total Score: {woohoo}') 
        toplevel.destroy()
        button.config(state = ACTIVE)

     # Create Answers Frame widget
    answers_frame = Frame(toplevel, width=800, height=200)
    answers_frame.grid(row=3, column=0, padx=10, pady=10)

    # Create Answer Buttons 1 widget
    answer_button1 = Button(answers_frame, text= x[2], width=100, command = correct)
    answer_button1.grid(row=randomized_alist[0],  padx=0, pady=5)
    
    # Create Answer Buttons 2 widget
    answer_button2 = Button(answers_frame, text= x[3], width=100, command = wrong)
    answer_button2.grid(row=randomized_alist[1], padx=0, pady=5)
    
    # Create Answer Buttons 3 widget
    answer_button3 = Button(answers_frame, text= x[4],  width=100, command = wrong)
    answer_button3.grid(row=randomized_alist[2], padx=0, pady=5)
    
    # Create Answer Buttons 4 widget
    answer_button4= Button(answers_frame, text= x[5], width=100, command = wrong)
    answer_button4.grid(row=randomized_alist[3], padx=0, pady=5)
    
    # trigger 'height' error for image to appear
    answer_button3 = Button(answers_frame, text="4", height =5, width=50, command = toplevel.destroy)
    answer_button3.grid(row=1, column=1, padx=0, pady=0)

##perhaps display rules at the side?
window.mainloop()



