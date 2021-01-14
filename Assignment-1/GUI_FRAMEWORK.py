from tkinter import *

root = Tk()



titleLabel = Label(root, text="~~~Welcome to Blackjack!~~~")
startButton = Button(root, text="Start", padx=50, command=play)
rulesButton = Button(root, text="Rules", padx=50, command=rules)
quitButton = Button(root, text="Quit", padx=50, command=end)

def play():
    print("play")

def rules():
    print("rules")

def end():
    print("end")
    
titleLabel.grid(row=0, column=0)
startButton.grid(row=1, column=0)
rulesButton.grid(row=2, column=0)
quitButton.grid(row=3, column=0)

root.mainloop