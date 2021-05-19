from game_of_greed.game_logic import GameLogic, Banker

class Game():
    def __init__(self, method_roller=None):
        self.method_roller = method_roller or GameLogic.roll_dice

    @classmethod
    def play(cls, roller=None):
        
        roller = roller or GameLogic.roll_dice
        counter = 0
        skip_roll = False
        cheater = False

        print("Welcome to Game of Greed")

        print("(y)es to play or (n)o to decline")
        play_answer = input("> ")

        if play_answer == 'n':
            print("OK. Maybe another time")

        elif play_answer == 'y':
            test_game = GameLogic()
            test_banker = Banker()
# test_banker.balance <= 10000 or 
            while(counter <= 10):

                if not skip_roll and not cheater:
                    counter += 1
                    remaining_dice = 6
                    print(f"Starting round {counter}")

                

                if not cheater:
                    print(f"Rolling {remaining_dice} dice...")

                    dice_results_tuple = roller(remaining_dice)

                    dice_results = ' '.join(map(str, dice_results_tuple))



                zilcher = test_game.calculate_score(dice_results_tuple)

                print(f"*** {dice_results} ***")

                if zilcher == 0:
                    print("""****************************************
**        Zilch!!! Round over         **
****************************************""")
                    
                    print(f'You banked 0 points in round {counter}')

                    print(f'Total score is {test_banker.balance} points')

                    skip_roll = False

                    continue
                
                
                print("Enter dice to keep, or (q)uit:")

                dice_to_keep = input("> ").replace(' ', '')

                if dice_to_keep == 'q':
                    print(f"Thanks for playing. You earned {test_banker.balance} points")
                    break

                elif not dice_to_keep.isdigit():
                    print(f"Thanks for playing. You earned {test_banker.balance} points")
                    break

                else:
                    dice_to_keep_tuple = tuple(int(num)for num in dice_to_keep)

                    cheater = not test_game.validate_keepers(dice_results_tuple,dice_to_keep_tuple)

                    if cheater :
                        print('Cheater!!! Or possibly made a typo...')
                        continue

                    current_score = test_game.calculate_score(dice_to_keep_tuple)
                    test_banker.shelf(current_score)

                    remaining_dice = remaining_dice - len(dice_to_keep_tuple)
                    print(f'You have {test_banker.shelved} unbanked points and {remaining_dice} dice remaining')

                    

                    print("(r)oll again, (b)ank your points or (q)uit:")

                    roll_or_bank = input("> ")

                    if roll_or_bank == 'b':
                        skip_roll = False
                        print(f'You banked {test_banker.bank()} points in round {counter}')
                        print(f'Total score is {test_banker.balance} points')

                    elif roll_or_bank == 'q':
                        print(f"Thanks for playing. You earned {test_banker.balance} points")
                        break

                    elif roll_or_bank == 'r' and remaining_dice != 0:
                        skip_roll = True
                        

            else:
                print(f"Thanks for playing. You earned {test_banker.balance} points")
                


if __name__ == '__main__':
    test = Game()
    test.play()