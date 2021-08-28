from tkinter import *
from PIL import Image, ImageTk
from random import randint

root1 = Tk()
root1.title("Rock Scissor Paper")
root1.configure(background="#9b59b6")

rock_img = ImageTk.PhotoImage(Image.open("rock1.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper1.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissoruser.jpg"))
scissor_img1 = ImageTk.PhotoImage(Image.open("scissor1.png"))

#indicator  to point 
user_indicator = Label(root1, font=50, text="USER", bg="#9b59b6", fg="white")
comp_indicator = Label(root1, font=50, text="COMPUTER",
                       bg="#9b59b6", fg="white")
user_indicator.grid(row=0, column=3)
comp_indicator.grid(row=0, column=1)

#scissor
user_label = Label(root1, image=scissor_img, bg="#9b59b6")
comp_label = Label(root1, image=scissor_img1, bg="#9b59b6")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

choices = ["rock", "paper", "scissor"]




# scores
playerScore = Label(root1, text=0, font=100, bg="#9b59b6", fg="white")
computerScore = Label(root1, text=0, font=100, bg="#9b59b6", fg="white")
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)
  
# update user score
def updateUserScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)

# update computer score
def updateCompScore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)
 # check winner

msg = Label(root1, font=50, bg="#9b59b6", fg="white")
msg.grid(row=3, column=2)

def updateMessage(x):
    msg['text'] = x

def checkWin(player, computer):
    if player == computer:
        updateMessage("Its a tie!!!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()

    else:
        pass
def updateChoice(x):

    # for computer
    compChoice = choices[randint(0, 2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img)
    else:
        comp_label.configure(image=scissor_img1)


# for user
    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)
    checkWin(x, compChoice)

# CREATING BUTTONS FOR USER TO CHOSE ANY OPTION
rock = Button(root1, width=20, height=2, text="ROCK",
              bg="#FF3E4D", fg="white", command=lambda: updateChoice("rock")).grid(row=2, column=1)
paper = Button(root1, width=20, height=2, text="PAPER",
               bg="#FAD02E", fg="white", command=lambda: updateChoice("paper")).grid(row=2, column=2)
scissor = Button(root1, width=20, height=2, text="SCISSOR",
                 bg="#0ABDE3", fg="white", command=lambda: updateChoice("scissor")) .grid(row=2, column=3)

root1.mainloop()