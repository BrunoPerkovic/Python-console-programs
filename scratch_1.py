import random

empty_board = [""] * 10
winning_combination = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
play_limit = 9
game_on = True


def display_board(board):
    print(board[7] + ' I ' + board[8] + ' I ' + board[9])
    print(board[4] + ' I ' + board[5] + ' I ' + board[6])
    print(board[1] + ' I ' + board[2] + ' I ' + board[3])            #funkcija koja prikazuje ploču


def coin_toss():                                                     #funkcija koja simulira bacanje novcica, pismo ili glava
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


def player_sign():                                                   #funkcija koja na temelju funkcije coin_toss traži od korisnika da odabere svoj simbol za igru
    player = coin_toss()
    print("First pick: " + player)
    first_player_sign = input("Please choose X or O: ").upper()
    while first_player_sign not in ["X", "O"]:
        first_player_sign = input("Please choose X or O: ").upper()
    if first_player_sign == "X":
        choices = (first_player_sign, "O")
        return choices
    else:
        choices = (first_player_sign, "X")
        return choices


def player_choice(player_symbol, current_player_picks, other_player_picks):  #funkcija koja traži od korisnika da unese broj polja na koji želi staviti svoj simbol, provjerava ispravnost unosa i stavlja simbol na ploču
    player_input = 0
    while player_input not in range(1, 10):
        try:
            player_input = int(input("Please choose a number from 1 to 9: "))
        except ValueError:
            print("Please enter a number, not a letter. ")
        if player_input not in range(1, 10):
            print("Please enter a number from 1 to 9. ")
        if player_input in current_player_picks or player_input in other_player_picks:
            print("Position already played, please enter a new position. ")
        else:
            current_player_picks.append(player_input)
            empty_board[player_input] = player_symbol
        display_board(empty_board)
        return current_player_picks


def win_check(choices):                                                   #funkcija koja provjerava pobjednika
    for ele in winning_combination:
        winning_intersect = set(choices) & set(ele)
        if len(winning_intersect) == 3:
            print("YOU WIN! Congratulations.")
            return True
    return False


def full_board(play_count):                                             #funkcija koja provjerava punu ploču bez pobjednika
    if play_count == play_limit:
        print("DRAW! ")
        return True
    else:
        return False


def main_game():                                                        #funkcija koja sadrži glavni blok koda u kojem se izvršva sve prethodno navedeno
    (first_player, second_player) = player_sign()
    print(first_player + " is going first")
    print(second_player + " is going second")
    first_player_choices = {first_player: []}
    second_player_choices = {second_player: []}
    play_count = 0

    turn = first_player

    while game_on:
        symbol = first_player
        first_choices = first_player_choices[first_player]
        second_choices = second_player_choices[second_player]
        first_player_choices[first_player] = player_choice(symbol, first_choices, second_choices)
        print(first_player_choices[first_player])
        play_count += 1
        if win_check(first_player_choices[first_player]):
            break
        if full_board(play_count):
            break
        else:
            symbol = second_player
            second_player_choices[second_player] = player_choice(symbol, second_choices, first_choices)
            print(second_player_choices[second_player])
            play_count += 1
            if win_check(second_player_choices[second_player]):
                break
            if full_board(play_count):
                break
            else:
                continue


def play_tictactoe():                                                  #funkcija koja pita korisnika želi li igrati i igrati opet
    play_again = input("Do you want to play? Yes or No: ").lower().startswith("y")
    while play_again:
        main_game()
        play_again = input("Do you want to play again? Yes or No: ").lower().startswith("y")
    print("Bye! ")

play_tictactoe()
