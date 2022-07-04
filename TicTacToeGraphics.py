import sys, pygame
from TicTacTeo import *

def cellpos(pos,cells):
    for r in range(3):
        for c in range(3):
            if cells[r][c].collidepoint(pos):
                return (r,c)
    return None


pygame.init()
clock=pygame.time.Clock()
font = pygame.font.Font(pygame.font.get_default_font(), 70)
screen_size = width, height = 1000, 1000
screen_color = 0, 0, 0
screen = pygame.display.set_mode(screen_size)

gridimg = pygame.image.load("Grid.png")
gridimg = pygame.transform.scale(gridimg,screen_size)
ximg_size= (235, 235)
oimg_size= (220, 220)
ximg = pygame.image.load("X.png")
ximg = pygame.transform.scale(ximg,ximg_size)
oimg = pygame.image.load("O.png")
oimg = pygame.transform.scale(oimg,oimg_size)


cells = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]
img_size=(225,225)
cells[0][0]=pygame.Rect((55,60),img_size)
cells[0][1]=pygame.Rect((400,60),img_size)
cells[0][2]=pygame.Rect((740,60),img_size)
cells[1][0]=pygame.Rect((50,390),img_size)
cells[1][1]=pygame.Rect((400,390),img_size)
cells[1][2]=pygame.Rect((740,390),img_size)
cells[2][0]=pygame.Rect((50,710),img_size)
cells[2][1]=pygame.Rect((400,710),img_size)
cells[2][2]=pygame.Rect((740,710),img_size)

grid = [[' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]
player='X'
finish=False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if player == 'X' and not finish:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                cellp=cellpos(pos,cells)
                if cellp != None:
                    grid[cellp[0]][cellp[1]]='X'
                    player='O'
    if getstatus(grid) != 'Resume':
        finish=True
    if player=='O' and not finish:
        ai(grid, player)
        player='X'
    screen.fill(screen_color)
    screen.blit(gridimg,(0,0))
    for r in range(3):
        for c in range(3):
            if grid[r][c]=='X':
                screen.blit(ximg,cells[r][c])
            if grid[r][c]=='O':
                screen.blit(oimg,cells[r][c])
    if finish:
        text_surface = font.render(getstatus(grid) + ' Wins', True, (255, 255, 0))  
        screen.blit(text_surface, (0, 0))
    pygame.display.flip()
    clock.tick(30)

    # now print the text
