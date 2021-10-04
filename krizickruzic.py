def display_board(board):
    print(board[7]+ ' I ' +board[8]+ ' I '+board[9])
    print(board[4]+ ' I ' +board[5]+ ' I '+board[6])
    print(board[1]+ ' I ' +board[2]+ ' I '+board[3])
empty_board = [""] * 10
playerx_choices = []
playero_choices = []
play_count = 0
play_limit = 9
winning_combination = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
print(display_board(empty_board))
while play_count != play_limit and playerx_choices not in winning_combination:
    result = max([len(set(playerx_choices) & set(ele)) for ele in winning_combination])
    try:
        playerx_input = int(input("Player X: Please choose a number from 1 to 9: "))
    except ValueError:
        print("Please enter a number, not a letter. ")
        continue
    if playerx_input not in range(1,10):
        print("Please enter a number from 1 to 9. ")
        continue
    if playerx_input in playerx_choices or playerx_input in playero_choices:
        print("Position already played, please enter a new position. ")
        continue
    else:
        playerx_choices.append(playerx_input)
        empty_board[playerx_input] = "X"
        result = max([len(set(playerx_choices) & set(ele)) for ele in winning_combination])
        print(display_board(empty_board))
        play_count += 1
    if result == 3:
        print("Player X WINS! ")
        break
    else:
        pass
    if play_count == play_limit:
        print("DRAW! ")
        play_again = input("If You want to play again, enter Y .")
        if play_again.upper() == "Y":
            play_count = 0
            playerx_choices.clear()
            playero_choices.clear()
            empty_board = [""] * 10
            continue
        else:
            break
    print(display_board(empty_board))
    result = max([len(set(playero_choices) & set(ele)) for ele in winning_combination])
    while playero_choices not in winning_combination:
        try:
            playero_input = int(input("Player O: Please choose a number from 1 to 9: "))
        except ValueError:
            print("Please enter a number, not a letter. ")
            continue
        if playero_input not in range(1,10):
            print("Please enter a number from 1 to 9. ")
            continue
        if playero_input in playerx_choices or playero_input in playero_choices:
            print("Position already played, please enter a new position. ")
        else:
            playero_choices.append(playero_input)
            empty_board[playero_input] = "O"
            result = max([len(set(playero_choices) & set(ele)) for ele in winning_combination])
            print(display_board(empty_board))
            play_count += 1
            break
        if result == 3:
            print("Player O WINS! ")
            break