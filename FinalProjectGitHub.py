"""
Program: Time Conversion Calculator
Author: Brindley
Purpose: Convert different amounts of time based on a user's input

1. Significant constants
    givenValue is the user's input; this value is a string
    origNum takes the givenValue and "makes" it an integer
    various lengths of time (ie. seconds, minutes)
    text is the string that puts all of the data together in a meaningful sentence
    e is the entry box for the user's input
    branch indicates the second window
    
2. The input is
    amount of time user wishes to convert
    
3. The output is
    amount of time after conversion calculations; essentially, equivalent to the user's input

4. Code used but not inherently in the program
    from resizeimage import resizeimage

    #Opening image file
    my_img2 = ImageTk.PhotoImage(Image.open("Solution_Found.png"))
    #Resizing image and saving resized image **OVER ORIGINAL FILE**
    with Image.open("Solution_Found.png") as image:
        cover = resizeimage.resize_cover(image, [100, 100])
        cover.save("Solution_Found.png", image.format)
    #Creating image label
    my_label = Label(root, image = my_img)
    #Showing image label
    my_label.grid(row = 0, column = 0)
"""

#Importing modules
import tkinter as tk 
from tkinter import *
from PIL import ImageTk, Image


#Creating a window called root through an instance of tkinter (tk)
root = tk.Tk()
#Creating a title for the root window's titlebar
root.title("Conversion Calculator")
#Placing an icon (ie. logo) in the root window's titlebar
root.iconbitmap(r"C:\Users\brind\OneDrive\Desktop\OneDrive brindley.morgan\OneDrive\Documents\Ivy Tech\2021-2022\Intro_to_Software_Development\Final Project\Wonova_logo.ico")

#Creating global variable (ie. "bucket" of objects throughout program)
global givenValue

#Creating function to convert seconds to minutes
def convertSecToMin():
    #Getting user input value from the entry box (e) and assigning it the name givenValue
    givenValue = e.get()
    #Converting user input to an integer and calling it origNum
    origNum = int(givenValue)
    #Calculating the number of minutes by dividing the user input by 60
    minutes = origNum / 60
    #Rounding the previously assigned minutes variable to the nearest hundredths place
    minutes = round(minutes, 2)
    #Clearing the entry box
    e.delete(0, END)
    #Creating a meaningful string from the data and calling it text
    text = str(origNum) + " seconds is " + str(minutes) + " minutes"
    #Creating a second window called branch through the same instance of tkinter (tk)
    branch = tk.Tk()
    #Creating a title for the branch window's titlebar
    branch.title("ANSWER")
    #Placing the same icon (ie. logo) in the branch window's titlebar for continuity
    branch.iconbitmap(r"C:\Users\brind\OneDrive\Desktop\OneDrive brindley.morgan\OneDrive\Documents\Ivy Tech\2021-2022\Intro_to_Software_Development\Final Project\Wonova_logo.ico")
    #Creating an answer label using the text variable
    branch.myLabel3 = Label(branch, text = "Answer: " + text, font = ("Helvetica", 10), padx = 20, pady = 20)
    #Placing the answer label in the branch window
    branch.myLabel3.grid(row = 0, column = 1)
    return None

#Creating function to convert seconds to hours
def convertSecToHr():
    #Getting user input value from the entry box (e) and assigning it the name givenValue
    givenValue = e.get()
    #Converting user input to an integer and calling it origNum
    origNum = int(givenValue)
    #Calculating the number of hours by dividing the user input by 3600
    hours = origNum / 3600
    #Rounding the previously assigned hours variable to the nearest hundredths place
    hours = round(hours, 2)
    #Clearing the entry box
    e.delete(0, END)
    #Creating a meaningful string from the data and calling it text
    text = str(origNum) + " seconds is " + str(hours) + " hours"
    #Creating a second window called branch through the same instance of tkinter (tk)
    branch = tk.Tk()
    #Creating a title for the branch window's titlebar
    branch.title("ANSWER")
    #Placing the same icon (ie. logo) in the branch window's titlebar for continuity
    branch.iconbitmap(r"C:\Users\brind\OneDrive\Desktop\OneDrive brindley.morgan\OneDrive\Documents\Ivy Tech\2021-2022\Intro_to_Software_Development\Final Project\Wonova_logo.ico")
    #Creating an answer label using the text variable
    branch.myLabel3 = Label(branch, text = "Answer: " + text, font = ("Helvetica", 10), padx = 20, pady = 20)
    #Placing the answer label in the branch window
    branch.myLabel3.grid(row = 0, column = 1)
    return None

