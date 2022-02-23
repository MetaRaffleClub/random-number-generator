import csv
import time
import random
from numpy import size
import pandas as pd
from random import choice
from tkinter import *
from tkinter import ttk

def rand_gen():
    data = pd.read_csv("general_winners_list.csv")
    winners = data["Winners"].values.tolist()

    rand_number = choice(list(set([x for x in range(1, 10001)]) - set(winners)))
    rand_number = [rand_number]

    with open("general_winners_list.csv",'a') as write:
        writer = csv.writer(write)
        writer.writerow(rand_number)
        
    return rand_number

def firework(UI, DIRECTION, ANCHOR_POINT):
    WIDTH = 1000
    HEIGHT = 500
    canvas = Canvas(master = UI, width= WIDTH, height= HEIGHT, bg="gray")    
    canvas.pack(side=DIRECTION, anchor=ANCHOR_POINT)
    def circle(w, x, y, r,col):
        id = w.create_oval(x-r,y-r,x+r,y+r,fill=col, tag="circle")
        return id

    class Particle:
        def __init__(self,x,y):
            self.shape = circle(canvas, x,y,random.random()*2,"white")
            self.xvel=random.random()*3-1.5
            self.yvel=-2+random.random()*2
            self.count=0
            
        def move(self):
            canvas.move(self.shape,self.xvel,self.yvel)
            self.yvel += yacc
            self.count +=1
            
    class Ball:
        def __init__(self,size):
            #col=('#%02X%02X%02X' % (r(),r(),r()))
            self.shape = circle(canvas, random.random()*(WIDTH-2*size)*0.5+WIDTH*0.25+size, HEIGHT-size, size,"gray")
            self.xvel = (random.random()*2-1)
            self.yvel = (-10+random.random()*4)
            self.explode=0
            
        def move(self):
            canvas.move(self.shape, self.xvel, self.yvel)
            pos=canvas.coords(self.shape)
            if pos[3] >= HEIGHT or pos[1] <=0:
                canvas.move(self.shape, 0, -self.yvel)
                col=('#%02X%02X%02X' % (r(),r(),r()))
                canvas.itemconfig(self.shape, fill=col)
                self.yvel=-self.yvel  #*0.9
            if pos[2] >= WIDTH or pos[0] <=0:
                canvas.move(self.shape, -self.xvel, 0)
                col=('#%02X%02X%02X' % (r(),r(),r()))
                canvas.itemconfig(self.shape, fill=col)
                self.xvel=-self.xvel  #*0.9
            self.yvel += yacc
            if self.explode==1:
                self.explode=0
            if (self.yvel>=0) and (self.yvel-yacc<0):
                self.explode=1 

    yacc=0.125
    balls = []
    particles = []
    r = lambda: random.randint(40,255)
            
    for i in range(5):
        balls.append(Ball(random.random()*2+2))

    while True:
        ddel = -1
        pdel = -1
        canvas.config(bg="black")
        for i, ball in enumerate(balls):
            ball.move()
            if ball.explode:
                canvas.config(bg="gray")
                posx=(canvas.coords(ball.shape)[0]+canvas.coords(ball.shape)[2])*0.5
                posy=(canvas.coords(ball.shape)[1]+canvas.coords(ball.shape)[3])*0.5
                ddel = i
                for j in range(20):
                    particles.append(Particle(posx,posy))
        for i, particle in enumerate(particles):
            particle.move()
            if particle.count>=20:
                pdel = i
        if ddel != -1:
            canvas.delete(balls[ddel].shape)
            del balls[ddel]
            ddel = -1
            balls.append(Ball(random.random()*2+2))
        if pdel != -1:
            canvas.delete(particles[pdel].shape)
            del particles[pdel]
            pdel = -1
        
        
        UI.update()
        time.sleep(0.04)

