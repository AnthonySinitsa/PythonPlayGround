from game_logic import GameLogic

def play():
    print("Welcome to Ten Thousand")
    choice = input("(y)es to play or (n)o to decline\n> ")
    if choice.lower() == 'n':
        print("OK. Maybe another time")
    elif choice.lower() == 'y':
        start_game()
    else:
        print("Invalid choice.")

def bank_or_roll(calc_points, dice_remaining):
    if dice_remaining > 0:
        print(f"You have {calc_points} unbanked points and {dice_remaining} dice remaining")
        print("(r)oll again, (b)ank your points or (q)uit:")
        player_input = input("> ")
        return player_input
    else:
        print(f"You have {calc_points} points and no dice remaining")
        print("(b)ank your points or (q)uit:")
        player_input = input("> ")
        return player_input

def quit_game(total_score):
    print(f"Thanks for playing. You earned {total_score} points")
    quit()

def random_roll(dice_remaining):
    roll_dice = GameLogic.roll_dice(dice_remaining)
    print(roll_dice)
    print("Enter dice to keep, or (q)uit:")
    player_input = input("> ")
    if player_input == "q":
        quit_game()
    else:
        selected_dice = tuple(int(dice) for dice in player_input.split())
        remaining_dice = tuple(dice for dice in roll_dice if dice not in selected_dice)
        return selected_dice, remaining_dice


def start_game():
    total_score = 0
    calc_points = 0
    round = 1
    dice_leftovers = 6

    while True:
        selected_dice, dice_remaining = random_roll(dice_leftovers)
        dice_leftovers -= len(selected_dice)
        calc_points += GameLogic.calculate_score(format_player_input(selected_dice))
        total_score += calc_points
        player_input = bank_or_roll(calc_points, dice_leftovers)
        if player_input == "b":
            print(f"You banked {calc_points} points in round {round}")
            print(f"Total score is {total_score} points")
            round += 1
            calc_points = 0
            print(f"Starting round {round}\nRolling {dice_leftovers} dice...")
            continue
        if player_input == "r":
            if if_farkled(dice_remaining):
                calc_points = 0
                round += 1
                print(f"Starting round {round}\nRolling {dice_leftovers} dice...")
                continue
        if dice_leftovers == 0:
            print("Sorry, no rolls left")
            calc_points = 0
            round += 1
            dice_leftovers = 6
            print(f"Starting round {round}\nRolling {dice_leftovers} dice...")
            continue
        if player_input == "q":
            quit_game(total_score)
        else:
            unbanked_points_message(round, total_score, calc_points, dice_leftovers)



def format_player_input(player_input_string):
    int_list = []
    for i in range(len(player_input_string)):
        int_list.append(int(player_input_string[i]))
    return int_list

def if_farkled(dice):
    dice_list = list(map(int, dice))  # Convert each element to an integer
    if 1 in dice_list or 5 in dice_list or GameLogic.calculate_score(dice_list) == 0:
        print("Farkle!")
        print("You lost all your unbanked points.")
        return True
    else:
        return False



def unbanked_points_message(round_num, total_score, calc_points, dice_left):
    print(f"You have {calc_points} unbanked points and {dice_left} dice remaining")

if __name__ == "__main__":
    play()
