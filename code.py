# Kanishk Jain
# LED Toggle On/Off Code
# Task 5.2C
# SIT 210 - Embedded Systems Development

from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

red = LED(14)
green = LED(15)
blue = LED(18)

# writing code needs to create the main window of the application creating main window object named gui
gui = Tk()

# giving title to the main window
gui.title("LED On/Off")

# Open window having dimension 400x400
gui.geometry('240x400')

#to set the background colour of the gui
gui.configure(bg='#856ff8')

# Defining a font to use it for the button text (optional)
buttonFont = tkinter.font.Font(family="Helvetica", size= 12, weight="bold")
HeaderFont = tkinter.font.Font(family="Helvetica", size= 24, weight="bold")

# empty label to get a margin at the top
header1= Label(gui)
header1.grid(row=0, column= 0)

#Label to show the header text  
header= Label(gui, text ="LED TOGGLER", font= HeaderFont, bg='white')
header.grid(row=1, column= 0)

#--------------RED Button-----------#
def red_led():    #function to toggle the red led
    if red.is_lit:
        red.off()
    else:
        red.on()
        green.off()
        blue.off()

red_button = Button(gui, text='RED', font= buttonFont, command= red_led, bg= 'red', height= 3, width= 15)
red_button.grid(row= 2, column=0)

#--------------GREEN Button-----------#
def green_led():    #function to toggle the green led
    if green.is_lit:
        green.off()
    else:
        green.on()
        red.off()
        blue.off()

green_button = Button(gui, text='GREEN', font= buttonFont, command= green_led, bg= 'green', height= 3, width= 15)
green_button.grid(row=3, column=0)

#--------------BLUE Button-----------#
def blue_led():    #function to toggle the blue led
    if blue.is_lit:
        blue.off()
    else:
        blue.on()
        green.off()
        red.off()

blue_button = Button(gui, text='BLUE', font= buttonFont, command= blue_led, bg= 'blue', height= 3, width= 15)
blue_button.grid(row=4, column=0)

# ------------Exit Button------------#
def close_window():    # funciton to performt the gpio.cleanup as well as close the gui window
    GPIO.cleanup()
    gui.destroy()


exit_button = Button(gui, text='EXIT', command=close_window, bg= 'grey', height= 1, width=9)
# Set the position of button on the bottom 
exit_button.grid(row=5, column=0)

# Syntax to perform the same function as exit button if the close window button on navigation bar is pressed
gui.protocol("WM_DELETE_WINDOW", close_window)


# calling mainloop method which is used
# when your application is ready to run
# and it tells the code to keep displaying
gui.mainloop()


