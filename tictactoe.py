class Element:
    def __init__(self,position):
        self.position = position
        self.hor_score = {'X':0,'O':0}
        self.vert_score = {'X':0,'O':0}
        self.diag_score = {'X':0,'O':0}
        self.anti_diag_score = {'X':0,'O':0}
        self.state = 0

class Board:

    def __init__(self, rows=3, columns=3):
        self.game_over = False
        self.rows = rows
        self.columns = columns
        self.board = [[Element((row-1)*self.columns + column ) for column in range(self.columns+2)] for row in range(self.rows+2)]
        # self.players = ('X','O')
        self.current_player = 'X'
        self.empty_cells = columns*rows
    
    def toggle_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def draw_board(self):
        # players = {1:'X', 2:'O'}

        for row in range(1,self.rows+1):
            for column in range(1,self.columns+1):
                if self.board[row][column].state == 0:
                    print(' {} '.format(self.board[row][column].position), end='')
                else:
                    print(' {} '.format(self.board[row][column].state), end='')
            
            print('')
            # print('_'*self.columns)

    def update_board(self,position):
        if position < self.board[1][1].position or position > self.board[-2][-2].position or not isinstance(position,int):
            raise IndexError('choose value within the board')

        i = (position - 1) // self.rows + 1
        j = (position - 1) % self.columns + 1

        # print(type(self.board[i][j]))
        self.board[i][j].state = self.current_player
        self.board[i][j].vert_score[self.current_player] += 1
        self.board[i][j].hor_score[self.current_player] += 1
        self.board[i][j].diag_score[self.current_player] += 1
        self.board[i][j].anti_diag_score[self.current_player] += 1

        up = i-1
        down = i+1
        left = j-1
        right = j+1

        # vertical
        if self.board[up][j].state == self.current_player:
            self.board[i][j].vert_score[self.current_player] += 1
            self.board[up][j].vert_score[self.current_player] += 1
        if self.board[down][j].state == self.current_player:
            self.board[i][j].vert_score[self.current_player] += 1
            self.board[down][j].vert_score[self.current_player] += 1
        
        # horizontal
        if self.board[i][left].state == self.current_player:
            self.board[i][j].hor_score[self.current_player] += 1
            self.board[i][left].hor_score[self.current_player] += 1
        if self.board[i][right].state == self.current_player:
            self.board[i][j].hor_score[self.current_player] += 1
            self.board[i][right].hor_score[self.current_player] += 1

        # diag
        if self.board[up][left].state == self.current_player:
            self.board[i][j].diag_score[self.current_player] += 1
            self.board[up][left].diag_score[self.current_player] += 1
        if self.board[down][right].state == self.current_player:
            self.board[i][j].diag_score[self.current_player] += 1
            self.board[down][right].diag_score[self.current_player] += 1
        
        # anti diag
        if self.board[up][right].state == self.current_player:
            self.board[i][j].anti_diag_score[self.current_player] += 1
            self.board[up][right].anti_diag_score[self.current_player] += 1
        if self.board[down][left].state == self.current_player:
            self.board[i][j].anti_diag_score[self.current_player] += 1
            self.board[down][left].anti_diag_score[self.current_player] += 1

        # check winning
        if (self.board[i][left].hor_score[self.current_player] >= 3 or self.board[i][right].hor_score[self.current_player] >= 3 or
            self.board[up][j].vert_score[self.current_player] >= 3 or self.board[down][j].vert_score[self.current_player] >= 3 or
            self.board[up][left].diag_score[self.current_player] >= 3 or self.board[down][right].diag_score[self.current_player] >= 3 or
            self.board[up][right].anti_diag_score[self.current_player] >= 3 or self.board[down][left].anti_diag_score[self.current_player] >= 3):
            print('{} wins!'.format(self.current_player))
            self.game_over = True
        
        self.empty_cells -= 1

        if self.empty_cells == 0:
            self.game_over = True
            print('Draw!')


class Bot:
    def __init__(self,first_player=True):
        self.is_first_player = first_player
    
    def play_move(self):
        # analyse based on ranking algo
        pass

        
if __name__ == '__main__':
    board = Board()
    board.draw_board()

    while not board.game_over:
        print('{} turn. Choose position'.format(board.current_player))
        while True:
            try:
                position = int(input())
            except IndexError:
                print('try again')
            break

        board.update_board(position)
        board.toggle_player()
        board.draw_board()

