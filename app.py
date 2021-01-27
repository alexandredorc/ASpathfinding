import pygame as pg
import sys

maps=[['0','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0','B','0'],
    ['0','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0','0','0'],
    ['0','0','A','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0','0','0']]
    
print(maps)
pg.init()
size=1000
screen = pg.display.set_mode((size, size))

white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
font = pg.font.Font('freesansbold.ttf', 20)

screen.fill((12,34,56))
for i in range(1, 10):
    pg.draw.line(screen,white,(size*i//10,0),(size*i//10,size))
    pg.draw.line(screen,white,(0,size*i//10),(size,size*i//10))
for x in range(0,10):
    for y in range(0,10):
        if maps[y][x]!='0':
            pg.draw.rect(screen,red,(x*size/10+1,y*size//10+1,size//10 -1,size//10-1))
            img = font.render(maps[y][x], True, blue)
            rect=img.get_rect()
            rect.center=(x*10,y*10)
            print(rect)
            screen.blit(img,)
           




#GameLoop
running = True
while running:





    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    pg.display.update()