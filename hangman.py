# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 12:04:19 2020

@author: Kota
"""
import random

def hangman():
    word_list = ["cat","dog","monkey","whale","mintia"]
    random_num = random.randint(0, 4)
    word = word_list[random_num]
    wrong_guesses = 0
    stages = ["", 
              "________      ", 
              "|      |      ", 
              "|      0      ", 
              "|     /|\     ", 
              "|     / \     ", 
              "|"]
    remaining_letters = list(word)
    letter_board = ["__"] * len(word)
    win = False
    print("ハングマンへようこそ！")
    while wrong_guesses < len(stages) - 1:
        print("\n")
        guess = input("１文字を予想してね: ")
        if guess in remaining_letters:
            character_index = remaining_letters.index(guess)
            letter_board[character_index] = guess
            remaining_letters[character_index] = "$"
        else:
            wrong_guesses += 1
        print(" ".join(letter_board))
        e = wrong_guesses + 1
        print("\n".join(stages[0:e]))
        if "__" not in letter_board:
            print("あなたの勝ち！")
            print(" ".join(letter_board))
            win = True
            break
    if not win:
        print("\n".join(stages[0 : wrong_guesses + 1]))
        print("あなたの負け！正解は {}.".format(word))
        


hangman()
        