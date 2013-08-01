'''
Created: Apr 13, 2013
Project: Battleship (Python version)
Purpose: Hacker School application
@author: Amy Roberts
contact: aroberts@live.unc.edu
'''

"""
*************************************
Setting up the game
*************************************
"""

#import needed for game
from random import randint

#create the board 
board = []
for x in range(0, 5):
    board.append(["O"] * 5)

#print the board
def print_board(board):
    letter = ["A", "B", "C", "D", "E"]
    print "-------------"
    print "   1 2 3 4 5"
    print "-------------"
    for i, row in zip(letter, board):
        print ( i + "| " + " ".join(row))
    print "-------------"
    print " "

#convert user's guess into format needed for scoring
def convert_guess_row(old):
    old = old.upper()
    new = 99
    if old == "A":
        new = 0
    elif old == "B":
        new = 1
    elif old == "C":
        new = 2
    elif old == "D": 
        new = 3
    elif old == "E":
        new = 4
    else: 
        print "Please enter a letter A, B, C, D, or E"
    return new

def convert_guess_col(old):
    new = int(old) -1
    return new

# reverse scoring back to original form
def revert_guess_row(old):
    new = ""
    if old == 0:
        new = "A"
    elif old == 1:
        new = "B"
    elif old == 2:
        new = "C"
    elif old == 3: 
        new ="D"
    elif old == 4:
        new = "E"
    else:
        pass
    return new

def revert_guess_col(old):
    new = old +1
    return new

#make and hide the ships!
def random_row(board):
    return randint(0, len(board) - 1)
def random_col(board):
    return randint(0, len(board[0]) - 1)
ship_row = random_row(board)
ship_col = random_col(board)

ship2_row = ship_row
ship2_col = ship_col

    
while ship2_row == ship_row and ship2_col == ship_col: #to prevent ships overlapping
    ship2_row = random_row(board)
    ship2_col = random_col(board)


#for reporting the final answer to the player
c_ship_row = revert_guess_row(ship_row)
c_ship_col = revert_guess_col(ship_col)
c_ship2_row = revert_guess_row(ship2_row)
c_ship2_col = revert_guess_col(ship2_col)

"""
#use for debugging/ hide for game
print ("These answers should only be shown for debugging")
print ("ship 1 is on row: " + str(ship_row))
print ("ship 1 is on column: " + str(ship_col))
print ("this is displayed as row %s and column %d" %(c_ship_row, c_ship_col))


print ("ship 2 is on row: " + str(ship2_row))
print ("ship 2 is on column: " + str(ship2_col))
print ("this is displayed as row %s and column %d" %(c_ship2_row, c_ship2_col))
"""

count = 0 #ship count 


"""
*************************************
Begin the game!
*************************************
"""
print " "
print " "
print "Welcome to Battleship!"
print "You will have 10 chances to find 2 ships"
print " "
print "----------------------------------------------------------------------------------"
print "Directions:"
print "Please enter a letter (A,B,C,D,E) for the row and a number (1-5) for the column" 
print "Correct guesses will be marked with an S."
print "Incorrect guesses will be marked with an X."
print "----------------------------------------------------------------------------------"
print " "
print "Let's play Battleship!"
print " "

print_board(board) 
#user enters their guess
for turn in range(10):
    row_alpha = raw_input("Guess a letter:")
    #check that the input is valid
    if row_alpha.isalpha() == True: 
        pass
    else: 
        print "Sorry that response is not allowed. Please enter a letter A, B, C, D, or E"  
        row_alpha = raw_input("Guess a letter:")
        
    col_num = raw_input ("Guess a number:")
    
    try: 
        int(col_num)
    except:
        print "Sorry that response is not allowed. Please enter a number 1-5."
        col_num = raw_input ("Guess a number:")

    guess_col = convert_guess_col(col_num)
    guess_row = convert_guess_row(row_alpha)
            
#game options win/lose/incorrect input
    if ((guess_col == ship_col and guess_row == ship_row) or (guess_col == ship2_col and guess_row == ship2_row)) and count > 0  and board[guess_row][guess_col] != "S" :
        print "Congratulations! You sank both battleships!"
        board[guess_row][guess_col] = "S"
        break
    
    elif ((guess_col == ship_col and guess_row == ship_row) or (guess_col == ship2_col and guess_row == ship2_row)) and count <2:
        print "Great Job! You sank a battleship! One more to go"
        print " "
        board[guess_row][guess_col] = "S"
        count += 1
    else:
        if guess_col > (len(board)-1) or guess_row > (len(board)-1) or guess_col < 0 or guess_row < 0:
            print "Oops, that's out of range."
            print " "
        elif board[guess_row][guess_col] == "X" or board[guess_row][guess_col] == "S":
            print "You guessed that one already. Try again"
            print " "
        else:
            print "You missed my battleship!"
            print " "
            board[guess_row][guess_col] = "X"

#ending the game
    if turn == 9:
        print "Game Over"
        print ("The first ship was in row %s and column %d" % (c_ship_row,c_ship_col))
        print ("The second ship was in row %s and column %d" % (c_ship2_row,c_ship2_col))
    else: 
        print ("You are on turn %s of 10" %(turn+2)) #keeps track of turns 
        print_board(board)