def main():
    ui = Tk()
    ui.geometry("1920x1080")
    ui.title("META RAFFLE CLUB PRESENTS:")  

    label_1 = Label(ui, text = "META RAFFLE CLUB PRESENTS", font=("Arial Black",60))
    label_1.pack(side=TOP, anchor=CENTER, padx=10, pady=200)
    label_2 = Label(ui, text = "THIS WEEK'S RAFFLE", font=("Arial Black",60))
    label_2.pack(side=TOP, anchor=CENTER, padx=10, pady=0)

    def nextPage1():
        ui.destroy()
        pg1()

    next_button = Button(ui,text="NEXT", command = nextPage1, font=("Arial",50))
    next_button.pack(side=BOTTOM, anchor=CENTER)

    ui.mainloop()

def pg1():
    ui = Tk()
    ui.geometry("1920x1080")
    ui.title("META RAFFLE CLUB PRESENTS:")
    progress_bar = ttk.Progressbar(ui, orient=HORIZONTAL, length=1000, mode="determinate")

    def progressbar():
        progress_bar.grid(row=4, column=1,columnspan=8)
        for x in range(5):
            progress_bar['value']+=20
            ui.update_idletasks()
            time.sleep(0.5)
        progress_bar.destroy()
        conso_looping()

    def conso_looping():
        for x in range(5,10):
            for y in range(1,9):
                conso_winner = Label(ui, text = rand_gen(), bd=5, relief="solid", font=("Arial",30), width=4, height=2)
                conso_winner.grid(row=x, column=y, padx=39, pady=15) 
        for z in range(1,8):
            conso_winner = Label(ui, text = rand_gen(), bd=5, relief="solid", font=("Arial",30), width=4, height=2)
            conso_winner.grid(row=11, column=z, padx=39, pady=15) 

        next_button = Button(ui,text="NEXT", command = nextPage2, font=("Arial",50))
        next_button.grid(row=11, column=8)

    def button_disable():
        winner_button['command'] = progressbar()
        winner_button['text'] = "CONGRATULATIONS!!"
        winner_button['command'] = 0

    def nextPage2():
        ui.destroy()
        pg2()

    #configure gui grids
    rows = 0 
    while rows < 8:
        ui.rowconfigure(rows, weight=1)
        ui.columnconfigure(rows,weight=1)
        rows += 1
    title_label = Label(ui, text = "CONSOLATION PRIZE WINNERS", font=("Arial Black",60))
    title_label.grid(row=0, column=1, columnspan=8)
    winner_button = Button(ui,text="PICK YOUR WINNERS!", command = button_disable, font=("Arial",50))
    winner_button.grid(row=2, column=1, columnspan=8)

    ui.mainloop()

def pg2():
    ui = Tk()
    ui.geometry("1920x1080")
    ui.title("META RAFFLE CLUB PRESENTS:")
    progress_bar = ttk.Progressbar(ui, orient=HORIZONTAL, length=1000, mode="determinate")

    def progressbar():
        progress_bar.pack(pady=80, side=TOP, anchor = CENTER)
        for x in range(5):
            progress_bar['value']+=20
            ui.update_idletasks()
            time.sleep(1)
        progress_bar.destroy()
        winners()

    def winners():
        winner = Label(ui, text = rand_gen(), bd=8, relief="solid", font=("Arial",80), width=5, height=2)
        winner.pack(pady=80, side=TOP, anchor = CENTER)
        message = Label(ui, text = "CONGRATS! THIS LUCKY OWNER WON 0.2 ETH", font=("Arial",40))
        message.pack(pady=50, side=TOP, anchor = CENTER) 
        next_button = Button(ui,text="NEXT", command = nextPage3, font=("Arial",50))
        next_button.pack(side=RIGHT, anchor=SE)
    
    def button_disable():
        winner_button['command'] = progressbar()
        winner_button['text'] = "CONGRATULATIONS!!"
        winner_button['command'] = 0

    def nextPage3():
        ui.destroy()
        pg3()

    title_label = Label(ui, text = "THE THIRD PRIZE WINNER IS:", font=("Arial Black",60))
    title_label.pack(side=TOP, anchor=N, padx=10, pady=10)
    winner_button = Button(ui,text="PICK YOUR WINNERS!", command = button_disable, font=("Arial",50))
    winner_button.pack(side=TOP, anchor=N, pady=20)

    ui.mainloop()

