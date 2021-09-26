import math

global map 

class tile_t:
    def __init__ (self, num, poss, square_num, line, column):
        self.num = num
        self.poss = poss
        self.square_num = square_num
        self.line = line
        self.column = column

def create_map():
    global map
    map=[]
    for i in range(9):
        map.append([])
        for j in range(9):
            temp=tile_t(0,[1,2,3,4,5,6,7,8,9],(math.floor(i/3)+2*(math.floor(i/3))+math.floor(j/3)),i,j)
            map[i].append(temp)

def add_nums():
    global map
    while(1):
        line=int(input("Line: "))-1
        
        if line==-1: 
            break

        column=int(input("Column: "))-1
        num=int(input("Number: "))

        map[line][column].num = num 
        remove_poss(line,column)

def remove_poss(line,column):
    global map
    for i in range(9):
        if map[line][column].num in  map[line][i].poss:
            map[line][i].poss.remove(map[line][column].num)

    for i in range(9):
        if map[line][column].num in  map[i][column].poss:
            map[i][column].poss.remove(map[line][column].num)

    for i in range(3):
        for j in range(3):
            if map[line][column].num in map[i+math.floor(map[line][column].square_num/3)*3][j+((map[line][column].square_num - (math.floor(map[line][column].square_num/3)*3))*3)].poss:
                map[i+math.floor(map[line][column].square_num/3)*3][j+((map[line][column].square_num - (math.floor(map[line][column].square_num/3)*3))*3)].poss.remove(map[line][column].num)

def solve():
    global map
    win = 1
    for i in range(9):
        for j in range(9):
            if len(map[i][j].poss)==1:
                map[i][j].num = map[i][j].poss[0]
                remove_poss(map[i][j].line, map[i][j].column)
            if len(map[i][j].poss)>1:
                win = 0
    if not win:
        solve()
    

def print_map():
    global map
    for i in range(9):
        print("\n")
        for j in range(9):
            print(map[i][j].poss)

def game():
    create_map()
    add_nums()
    solve()
    print_map()

game()
