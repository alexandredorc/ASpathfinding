import pygame as pg
import sys
from time import sleep

pg.init()
size=800
rows=100
width=size//rows
screen = pg.display.set_mode((size, size))

white=(255,255,255)
red=(162,15,15)
green=(30,170,15)
blue=(15,40,170)
black=(0,0,0)
cyanS=(75,200,200)
cyanE=(75,201,200)
wall=(12,34,56)
grey=(125,125,125)


#preset pos

class Node: 
    def __init__(self,row, col, width,total):
        self.row = row
        self.colum = col
        self.x = row * width
        self.y = col * width
        self.color = white
        self.neighbords=[]
        self.width = width
        self.total = total
        self.gainS=-1
        

    def getpos(self):
        return self.row, self.col

    def is_state(self,color):
        return self.color == color

    def changeColor(self,color):
        self.color = color

    def draw(self,screen):
        pg.draw.rect(screen,self.color,(self.x, self.y, self.width, self.width ))

    def update(self,grid):
        pass

    def __lt__(self,other):
        return False

def dist(p1,p2):
    x1,y1= p1
    x2,y2= p2
    x=abs(x2-x1)
    y=abs(y2-y1)
    d=max(x,y)-abs(x-y)
    return d*14 + (x-d)*10 + (y-d)*10


def make_grid(rows,width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i,j,gap,rows)
            grid[i].append(node)

    return grid 

def draw_grid(screen, rows,width):
    gap = width // rows
    for i in range(rows):
        pg.draw.line(screen,grey,(0,i*gap),(width,i*gap))
        pg.draw.line(screen,grey,(i*gap,0),(i*gap,width))

def draw(screen,grid,rows,width):
    screen.fill(white)
    for row in grid:
        for node in row:
            node.draw(screen)
    draw_grid(screen,rows,width)
    pg.display.update()