#Creating function to convert minutes to hours
def convertMinToHr():
    #Getting user input value from the entry box (e) and assigning it the name givenValue
    givenValue = e.get()
    #Converting user input to an integer and calling it origNum
    origNum = int(givenValue)
    #Calculating the number of hours by dividing the user input by 60
    hours = origNum / 60
    #Rounding the previously assigned hours variable to the nearest hundredths place
    hours = round(hours, 2)
    #Clearing the entry box
    e.delete(0, END)
    #Creating a meaningful string from the data and calling it text
    text = str(origNum) + " minutes is " + str(hours) + " hours"
    #Creating a second window called branch through the same instance of tkinter (tk)
    branch = tk.Tk()
    #Creating a title for the branch window's titlebar
    branch.title("ANSWER")
    #Placing the same icon (ie. logo) in the branch window's titlebar for continuity
    branch.iconbitmap(r"C:\Users\brind\OneDrive\Desktop\OneDrive brindley.morgan\OneDrive\Documents\Ivy Tech\2021-2022\Intro_to_Software_Development\Final Project\Wonova_logo.ico")
    #Creating an answer label using the text variable
    branch.myLabel3 = Label(branch, text = "Answer: " + text, font = ("Helvetica", 10), padx = 20, pady = 20)
    #Placing the answer label in the branch window
    branch.myLabel3.grid(row = 0, column = 1)
    return None

#Creating function to convert minutes to days
def convertMinToDay():
    #Getting user input value from the entry box (e) and assigning it the name givenValue
    givenValue = e.get()
    #Converting user input to an integer and calling it origNum
    origNum = int(givenValue)
    #Calculating the number of minutes by dividing the user input by 1440
    days = origNum / 1440
    #Rounding the previously assigned days variable to the nearest hundredths place
    days = round(days, 2)
    #Clearing the entry box
    e.delete(0, END)
    #Creating a meaningful string from the data and calling it text
    text = str(origNum) + " minutes is " + str(days) + " days"
    #Creating a second window called branch through the same instance of tkinter (tk)
    branch = tk.Tk()
    #Creating a title for the branch window's titlebar
    branch.title("ANSWER")
    #Placing the same icon (ie. logo) in the branch window's titlebar for continuity
    branch.iconbitmap(r"C:\Users\brind\OneDrive\Desktop\OneDrive brindley.morgan\OneDrive\Documents\Ivy Tech\2021-2022\Intro_to_Software_Development\Final Project\Wonova_logo.ico")
    #Creating an answer label using the text variable
    branch.myLabel3 = Label(branch, text = "Answer: " + text, font = ("Helvetica", 10), padx = 20, pady = 20)
    #Placing the answer label in the branch window
    branch.myLabel3.grid(row = 0, column = 1)
    return None

#Creating function to convert days to weeks
def convertDayToWeek():
    #Getting user input value from the entry box (e) and assigning it the name givenValue
    givenValue = e.get()
    #Converting user input to an integer and calling it origNum
    origNum = int(givenValue)
    #Calculating the number of weeks by dividing the user input by 7
    weeks = origNum / 7
    #Rounding the previously assigned weeks variable to the nearest hundredths place
    weeks = round(weeks, 2)
    #Clearing the entry box
    e.delete(0, END)
    #Creating a meaningful string from the data and calling it text
    text = str(origNum) + " days is " + str(weeks) + " weeks"
    #Creating a second window called branch through the same instance of tkinter (tk)
    branch = tk.Tk()
    #Creating a title for the branch window's titlebar
    branch.title("ANSWER")
    #Placing the same icon (ie. logo) in the branch window's titlebar for continuity
    branch.iconbitmap(r"C:\Users\brind\OneDrive\Desktop\OneDrive brindley.morgan\OneDrive\Documents\Ivy Tech\2021-2022\Intro_to_Software_Development\Final Project\Wonova_logo.ico")
    #Creating an answer label using the text variable
    branch.myLabel3 = Label(branch, text = "Answer: " + text, font = ("Helvetica", 10), padx = 20, pady = 20)
    #Placing the answer label in the branch window
    branch.myLabel3.grid(row = 0, column = 1)
    return None

