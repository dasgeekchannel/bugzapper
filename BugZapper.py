# BugZapper is a proof of concept project for bug reporting
# Made for Pop!_OS but meant to be forked and modified
# Created by DasGeek (Destination Linux Network)
#!/usr/bin/python

import os
from tkinter import * #import GUI tool tkinter
from tkinter import scrolledtext #import scrolled text module
# setup windows
window = Tk() #create Window
window.title("Welcome to BugZapper") #title of window
window.geometry('400x450') # set window size for application
# labels for window
lbl = Label(window, text="Bug Reporting Application\n Thank you for taking the time to fill this out!", font=("Arial Bold", 12))
lbl.grid(column=0, row=0) # without defining the grid size text in lbl won't show
lbl1 = Label(window, text="System Reports help narrow down the issue. Please choose one.")
lbl1.grid(column=0, row=1)
#Generate Report Buttons
def clicked(): #defining action of command clicked for btnfullsys below
    myCmd = 'ls -la > systemreport.txt' # define command and output result to a file named systemreport.txt/ testing with ls
    os.system(myCmd) #send command to shell
    btnfullsys.configure(text="Report Generated!") #message once clicked
btnfullsys = Button(window, text="Include Full System Report (Best)", bg="orange", fg="red", command = clicked)
btnfullsys.grid(column=0, row = 4)
btnstart = Button(window, text="Include Startup Report Only (Specific)", bg = "orange", fg="green") #creates a button with text
btnstart.grid(column=0, row=5) #positions button within window
btnGPU = Button(window, text="Include Hardware Report Only (Specific)", bg = "orange", fg="green") #creates a button with text
btnGPU.grid(column=0, row=6, padx=0, pady=0) #positions button within window
# Text Entry
lbltxt1 = Label(window, padx=0, pady=10, text="Problem Description: ")
lbltxt1.grid(column=0, row=13)
txt1 = scrolledtext.ScrolledText(window,width=40,height=15, bg = "white smoke")
txt1.grid(column=0, row=14, padx=0, pady=10)
txt1.insert(INSERT,'Enter Steps To Recreate Issue Here: \n \n \n \nDoes the issue happen everytime\nor infrequently?: \n \n \n \nWhat error messages do you receive?: \n ')


# Keep Window Open Loop
window.mainloop() #endless loop of window until we close it