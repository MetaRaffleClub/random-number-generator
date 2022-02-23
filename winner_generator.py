import csv
import time
import random
from numpy import size
import pandas as pd
from random import choice
from tkinter import *
from tkinter import ttk

def rand_gen():
    data_1 = pd.read_csv("general_winners_list.csv")
    general_winners = data_1["Winners"].values.tolist()
    general_winners = set(general_winners)

    data_2 = pd.read_csv("winners_winners_list.csv")
    winners_winners = data_2["Winners"].values.tolist()
    winners_winners = set(winners_winners)

    data_3 = (general_winners.difference(winners_winners)) #removing past winners winners pool from general winners pool

    rand_number = choice(list(set(data_3)))
    rand_number = [rand_number]

    with open("winners_winners_list.csv",'a') as write:
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
    label_2 = Label(ui, text = "WELCOME TO THIS MONTH'S WINNERS' POOL RAFFLE!!!!", font=("Arial Black",45))
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
        message = Label(ui, text = "CONGRATS! THIS LUCKY OWNER WON 1 ETH", font=("Arial",40))
        message.pack(pady=50, side=TOP, anchor = CENTER)
        next_button = Button(ui,text="NEXT", command = nextPage2, font=("Arial",50))
        next_button.pack(side=RIGHT, anchor=SE)
    
    def button_disable():
        winner_button['command'] = progressbar()
        winner_button['text'] = "CONGRATULATIONS!!"
        winner_button['command'] = 0

    def nextPage2():
        ui.destroy()
        pg2()

    title_label = Label(ui, text = "THE THIRD LUCKY PRIZE WINNER:", font=("Arial Black",60))
    title_label.pack(side=TOP, anchor=N, padx=10, pady=10)
    winner_button = Button(ui,text="PICK YOUR WINNERS!", command = button_disable, font=("Arial",50))
    winner_button.pack(side=TOP, anchor=N, pady=20)

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
        message = Label(ui, text = "CONGRATS! THIS LUCKY OWNER WON 2 ETH", font=("Arial",40))
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
 
    title_label = Label(ui, text = "THE SECOND LUCKY PRIZE WINNER:", font=("Arial Black",60))
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
            time.sleep(1.5)
        progress_bar.destroy()
        winners()

    def winners():
        winner = Label(ui, text = rand_gen(), bd=8, relief="solid", font=("Arial",80), width=5, height=2)
        winner.pack(pady=80, side=TOP, anchor = CENTER) 
        message = Label(ui, text = "CONGRATS! THIS LUCKY OWNER WON 3 ETH", font=("Arial",40))
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
 
    title_label = Label(ui, text = "THE FIRST LUCKY PRIZE WINNER:", font=("Arial Black",60))
    title_label.pack(side=TOP, anchor=N, padx=10, pady=10)
    winner_button = Button(ui,text="PICK YOUR WINNERS!", command = button_disable, font=("Arial",50))
    winner_button.pack(side=TOP, anchor=N, pady=20)

    ui.mainloop()

def pg4():
    ui = Tk()
    ui.geometry("1920x1080")
    ui.title("META RAFFLE CLUB PRESENTS:")
    message_1 = Label(ui, text = "CONGRATULATIONS ALL WINNERS!", font=("Arial Black",60))
    message_1.pack(anchor=CENTER, padx=10, pady=10)
    message_2 = Label(ui, text = "MAY YOU 'DE-FI' THE ODDS NEXT MONTH", font=("Arial Black",60))
    message_2.pack(anchor=CENTER, padx=10, pady=10)
    message_3 = Label(ui, text = "SPEND YOUR ETH WISELY 🤤", font=("Arial Black",60))
    message_3.pack(anchor=CENTER, padx=10, pady=10)
    firework(ui, TOP, CENTER)

main()