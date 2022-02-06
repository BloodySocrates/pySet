class Board:
    def __init__(self, cardwidth, cardheight, gutter, rows, columns):
        self.cardwidth = cardwidth
        self.cardheight = cardheight
        self.gutter = gutter
        self.rows = rows
        self.columns = columns
        self.board = self.make_board()

    def make_board(self):
        '''
        takes a gutter size, card height, card width
        and number of columns, and number of rows
        returns 2d array of points for cards
        '''
        array=[]
        y_values=[self.gutter+(self.cardheight+self.gutter)*i for i in range(0,self.columns)]
        for y in y_values:
            row=[]
            for i in range(0,self.rows):
                cardx=self.gutter+(self.cardwidth+self.gutter)*i
                cardy=y
                row.append((cardx, cardy)) 
            array.append(row)
        return array

board=Board(200, 100, 20, 4, 4)
print(board.board)

