import random

class Minefield:
    """Minesweeper class with handling and win condition.
    Internally has two arrays for the board and mines. 
    """
    def __init__(self, w, h, mines):
        self.board = [['#']*w for _ in range(h)]
        self.mineLayer = [[False]*w for _ in range(h)]
        self.width = w
        self.height  = h

        # place some mines on the field
        for m in range(mines):
            x = random.randint(0,w-1)
            y = random.randint(0,h-1)
            while self.mineLayer[x][y]:
                x = random.randint(0,w-1)
                y = random.randint(0,h-1)
            self.mineLayer[y][x] = True

    def __str__(self):
        return '\n'.join([''.join(['{:2}'.format(item) for item in row]) for row in self.board])

    def check(self, x, y):
        """Return the content of mineLayer in location (x,y)."""
        if x<0 or y<0:
            raise IndexError
        return self.mineLayer[y][x]
    
    def flag(self, x, y):
        """Place or remove a flag."""
        if self.board[y][x] in '#F':
            if not self.board[y][x] == 'F':
                self.board[y][x] = 'F'
                return
            self.board[y][x] = '#'

    def count(self, x, y):
        """Count surrounding mines."""
        count = 0
        for w in range(-1,2):
            for h in range(-1,2):
                try:
                    if not (w==0 and h==0) and self.check(x+w, y+h):
                        count += 1
                except IndexError:
                    pass
        return count

    def open(self, x, y):
        """Open surrounding mines and repeat on empty spots.
        Return true or false if there wasn't or was a mine.
        """
        if self.board[y][x] == '#':
            if not self.check(x,y):
                c = self.count(x,y)
                if c > 0:
                    self.board[y][x] = str(c)
                else:
                    self.board[y][x] = '.'
                    for w in range(-1,2):
                        for h in range(-1,2):
                            if not (w==0 and h==0):
                                try:
                                    self.open(x+w, y+h)
                                except IndexError:
                                    pass
                return True
            return False
        return True

    def showMines(self):
        return '\n'.join([''.join(['{:2}'.format(item) for item in row]) for row in self.mineLayer])

    def winCondition(self):
        """Check if all mines have been cleared."""
        for w in range(self.width):
            for h in range(self.height):
                if self.board[h][w] in '#F' and not self.check(w,h): 
                    return False
        return True