def get_pos(pos,rows,size):
    x,y=pos
    return(x*rows//size,y*rows//size)

def change(pos,color,grid):
    grid[pos[0]][pos[1]].changeColor(color);

            
def pen(pos,color,grid,stroke):
    for x in range(-1*stroke+1,stroke):
        for y in range(-1*stroke+1,stroke):
            if pos[0]+x>=0 and pos[0]+x<rows and pos[1]+y>=0 and pos[1]+y<rows and not grid[pos[0]+x][pos[1]+y].is_state(cyanE) and not grid[pos[0]+x][pos[1]+y].is_state(cyanS):
                change((pos[0]+x,pos[1]+y),color,grid)

def activate(node,origin,posx,posy,posE):
    if  node.gainS ==-1:
        node.origin=origin
        if posy != 0 and posx != 0:
            node.gainS=origin.gainS+14
        else:
            node.gainS=origin.gainS+10
    elif posy != 0 and posx != 0 :
        if node.gainS>origin.gainS+14:
            node.origin=origin
            node.gainS=origin.gainS+14
    else:
        if node.gainS > origin.gainS+10:
            node.origin=origin
            node.gainS=origin.gainS+10

    
    node.gainE=dist((node.row,node.colum),posE)

    
    node.totgain=(node.gainE*1.5)+node.gainS
   
        
    
def activatearound(grid,pos,posE,posS):
    if pos!=posE and pos!=posS:
        change((pos[0],pos[1]),red,grid)
    for i in range(-1,2):
        for j in range(-1,2):
            if  pos[0]+i>=0 and pos[0]+i<rows and pos[1]+j>=0 and pos[1]+j<rows and grid[pos[0]+i][pos[1]+j].color!=wall and grid[pos[0]+i][pos[1]+j].color!=cyanE and grid[pos[0]+i][pos[1]+j].color!=cyanS :
                activate(grid[pos[0]+i][pos[1]+j],grid[pos[0]][pos[1]],i,j,posE)
                if grid[pos[0]+i][pos[1]+j].color!=red:
                    grid[pos[0]+i][pos[1]+j].color=green
            elif (pos[0]+i,pos[1]+j)==posE:
                return grid[pos[0]][pos[1]]
    return False
          
                
            

def algo(grid,posE,posS):
    finish=0
    best = Node(-1, -1, -1,-1)
    best.totgain=-1
    totgain=-1
    lisBest=[]
    for row in grid:
        for node in row:
            if node.color==green:
                if node.totgain < totgain or totgain==-1 :
                    lisBest=[]
                    lisBest.append(node)
                    totgain=node.totgain
                if node.totgain == best.totgain:
                    lisBest.append(node)
                if node.row==posE[0] and node.colum==posE[1]:
                    return 1
    
    mini = Node(-1, -1, -1,-1)
    mini.gainE =-1
    for i,node in enumerate(lisBest):
        if node.gainE < mini.gainE or mini.gainE==-1:
            mini=node
    finish =activatearound(grid,(mini.row,mini.colum),posE,posS)

    
    return finish

def recFindWay(grid,posS,node):
    if (node.row,node.colum)==posS:
        return True
    else:
        node.color=blue
        recFindWay(grid,posS,node.origin)


def findWay(grid,posE,posS,finish):
    grid[posE[0]][posE[1]].color=blue
    recFindWay(grid,posS,finish)
    '''
    best = Node(-1, -1, -1,-1)
    best.totgain=-1
    for i in range(-1,2):
        for j in range(-1,2):
            if (posE[0]+i,posE[1]+j)==posS:
                return 0
            if posE[0]+i>=0 and posE[0]+i<rows and posE[1]+j>=0 and posE[1]+j<rows and grid[posE[0]+i][posE[1]+j].color==red :
                if grid[posE[0]+i][posE[1]+j].totgain < best.totgain or best.totgain==-1 :
    
                    best=grid[posE[0]+i][posE[1]+j]'''
    
    
 
def main():
    
    finish=0
    state= 'start'
    memo='start'
    grid=make_grid(rows,size)
    stroke=1
    pg.display.update()
    #GameLoop
    run = True
    while run:
        
    
        draw(screen,grid,rows,size)
        keys=pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        if state== 'pause':
            if pg.mouse.get_pressed() !=(1,0,0):
                state=memo

        if state == 'start':
            if pg.mouse.get_pressed() ==(1,0,0):
                pos = get_pos(pg.mouse.get_pos(),rows,size)
                change(pos,cyanS,grid)
                state='pause'
                memo='end'
                posS=pos
                grid[pos[0]][pos[1]].gainS=0
        elif state == 'end':
            if pg.mouse.get_pressed() ==(1,0,0):
                pos = get_pos(pg.mouse.get_pos(),rows,size)
                change(pos,cyanE,grid)
                state='pause'
                memo='walls'
                posE=pos

        elif state == 'walls':
            if pg.mouse.get_pressed() ==(1,0,0):
                pos = get_pos(pg.mouse.get_pos(),rows,size)
                if keys[pg.K_LSHIFT]:
                    pen(pos,white,grid,stroke)
                else:
                    pen(pos,wall,grid,stroke)
            x,y = get_pos(pg.mouse.get_pos(),rows,size)
            if keys[pg.K_1]:
                stroke=1
            if keys[pg.K_2]:
                stroke=2
            if keys[pg.K_3]:
                stroke=3
            if keys[pg.K_4]:
                stroke=4
            if keys[pg.K_RETURN]:
                state = 'finding'
                activatearound(grid,posS,posE,posS)

        elif state == 'finding':
            finish=algo(grid,posE,posS)
        elif state=='find way':
            findWay(grid,posE,posS,finish)
            state='finish'
            print('tessend')
            finish=0


        if finish!=False:
            state= 'find way'
        if state=='finish':
            if keys[pg.K_RETURN]:
                    finish=0
                    state= 'start'
                    memo='start'
                    grid=make_grid(rows,size)
                    stroke=1
                    pg.display.update()
        
        pg.display.update()
    print('end')
    pg.quit()


main()