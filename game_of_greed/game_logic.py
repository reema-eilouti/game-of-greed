from random import randint, sample
from collections import Counter

from _pytest.outcomes import skip


class Game():
    def __init__(self, method_roller=None):
        self.method_roller = method_roller or GameLogic.roll_dice

    def play(self, roller=None):
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
            while(True):

                if not skip_roll and not cheater:
                    counter += 1
                    remaining_dice = 6
                    print(f"Starting round {counter}")

                if remaining_dice == 0:
                    remaining_dice = 6

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
                    print(
                        f"Thanks for playing. You earned {test_banker.balance} points")
                    break

                else:
                    dice_to_keep_tuple = tuple(int(num)for num in dice_to_keep)
                    cheater = not test_game.validate_keepers(dice_results_tuple,dice_to_keep_tuple)
                    if cheater :
                        print('Cheater!!! Or possibly made a typo...')
                        continue

                    current_score = test_game.calculate_score(
                        dice_to_keep_tuple)
                    test_banker.shelf(current_score)

                    remaining_dice = remaining_dice - len(dice_to_keep_tuple)
                    print(
                        f'You have {test_banker.shelved} unbanked points and {remaining_dice} dice remaining')
                    print("(r)oll again, (b)ank your points or (q)uit:")
                    roll_or_bank = input("> ")
                    if roll_or_bank == 'b':
                        skip_roll = False
                        print(f'You banked {test_banker.bank()} points in round {counter}')
                        print(f'Total score is {test_banker.balance} points')

                    elif roll_or_bank == 'q':
                        print(
                            f"Thanks for playing. You earned {test_banker.balance} points")
                        break
                    elif roll_or_bank == 'r':
                        skip_roll = True


class GameLogic():
    def __init__(self):
        pass

    @staticmethod
    def calculate_score(dice_roll: tuple) -> int:
        """
    Add calculate_score static method to GameLogic class.
    The input to calculate_score is a tuple of integers that represent a dice roll.
    The output from calculate_score is an integer representing the roll’s score according to rules of game.
        """
        score = 0
        counter = 0

        dice_roll_counter_dict = Counter(dice_roll)

        for i in range(1, 7):
            if dice_roll_counter_dict[i] == 1:
                counter += 1
            if dice_roll_counter_dict[i] == 2:
                counter += 3

        if counter == 6 or counter == 9:
            # Striaght or 3 pairs
            score = 1500
            return score

        for key in dice_roll_counter_dict:

            if dice_roll_counter_dict[key] > 2:
                if key == 1:
                    score += (dice_roll_counter_dict[key]-2) * key * 1000

                else:
                    score += (dice_roll_counter_dict[key]-2) * key * 100

            elif key == 5:
                score += dice_roll_counter_dict[key] * 50

            elif key == 1:
                score += dice_roll_counter_dict[key] * 100

        return score

    @staticmethod
    def roll_dice(num_dice: int) -> tuple:
        """   
    Add roll_dice static method to GameLogic class.
    The input to roll_dice is an integer between 1 and 6.
    The output of roll_dice is a tuple with random values between 1 and 6.
    The length of tuple must match the argument given to roll_dice method.
        """
        return tuple(randint(1, 6) for _ in range(0, num_dice))


    @staticmethod
    def get_scorers(dice_roll:tuple) -> tuple:

        return tuple(filter(lambda number : number == 1 or number == 5 , dice_roll))
                



    @staticmethod
    def validate_keepers(roll , keeper):
        keeper_dict = Counter(keeper)
        roll_dict = Counter(roll)
        for key in keeper_dict:
            if not keeper_dict[key] <= roll_dict[key]:
                return False
            else:
                return True



class Banker:
    def __init__(self):
        self.shelved = 0
        self.balance = 0

    def shelf(self, points: int):
        """        
    Input to shelf is the amount of points (integer) to add to shelf.
    shelf should temporarily store unbanked points.
        """
        self.shelved += points

    def bank(self) -> int:
        """
    bank should add any points on the shelf to total and reset shelf to 0.
    bank output should be the amount of points added to total from shelf.
        """
        added_points = self.shelved
        self.balance += added_points
        self.shelved = 0
        return added_points

    def clear_shelf(self):
        """
        clear_shelf should remove all unbanked points.
        """
        self.shelved = 0


if __name__ == '__main__':
    test = Game()
    test.play()
