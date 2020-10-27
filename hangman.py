ngmanGame(word):
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    remaining_letters = list(word.upper())
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages) - 1:
        print("\n")
        char = input("Guess a letter: ").upper()
        if char in remaining_letters:
            found = True
            while found == True:
                if char in remaining_letters:
                    cind = remaining_letters.index(char)
                    board[cind] = char
                    remaining_letters[cind] = '$'
                else:
                    found = False
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print(f"You lose! It was \"{word.upper()}\".")
