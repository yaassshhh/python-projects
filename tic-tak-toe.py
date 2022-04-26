# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 00:00:41 2022

@author: Yashraj Nigam
"""
import math
import random
import time
from player import HumanPlayer, RandomComputerPlayer

class TicTacToe():
    def __init__(self):
         self.board = [' ' for _ in range(9)]
         self.current_winner = None
        
    def print_board(self):
         #this is getting the rows  
         for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
             print('| '+' | '.join(row)+' |')
    
    @staticmethod
    def print_board_nums():
        # 0|1|2 etc (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| '+' | '.join(row)+' |')
    
    def available_moves(self):
        return[i for i , spot in enumerate(self.board) if spot == ' ']
    
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        if self.board[square]==' ':
            self.board[square]=letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
       # check the row
        row_ind = math.floor(square // 3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        
        if all([spot == letter for spot in row]):
            return True
        
        # check the column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        
        if all([spot == letter for spot in column]):
            return True
        
        # check the diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            
            if all([spot == letter for spot in diagonal2]):
                return True
        return False  
    
def play(game, x_player, o_player, print_game = True):
    if print_game:
        game.print_board_nums()
        
    letter = 'x' # starting letter
    # iterate while the game still has empty squares
    #(about winner - just return that which breaks the loop)
    while game.empty_squares():
        #get the move from the appropriate player
        if letter == 'o':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
            
        #let's define a function to make a move!
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print(' ') # just empty line
            
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter
            
            # after we made our move , we need to alternate letters
            letter = 'o' if letter == 'x' else 'x' 
        
        time.sleep(.8)
        
    if print_game:
        print('It\'s a tie!')
        
if __name__ == '__main__':
    x_player = HumanPlayer('x')
    o_player = RandomComputerPlayer('o')
    t = TicTacToe()
    play(t, x_player, o_player, print_game = True)