#Creating function to convert weeks to months
def convertWeekToMonth():
    #Getting user input value from the entry box (e) and assigning it the name givenValue
    givenValue = e.get()
    #Converting user input to an integer and calling it origNum
    origNum = int(givenValue)
    #Calculating the number of months by dividing the user input by 4
    months = origNum / 4
    #Rounding the previously assigned months variable to the nearest hundredths place
    months = round(months, 2)
    #Clearing the entry box
    e.delete(0, END)
    #Creating a meaningful string from the data and calling it text
    text = str(origNum) + " weeks is " + str(months) + " months"
    #Creating a second window called branch through the same instance of tkinter (tk)
    branch = tk.Tk()
    #Creating a title for the branch window's titlebar
    branch.title("ANSWER")
    #Placing the same icon (ie. logo) in the branch window's titlebar for continuity
    branch.iconbitmap(r"C:\Users\brind\OneDrive\Desktop\OneDrive brindley.morgan\OneDrive\Documents\Ivy Tech\2021-2022\Intro_to_Software_Development\Final Project\Wonova_logo.ico")
    #Creating an answer label using the text variable
    branch.myLabel3 = Label(branch, text = "Answer: " + text, font = ("Helvetica", 10), padx = 20, pady = 20)
    #Placing the answer label in the branch window
    branch.myLabel3.grid(row = 0, column = 1)
    return None

#Creating function to convert weeks to years
def convertWeekToYear():
    #Getting user input value from the entry box (e) and assigning it the name givenValue
    givenValue = e.get()
    #Converting user input to an integer and calling it origNum
    origNum = int(givenValue)
    #Calculating the number of years by dividing the user input by 52
    years = origNum / 52
    #Rounding the previously assigned years variable to the nearest hundredths place
    years = round(years, 2)
    #Clearing the entry box
    e.delete(0, END)
    #Creating a meaningful string from the data and calling it text
    text = str(origNum) + " weeks is " + str(years) + " years"
    #Creating a second window called branch through the same instance of tkinter (tk)
    branch = tk.Tk()
    #Creating a title for the branch window's titlebar
    branch.title("ANSWER")
    #Placing the same icon (ie. logo) in the branch window's titlebar for continuity
    branch.iconbitmap(r"C:\Users\brind\OneDrive\Desktop\OneDrive brindley.morgan\OneDrive\Documents\Ivy Tech\2021-2022\Intro_to_Software_Development\Final Project\Wonova_logo.ico")
    #Creating an answer label using the text variable
    branch.myLabel3 = Label(branch, text = "Answer: " + text, font = ("Helvetica", 10), padx = 20, pady = 20)
    #Placing the answer label in the branch window
    branch.myLabel3.grid(row = 0, column = 1)
    return None


#Creating function to convert months to years
def convertMonthToYear():
    #Getting user input value from the entry box (e) and assigning it the name givenValue
    givenValue = e.get()
    #Converting user input to an integer and calling it origNum
    origNum = int(givenValue)
    #Calculating the number of years by dividing the user input by 12
    years = origNum / 12
    #Rounding the previously assigned years variable to the nearest hundredths place
    years = round(years, 2)
    #Clearing the entry box
    e.delete(0, END)
    #Creating a meaningful string from the data and calling it text
    text = str(origNum) + " months is " + str(years) + " years"
    #Creating a second window called branch through the same instance of tkinter (tk)
    branch = tk.Tk()
    #Creating a title for the branch window's titlebar
    branch.title("ANSWER")
    #Placing the same icon (ie. logo) in the branch window's titlebar for continuity
    branch.iconbitmap(r"C:\Users\brind\OneDrive\Desktop\OneDrive brindley.morgan\OneDrive\Documents\Ivy Tech\2021-2022\Intro_to_Software_Development\Final Project\Wonova_logo.ico")
    #Creating an answer label using the text variable
    branch.myLabel3 = Label(branch, text = "Answer: " + text, font = ("Helvetica", 10), padx = 20, pady = 20)
    #Placing the answer label in the branch window
    branch.myLabel3.grid(row = 0, column = 1)
    return None

