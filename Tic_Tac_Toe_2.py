# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 09:07:32 2017

@author: Rishi Raj
"""

def tic_tac_toe():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    end = False
    win_commbinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    prev=0
    
    def restrict(n):
        if n==1:
            return [2,4]
        elif n==2:
            return [1,3,5]
        elif n==3:
            return [2,6]
        elif n==4:
            return [1,5,7]
        elif n==5:
            return [2,4,6,8]
        elif n==6:
            return [3,5,9]
        elif n==7:
            return [4,8]
        elif n==8:
            return [5,7,9]
        elif n==9:
            return [6,8]
        else:
            return []
        
    
    def draw():
        print(board[0], board[1], board[2])
        print(board[3], board[4], board[5])
        print(board[6], board[7], board[8])
        print()

    def p1(a):
        n = choose_number()
        if board[n] == "X" or board[n] == "O" or (n in restrict(a)) :
            print("\nYou can't go there. Try again")
            p1(a)
        else:
            board[n] = "X"
            return n

    def p2(a):
        n = choose_number()
        if board[n] == "X" or board[n] == "O" or (n in restrict(a)):
            print("\nYou can't go there. Try again")
            p2(a)
        else:
            board[n] = "O"
            return n

    def choose_number():
        while True:
            while True:
                a = input()
                try:
                    a  = int(a)
                    a -= 1
                    if a in range(0, 9):
                        return a
                    else:
                        print("\nThat's not on the board. Try again")
                        continue
                except ValueError:
                   print("\nThat's not a number. Try again")
                   continue

    def check_board():
        count = 0
        for a in win_commbinations:
            if board[a[0]] == board[a[1]] == board[a[2]] == "X":
                print("Player 1 Wins!\n")
                print("Congratulations!\n")
                return True

            if board[a[0]] == board[a[1]] == board[a[2]] == "O":
                print("Player 2 Wins!\n")
                print("Congratulations!\n")
                return True
        for a in range(9):
            if board[a] == "X" or board[a] == "O":
                count += 1
            if count == 9:
                print("The game ends in a Tie\n")
                return True

    while not end:
        draw()
        end = check_board()
        if end == True:
            break
        print("Player 1 choose where to place a cross")
        prev = p1(prev)
        print()
        draw()
        end = check_board()
        if end == True:
            break
        print("Player 2 choose where to place a nought")
        prev = p2(prev)
        print()

    if input("Play again (y/n)\n") == "y":
        print()
        tic_tac_toe()

tic_tac_toe()