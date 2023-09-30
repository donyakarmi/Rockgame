from logic import print_winner, is_draw, get_computer_choice, get_player_choice


def play_game():

    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    if is_draw(player_choice, computer_choice):
        print("It's a draw, both players picked %s: " % player_choice)
    else:
        print("Computer picked: %s" % computer_choice)
        print("Player picked: %s" % player_choice)
        print_winner(player_choice, computer_choice)


if __name__ == "__main__":
    play_game()


