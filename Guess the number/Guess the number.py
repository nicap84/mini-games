# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

#import simplegui
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random


# initialize global variables used in your code
num_range=100

aleatorio=0
inp_number=0
count=7

# helper function to start and restart the game
def new_game():
    global aleatorio
    aleatorio=random.randrange(0,num_range)
       

# define event handlers for control panel
def range100():
    global num_range
    num_range=100
    global count
    count=7
    new_game()
    print "New game. Range is from 0 to " +str (num_range)
    print "Number if remaining guesses is " + str(count)
    print ""
    
def range1000():
    global num_range
    num_range=1000
    global count
    count=10
    new_game()
    print "New game. Range is from 0 to 1000"
    print "Number if remaining guesses is " + str(count)
    print ""
    
def input_guess(guess):
    global inp_number
    inp_number=int(guess)
    global count 
    count=count-1
    print "Guess was " + str(inp_number)
    print "Number of remaining guesses is " + str(count)
    if count>0:
        if inp_number < aleatorio:
            print "Higher!"
            print ""
        elif inp_number >aleatorio:   
            print "Lower!"
            print ""
        elif inp_number == aleatorio:
            print "Correct!"
            print ""  
            if num_range==100:
                range100()    
            else:
                range1000()
    elif count<=0:
         print "You ran out of guesses.  The number was " + str(aleatorio)
         print ""
         if num_range==100:
            range100()    
         else:
            range1000()
    
# create frame
frame=simplegui.create_frame ("Guess the number",200,200)


# register event handlers for control elements
frame.add_button ("Range is [0,100)", range100, 200)
frame.add_button ("Range is [0,1000)",range1000, 200)
frame.add_input ("Enter a guess", input_guess, 200)


range100()
frame.start()


# always remember to check your completed program against the grading rubric