##Create first image label
#Opening a png file and calling it my_img
my_img = ImageTk.PhotoImage(Image.open("Calculator.png"))
#Creating the first image label
my_imgLabel = Label(root, image = my_img)
#Showing the first image label
my_imgLabel.grid(row = 0, column = 0)

##Create second image label
#Opening a png file and calling it my_img2
my_img2 = ImageTk.PhotoImage(Image.open("Solution_Found.png"))
#Creating the second image label
my_imgLabel2 = Label(root, image = my_img2)
#Showing the second image label
my_imgLabel2.grid(row = 6, column = 3, rowspan = 8)

#Creating title label
title_label = Label(root, text = "TIME CONVERTER", font = ("Helvetica", 22))
#Showing title label
title_label.grid(row = 0, column = 1, columnspan = 3)

#Creating prompt label for the initial amount of time (user input)
prompt_label = Label(root, text = "Enter the amount of time: ", font = ("Helvetica", 10), padx = 20, pady = 20)
#Showing prompt label for the initial amount of time (user input)
prompt_label.grid(row = 1, column = 0)

#Creating input field for time input (entry box) and calling it e
e = Entry(root, font = ("Calibri", 14))
#Showing field for time input (entry box) and calling it e
e.grid(row = 2, column = 0, rowspan = 2, columnspan = 12)

#Creating second prompt label for user to select a button
myLabel2 = Label(root, text = "Then select which time you would like the number converted to:", font = ("Helvetica", 10), padx = 20, pady = 20)
#Showing second prompt label for user to select a button
myLabel2.grid(row = 4, column = 0, rowspan = 2, columnspan = 3)

#Creating button to convert seconds to minutes
secToMin_button = Button(root, text = "Seconds to minutes", command = convertSecToMin, font = ("Arial Black", 8))
#Showing conversion button in window
secToMin_button.grid(row = 6, column = 0)

#Creating button to convert seconds to hours
secToHr_button = Button(root, text = "Seconds to hours", command = convertSecToHr, font = ("Arial Black", 8))
#Showing conversion button in window
secToHr_button.grid(row = 7, column = 0)

#Creating button to convert minutes to hours
minToHr_button = Button(root, text = "Minutes to hours", command = convertMinToHr, font = ("Arial Black", 8))
#Showing conversion button in window
minToHr_button.grid(row = 8, column = 0)

#Creating button to convert minutes to days
minToDay_button = Button(root, text = "Minutes to days", command = convertMinToDay, font = ("Arial Black", 8))
#Showing conversion button in window
minToDay_button.grid(row = 9, column = 0)

#Creating button to convert days to weeks
dayToWeek_button = Button(root, text = "Days to weeks", command = convertDayToWeek, font = ("Arial Black", 8))
#Showing conversion button in window
dayToWeek_button.grid(row = 6, column = 1)

#Creating button to convert weeks to months
wkToMonth_button = Button(root, text = "Weeks to months", command = convertWeekToMonth, font = ("Arial Black", 8))
#Showing conversion button in window
wkToMonth_button.grid(row = 7, column = 1)

#Creating button to convert weeks to years
wkToYr_button = Button(root, text = "Weeks to years", command = convertWeekToYear, font = ("Arial Black", 8))
#Showing conversion button in window
wkToYr_button.grid(row = 8, column = 1)

#Creating button to convert months to years
monthToYr_button = Button(root, text = "Months to years", command = convertMonthToYear, font = ("Arial Black", 8))
#Showing conversion button in window
monthToYr_button.grid(row = 9, column = 1)


root.mainloop()
