import pygame as pg
import sys




posS=(2,4)
posE=(7,9)
pg.init()
size=1000
rows=200
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

def casePath(node):
    pass

def pathfinding(grid):
    for row in grid:
        for node in row:
            node= casePath(node)
            
def pen(pos,color,grid,stroke):
    for x in range(-1*stroke+1,stroke):
        for y in range(-1*stroke+1,stroke):
            if pos[0]+x>=0 and pos[0]+x<rows and pos[1]+y>=0 and pos[1]+y<rows and not grid[pos[0]+x][pos[1]+y].is_state(cyanE) and not grid[pos[0]+x][pos[1]+y].is_state(cyanS):
                change((pos[0]+x,pos[1]+y),color,grid)
            

def main():
    
    state= 'walls'
    grid=make_grid(rows,size)

    change(posE,cyanE,grid)
    change(posS,cyanS,grid)
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
        
        if state == 'walls':
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
        elif state == 'finding':
            pass
        
        pg.display.update()
    pg.quit()


main()