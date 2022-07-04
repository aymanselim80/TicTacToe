def showgrid(grid):
    for row in grid:
        print(row)

def getstatus(grid):
    for row in range (3): #Check Rows for winner
        if grid[row][0]==grid[row][1]==grid[row][2]!=' ':
            return grid[row][0]
    for col in range (3): #Check Columns for winner
        if grid[0][col]==grid[1][col]==grid[2][col]!=' ':
            return grid[0][col]
    if grid[0][0] == grid[1][1] == grid[2][2] !=' ' or grid[0][2] == grid[1][1] == grid[2][0]!=' ': #Check Diagonal for winner
        return grid[1][1]
    for row in range (3):#Check if not full
        for col in range (3):
            if grid[row][col]==' ':
                return 'Resume'
    return 'No One'

def getscore(grid):
    result=getstatus(grid)
    if result=='X': #AI lose
        return -1
    if result=='O':#AI wins
        return 1
    return 0 #Tie

def playerinput(grid,player):
    print('availvable moves', availablemoves(grid))
    while True:
        row, col = input('Enter the destination For player ' + player).split(',') #take Pos
        row = int(row)
        col = int(col)
        if (row, col) not in availablemoves(grid): print('Wrong move'); continue
        grid[row][col] = player
        break

def gameplay(grid):
    player='X'
    while True:
        showgrid(grid)
        if player=='X': playerinput(grid,player) #Player Turn
        else: ai(grid,player)#AI Turn
        player = 'X' if player == 'O' else 'O'
        if getstatus(grid) !='Resume':
            showgrid(grid)
            print(getstatus(grid),'WINS')
            break

def ai(grid,mark):
    row,col=minimax(grid,True)[1]#Get the best move
    grid[row][col]=mark

def availablemoves(grid):
    moves=[]
    if getstatus(grid) !='Resume':#Game over
        return moves
    for row in range (3):
        for col in range (3):
            if grid[row][col]==' ': moves.append((row,col)) #add empty postions
    return moves

def minimax(grid,ismax):
    av_moves=availablemoves(grid)
    if av_moves==[]:
        return getscore(grid),None
    if ismax:
        maxval=-999
        for i in range (len(av_moves)):
            x = av_moves[i][0]
            y= av_moves[i][1]
            val=minimax(getnext(grid,x,y,'O'),False)[0]
            if val>maxval:
                maxval=val
                pos=(x,y)
        return maxval,pos
    else:
        minval =999
        for i in range (len(av_moves)):
            x = av_moves[i][0]
            y= av_moves[i][1]
            val=minimax(getnext(grid,x,y,'X'),True)[0]
            if val < minval:
                minval = val
                pos = (x, y)
        return minval, pos

def getnext(grid,row,col,mark):
    nextgrid=[]
    for r in range(3): #copy the current grid
        nextgrid.append([])#create empty row
        for c in range(3):#put three values in each row
            nextgrid[r].append(grid[r][c])
    nextgrid[row][col]=mark #apply action to grid
    return nextgrid

if __name__ == '__main__':

    grid=[[' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' ']]
    gameplay(grid)
