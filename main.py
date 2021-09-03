class tile_t:
    def __init__ (self, num, poss, square_num, line, column):
        self.num = num
        self.poss = poss
        self.square_num = square_num
        self.line = line
        self.column = column

tile=tile_t(0,[1,2,3,4,5,6,7,8,9], 3, 4, 2)
print(tile.num)