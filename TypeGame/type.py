from tkinter import *
import random
import tkinter.messagebox as tsmg
miss=0
timeleft = 15
scr=0

wordList = ['hat', 'river', 'statue', 'generate', 'Hello', 'Cocktail', 'add', 'answer', 'blame']

def exitGame():
    exit(0)

def restartGame():
    global scr, miss, timeleft
    str.set('')
    scr=0
    timeleft=15
    miss=0
    scoreCount.configure(text=scr)
    missCount.configure(text=miss)
    timeCount.configure(text=timeleft)
    b=random.choice(wordList)
    random.shuffle(wordList)
    words['text']=b
    status.configure(text='')

def startTimer():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        timeCount.configure(text=timeleft)
        timeCount.after(1000,startTimer)
    elif timeleft == 0:
        status.configure(text="Gave Over!!!")
        r = tsmg.showinfo("Noteification","Game Over!!!")
        if r == 'ok':
            restartGame()

def Gamelogic(event):
    global scr, miss
    if timeleft == 15:
        startTimer()
    if str.get() == word['text']:
        scr += 1
        scoreCount.configure(text=scr)
    else:
        miss += 1
        missCount.configure(text=miss)
    random.shuffle(wordList)
    b=random.choice(wordList)
    word['text']=b
    Inputword.delete(0,END)

root = Tk()
root.title('Typing Speed Game')
root.geometry("800x600+250+50")
root.iconbitmap('games_folder_file_10467.ico')
root.resizable(False,False)
root.configure(background="black")

f1 = Frame(root,height=50,width=600)
l1 = Label(f1,text="Typing Speed Game", font="comicsansms 50 italic bold", bg = "black", fg='white')
l1.pack()
f1.pack(pady=30)

f2 = Frame(root,height=200,width=200)
word = Label(f2,text="Start", font="comicsansms 35 italic bold", bg = "black", fg='white')
word.pack()
f2.pack()

score = Label(root, text="Hit score : " , font="comicsansms 25 italic bold", bg="black", fg="white")
score.place(x=20, y=430)

scoreCount = Label(root, text=scr , font="comicsansms 25 italic bold", bg="black", fg="green")
scoreCount.place(x=90, y=480)

Missscore = Label(root, text="Missing Score" , font="comicsansms 25 italic bold", bg="black", fg="white")
Missscore.place(x=300, y=430)

missCount = Label(root, text=miss , font="comicsansms 25 italic bold", bg="black", fg="green")
missCount.place(x=400, y=480)

status = Label(root, text="" , font="comicsansms 25 italic bold", bg="black", fg="red")
status.place(x=280, y=380)

times = Label(root, text="Time Left : " , font="comicsansms 25 italic bold", bg="black", fg="white")
times.place(x=600, y=430)

timeCount = Label(root, text=timeleft , font="comicsansms 25 italic bold", bg="black", fg="green")
timeCount.place(x=600, y=480)



str = StringVar()
f3 = Frame(root,height = 200, width=600)
Inputword = Entry(f3, textvariable=str,width=30,font="comicsansms 30 italic bold", bg= "black", fg="yellow",justify="center",bd=5)
Inputword.pack()
Inputword.focus_set()
Inputword.configure(insertbackground="white")
f3.pack(pady=30)

restart = Button(root, text="Restart", bg="green",fg="white",font="comicsansms 20 italic bold", padx=30, command=restartGame)
restart.place(x=220,y=310)

pause = Button(root, text="Cancel", bg="green",fg="white",font="comicsansms 20 italic bold", padx=30, command=exitGame)
pause.place(x=420,y=310)

root.bind("<Return>",Gamelogic)
root.mainloop()