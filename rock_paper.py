# imports
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import random


win = Tk()
win.configure(bg="#FFD8A9")
win.geometry("1800x1824")

# function 
def game(player_chose):
    global img_label
    global player_score , computer_score ,label_status
    label_status=Label(win)
    
    VS_lab = Label(win,text="VS",font=("Times New Roman",40),fg="#C1AEFC",bg="#FFD8A9")
    VS_lab.place(x=640,y=300)

    rock_paper_scissors = ["rock","paper","scissors"]
    computer_chose = random.choice(rock_paper_scissors)
    
    # player chose placing
    
    if player_chose == "rock":
        img_label =Label(win,image=my_img4,bg="#FFD8A9")
        img_label.place(x=350,y=250)
    elif player_chose == 'paper':
        img_label =Label(win,image=my_img2,bg="#FFD8A9")
        img_label.place(x=350,y=250)
    else:
        img_label =Label(win,image=my_img3,bg="#FFD8A9")
        img_label.place(x=350,y=250)
        
    # computer chose placing
    if computer_chose == "rock":
        img_label =Label(win,image=my_img4,bg="#FFD8A9")
        img_label.place(x=850,y=250)
    elif computer_chose == 'paper':
        img_label =Label(win,image=my_img2,bg="#FFD8A9")
        img_label.place(x=850,y=250)
    else:
        img_label =Label(win,image=my_img3,bg="#FFD8A9")
        img_label.place(x=850,y=250)
        
    # win conditions
    if player_chose == "rock" and computer_chose == "scissors" :
        label_status.destroy()
        player_score += 1
        player_score_lab = Label(win,text=f'Your Score : {player_score}',font=("Times New Roman",25),fg="#C1AEFC",bg="#FFD8A9")
        player_score_lab.place(x=17,y=300)
        label_status=Label(win,text="You Won",fg="#C1AEFC",bg="#FFD8A9",font=("Times New Roman",35))
        label_status.place(x=532,y=100)
        
    elif player_chose == "paper" and computer_chose == "rock" :
        label_status.destroy()
        player_score += 1
        player_score_lab = Label(win,text=f'Your Score : {player_score}',font=("Times New Roman",25),fg="#C1AEFC",bg="#FFD8A9")
        player_score_lab.place(x=17,y=300)
        label_status=Label(win,text=" You Won",fg="#C1AEFC",bg="#FFD8A9",font=("Times New Roman",35))
        label_status.place(x=532,y=100)
        
    elif player_chose == "scissors" and computer_chose == "paper" :
        label_status.destroy()
        player_score += 1 
        player_score_lab = Label(win,text=f'Your Score : {player_score}',font=("Times New Roman",25),fg="#C1AEFC",bg="#FFD8A9")
        player_score_lab.place(x=17,y=300)
        label_status=Label(win,text=" You Won",fg="#C1AEFC",bg="#FFD8A9",font=("Times New Roman",35))
        label_status.place(x=532,y=100)
        
    elif player_chose == computer_chose :
        label_status.destroy()
        label_status=Label(win,text="     TIE",fg="#C1AEFC",bg="#FFD8A9",font=("Times New Roman",36),width=9)
        label_status.place(x=530,y=100)
    else:
        computer_score+=1
        computer_score_lab = Label(win,text=f'computer Score : {computer_score}',font=("Times New Roman",25),fg="#C1AEFC",bg="#FFD8A9")
        label_status.destroy()
        computer_score_lab.place(x=1095,y=300)
        label_status=Label(win,text="You lost",fg="#C1AEFC",bg="#FFD8A9",font=("Times New Roman",34),width=9)
        label_status.place(x=530,y=100)

        
        

    
        
    

# img 
my_img = ImageTk.PhotoImage(Image.open(r'images/rock-paper-scissors (5).png'))
my_img2 = ImageTk.PhotoImage(Image.open(r'images/stop (1).png'))
my_img3 = ImageTk.PhotoImage(Image.open(r'images/two-fingers (1).png'))
my_img4 = ImageTk.PhotoImage(Image.open(r'images/fist (1).png'))

# titles
label_titel = Label(win,image=my_img,border=0,bg="#FFD8A9")
label_titel.place(x=0,y=0)

label_titel2 = Label(win,text="Rock Paper Scissors",border=0,font=("Times New Roman",35),bg="#FFD8A9")
label_titel2.place(x=510,y=0)

label_titel3 = Label(win,image=my_img,border=0,bg="#FFD8A9")
label_titel3.place(x=1100,y=0)

# placing ....
but_rock = Button(win,border=0,image=my_img4,bg="#FFD8A9",activebackground='#F6F7C1',command=lambda:game("rock"))
but_rock.place(x=225,y=530)

but_paper = Button(win,border=0,image=my_img2,bg="#FFD8A9",activebackground='#F6F7C1',command=lambda:game("paper"))
but_paper.place(x=625,y=530)

but_sciss = Button(win,border=0,image=my_img3,bg="#FFD8A9",activebackground='#F6F7C1',command=lambda:game("scissors"))
but_sciss.place(x=1025,y=530)

# scores
player_score = 0
computer_score = 0

# placing scores
player_score_lab = Label(win,text=f'Your Score : {player_score}',font=("Times New Roman",25),fg="#C1AEFC",bg="#FFD8A9")
player_score_lab.place(x=17,y=300)

computer_score_lab = Label(win,text=f'computer Score : {computer_score}',font=("Times New Roman",25),fg="#C1AEFC",bg="#FFD8A9")
computer_score_lab.place(x=1095,y=300)




win.mainloop()