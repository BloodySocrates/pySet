class Board:
    def __init__(self):
        '''
        todo: add total width and height properties, 
        so this class can serve as config for pygame.display.set_mode
 
CARDHEIGHT=100
CARDWIDTH=200
GUTTER=CARDWIDTH/10
ROWS=4
COLUMNS=4

       '''
        self.cardwidth = 200
        self.cardheight = 100
        self.gutter = 20
        self.rows = 4
        self.columns = 4
        self.total_width = ((self.cardwidth+self.gutter)*self.columns)+self.gutter
        self.total_height = ((self.cardheight+self.gutter)*self.rows)+self.gutter


    def get_coords(self):
        '''
        takes a gutter size, card height, card width
        number of columns, and number of rows
        returns 2d array of points for cards
        '''
        array=[]
        y_values=[self.gutter+(self.cardheight+self.gutter)*i for i in range(0,self.columns)]
        for y in y_values:
            for i in range(0,self.rows):
                cardx=self.gutter+(self.cardwidth+self.gutter)*i
                cardy=y
                array.append((cardx, cardy)) 
        return array

