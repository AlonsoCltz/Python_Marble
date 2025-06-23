import pygame
import math
import random
from tkinter import *
from tkinter import messagebox
pygame.init()
width=1000
height=950
win=pygame.display.set_mode((width,height))
pygame.display.set_caption("Pachinko")
clock=pygame.time.Clock()
run=True
WHITE=(250,250,250)
RED=(250,0,0)
ORANGE=(200,250,0)
GREEN=(0,250,250)
BLACK=(0,0,0)
gravity=0.4
vy=-25
vx=0
ballpos=[width-70,height-100]
situ=0
circ=[width/2,500]
Rc=(width-40-(width/2))
pill=[]
line=[]
linest=[width-40,height-100]
ball=5
ballin=0
def drawword(st):
    global win
    global clock
    pygame.font.init()
    ft=pygame.font.SysFont('comicsans',50)
    txt=ft.render(st,False,WHITE)
    win.blit(txt,(100,200))
    pygame.display.flip()
    clock.tick(1)
def redraw():
    global ball
    global linest
    pos=[50,500]
    inter=100
    dot=10
    col=5
    for j in range(1,col):
        for i in range(1,dot):
            pygame.draw.circle(win,WHITE,(pos[0]+((i-1)*inter),pos[1]),10)
            
        if i%2==0:
            pos[0]-=(inter/2)
            pos[1]+=inter
            dot+=1
        else:
            pos[0]+=(inter/2)
            pos[1]+=inter
            dot-=1
    for k in line:
        if k.score == True :
            pygame.draw.rect(win,RED,(k.x,k.y,inter,height-k.y))
        pygame.draw.line(win,WHITE,(k.x,k.y),(k.x,height))
    #draw path
    pygame.draw.line(win,WHITE,(linest[0],linest[1]),(linest[0],circ[1]))
    pygame.draw.line(win,WHITE,(linest[0]-60,linest[1]),(linest[0]-60,circ[1]))
    pygame.draw.arc(win, WHITE, (circ[0]/12,circ[1]/12-40, (linest[0]-circ[0])*2, (linest[0]-circ[0])*2),-0.09, math.pi+0.09, 5)
    pygame.draw.circle(win,RED,(ballpos[0],ballpos[1]),20)
    pygame.display.update()
class pillar():
    def __init__(self,x,y):
        self.x=x
        self.y=y
class ln():
    def __init__(self,x,y,b):
        self.x=x
        self.y=y
        self.score=b
#bool for tkinter
choose=0
def slot():
    global vy
    global run
    global ballin
    global root
    global slider
    global ball
    global choose
    global run
    choose=0
    situ = -1
    left=width-490
    right=width-370
    interval=60
    win.fill(BLACK)
    redraw()
    #get ball
    def printInfo():
        global ballin
        global choose
        ballin=int(slider.get())
        choose=1
        window.destroy()
    window=Tk()
    if ball>=2:
        Label(window,text=str(ball)+' balls left').pack()
    elif ball==1:
        Label(window,text='last shot').pack()
    elif ball<=0:
        messagebox.showinfo('INFO','You Lose')
        pygame.quit()
        window.destroy()
        run=False
        return
        
    slider=Scale(window,from_=1,to=ball,orient=HORIZONTAL)
    slider.pack()
    def qt():
        global run
        window.destroy()
        pygame.quit()
        run=False
        return
    Button(window,text='save',command=printInfo).pack()
    Button(window,text='quit game',command=qt).pack()
    window.mainloop()
    if(choose==0 and run==True):
        messagebox.showinfo('Warning','Save First')
        return False
    
    
    lnpos=left
    lnv=3
    while situ == -1 :
        clock.tick(30)
        win.fill(BLACK)
        pygame.draw.rect(win,WHITE,(lnpos,height-700,15,60))
        pygame.draw.rect(win, RED,(right,height-700,interval,10))
        pygame.draw.rect(win, ORANGE,(right-interval,height-700,interval,10))
        pygame.draw.rect(win, GREEN,(right-2*interval,height-700,interval,10))
        redraw()
        lnpos+=lnv
        if(lnpos>=right+interval-15 or lnpos<=left):
            lnv*=-1
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                rt=((lnpos-left)/(right+interval-15-left))
                vy=21+(rt*6)
                vy*=-1
                situ=0
            if event.type == pygame.QUIT:
                run=False
                situ=0
def start():
    global situ
    global vx
    global vy
    global ballpos
    global text
    global line
    line=[]
    situ=0
    vx=0
    ballpos=[width-70,height-100]
    pos=[50,500]
    inter=100
    dot=10
    col=5
    for j in range(1,col):
        for i in range(1,dot):
            pill.append(pillar(pos[0]+((i-1)*inter),pos[1]))
        if i%2==0:
            pos[0]-=(inter/2)
            pos[1]+=inter
            dot+=1
        else:
            pos[0]+=(inter/2)
            pos[1]+=inter
            dot-=1
    pos[1]-=(inter-15)
    for i in range(1,dot):
        line.append(ln(pos[0]+((i-1)*inter),pos[1],bool(4>=random.randint(0, 10))))
    line[len(line)-1].score=False
    win.fill(BLACK)
    redraw()
    #shot
    while(run==True and slot()==False):
        continue
    situ=1