def pg3():
    ui = Tk()
    ui.geometry("1920x1080")
    ui.title("META RAFFLE CLUB PRESENTS:")
    progress_bar = ttk.Progressbar(ui, orient=HORIZONTAL, length=1000, mode="determinate")

    def progressbar():
        progress_bar.pack(pady=80, side=TOP, anchor = CENTER)
        for x in range(5):
            progress_bar['value']+=20
            ui.update_idletasks()
            time.sleep(1)
        progress_bar.destroy()
        winners()

    def winners():
        winner = Label(ui, text = rand_gen(), bd=8, relief="solid", font=("Arial",80), width=5, height=2)
        winner.pack(pady=80, side=TOP, anchor = CENTER) 
        message = Label(ui, text = "CONGRATS! THIS LUCKY OWNER WON 0.5 ETH", font=("Arial",40))
        message.pack(pady=50, side=TOP, anchor = CENTER)
        next_button = Button(ui,text="NEXT", command = nextPage4, font=("Arial",50))
        next_button.pack(side=RIGHT, anchor=SE)

    def button_disable():
        winner_button['command'] = progressbar()
        winner_button['text'] = "CONGRATULATIONS!!"
        winner_button['command'] = 0

    def nextPage4():
        ui.destroy()
        pg4()
 
    title_label = Label(ui, text = "THE SECOND PRIZE WINNER IS:", font=("Arial Black",60))
    title_label.pack(side=TOP, anchor=N, padx=10, pady=10)
    winner_button = Button(ui,text="PICK YOUR WINNERS!", command = button_disable, font=("Arial",50))
    winner_button.pack(side=TOP, anchor=N, pady=20)

    ui.mainloop()

def pg4():
    ui = Tk()
    ui.geometry("1920x1080")
    ui.title("META RAFFLE CLUB PRESENTS:")
    progress_bar = ttk.Progressbar(ui, orient=HORIZONTAL, length=1000, mode="determinate")

    def progressbar():
        progress_bar.pack(pady=80, side=TOP, anchor = CENTER)
        for x in range(5):
            progress_bar['value']+=20
            ui.update_idletasks()
            time.sleep(1.5)
        progress_bar.destroy()
        winners()

    def winners():
        winner = Label(ui, text = rand_gen(), bd=8, relief="solid", font=("Arial",80), width=5, height=2)
        winner.pack(pady=80, side=TOP, anchor = CENTER)
        message = Label(ui, text = "CONGRATS! THIS LUCKY OWNER WON 1 ETH", font=("Arial",40))
        message.pack(pady=50, side=TOP, anchor = CENTER) 
        next_button = Button(ui,text="NEXT", command = nextPage, font=("Arial",50))
        next_button.pack(side=RIGHT, anchor=SE)
        
    def button_disable():
        winner_button['command'] = progressbar()
        winner_button['text'] = "CONGRATULATIONS!!"
        winner_button['command'] = 0

    def nextPage():
        ui.destroy()
        pg5()
 
    title_label = Label(ui, text = "THE FIRST PRIZE WINNER IS:", font=("Arial Black",60))
    title_label.pack(side=TOP, anchor=N, padx=10, pady=10)
    winner_button = Button(ui,text="PICK YOUR WINNERS!", command = button_disable, font=("Arial",50))
    winner_button.pack(side=TOP, anchor=N, pady=20)

    ui.mainloop()

def pg5():
    ui = Tk()
    ui.geometry("1920x1080")
    ui.title("META RAFFLE CLUB PRESENTS:")
    message_1 = Label(ui, text = "CONGRATULATIONS ALL WINNERS!", font=("Arial Black",60))
    message_1.pack(anchor=CENTER, padx=10, pady=10)
    message_2 = Label(ui, text = "MAY YOU 'DE-FI' THE ODDS NEXT WEEK", font=("Arial Black",60))
    message_2.pack(anchor=CENTER, padx=10, pady=10)
    firework(ui, TOP, CENTER)

main()