if run==True:
    start()

def bounce(ax , ay , bx , by):
    #a: the speed / b: the position
    # a allign with b
    const=((ax*bx)+(ay*by))/(bx**2 + by**2)
    projx=const*bx #change
    projy=const*by
    vertx=ax-projx #hold
    verty=ay-projy
    epstron=0.3
    return (vertx-(projx*epstron),verty-(projy*epstron))
while run:
    clock.tick(30)
    #shot
    if situ==1:
        ballpos[1]+=vy
        vy+=gravity
        if(ballpos[1]<=500 and (ballpos[0]-(width/2))**2 + (ballpos[1]-circ[1])**2 >= (width-40-(width/2))**2):
            situ=2
    elif situ==2:
        vec=[ballpos[0]-circ[0] , ballpos[1]-circ[1]]
        vec2=[vec[1],(-1)*vec[0]]
        lengt=(vec2[0]**2 + vec2[1]**2)
        Vlengt=(vy**2 + vx**2)
        ratio=Vlengt/lengt
        ratio=ratio**(0.5)
        newvec=[vec2[0]*ratio , vec2[1]*ratio]
        vx=newvec[0]
        vy=newvec[1]
        vy+=gravity
        ballpos[0]+=vx
        ballpos[1]+=vy
        #leave the arch
        sinn=(ballpos[1]-circ[1])/Rc
        coss=(ballpos[0]-circ[0])/Rc
        acce=Vlengt/Rc
        if acce<gravity:
            situ=3
        elif ballpos[0]<=circ[0]-Rc:
            situ=3
    #radius = 30
    elif situ==3:
        vy+=gravity
        ballpos[0]+=vx
        ballpos[1]+=vy
        #pillar bounce
        for i in pill:
            if (ballpos[0]-i.x)**2 + (ballpos[1]-i.y)**2 <= 900 :
                if (vx*(i.x-ballpos[0])) + (vy*(i.y-ballpos[1]))>0:
                    (vx,vy)=bounce(vx,vy,i.x-ballpos[0],i.y-ballpos[1])
        #arch bounce
        if(ballpos[1]<=500 and (ballpos[0]-(width/2))**2 + (ballpos[1]-circ[1])**2 >= (width-40-(width/2))**2):
            vex=ballpos[0]-circ[0]
            vey=ballpos[1]-circ[1]
            if (vx*(vex)) + (vy*(vey))>0:
                (vx,vy)=bounce(vx,vy,vex,vey)
        #right line bounce
        if(ballpos[1]>=500 and ballpos[0]>=linest[0]-80):
            vex=linest[0]-60-ballpos[0]
            vey=0
            if (vx*(vex)) + (vy*(vey))>0:
                (vx,vy)=bounce(vx,vy,vex,vey)
        #score line bounce
        for i in line:
            if ballpos[1]>=i.y-20 and ((ballpos[0]-i.x)*(ballpos[0]-20-i.x)<=0):
                if ballpos[1]<=i.y:
                    vex=i.x-ballpos[0]
                    vey=i.y-ballpos[1]
                    if (vx*(vex)) + (vy*(vey))>0:
                        (vx,vy)=bounce(vx,vy,vex,vey)
                else:
                    vex=i.x-ballpos[0]
                    vey=0
                    if (vx*(vex)) + (vy*(vey))>0:
                        (vx,vy)=bounce(vx,vy,vex,vey)

            elif ballpos[1]>=i.y-20 and (ballpos[0]-i.x)*(ballpos[0]+20-i.x)<=0:
                if ballpos[1]<=i.y:
                    vex=i.x-ballpos[0]
                    vey=i.y-ballpos[1]
                    if (vx*(vex)) + (vy*(vey))>0:
                        (vx,vy)=bounce(vx,vy,vex,vey)
                else:
                    vex=i.x-ballpos[0]
                    vey=0
                    if (vx*(vex)) + (vy*(vey))>0:
                        (vx,vy)=bounce(vx,vy,vex,vey)
               
    if ballpos[0]>width or ballpos[1]>height:
        doesiwin=0
        
        for i in range(0,len(line)):
            if line[i].score==True and line[i].x<ballpos[0] and line[i+1].x>ballpos[0]:
                doesiwin=1
        if doesiwin==1:
            drawword('Win (+'+str(ballin)+')')
            ball+=ballin
            ballin=0
        else:
            drawword('Miss (-'+str(ballin)+')')
            ball-=ballin
            ballin=0
        
        start()
    
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    win.fill(BLACK)
    redraw()
pygame.quit()
#pyinstaller -F -w -i ./icicic.ico main.py