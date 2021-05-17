from random import randint, sample
from collections import Counter

class Game():
    def __init__(self, method_roller=None):
        self.method_roller = method_roller or GameLogic.roll_dice

    def play(self):
        counter = 0

        print("Welcome to Game of Greed")
        play_answer = input("Wanna play?")
        if play_answer == 'n':
            print("OK. Maybe another time")
        elif play_answer == 'y':
            test_game = GameLogic()

            test_banker = Banker()
            while(True):
                counter += 1
                print(f"Starting round {counter}")
                print("Rolling 6 dice...")

                dice_results = ','.join(map(str, self.method_roller(6)))
                print(dice_results)

                dice_to_keep = input("Enter dice to keep (no spaces), or (q)uit: ")
                
                if dice_to_keep == 'q':
                    print(f"Total score is {test_banker.balance} points")
                    print(f"Thanks for playing. You earned {test_banker.balance} points")
                    break

                else:
                    dice_to_keep_tuple = tuple( int(num) for num in dice_to_keep )   
                    current_score = test_game.calculate_score(dice_to_keep_tuple)
                    test_banker.shelf(current_score)

                    remaining_dice = 6-len(dice_to_keep_tuple)
                    print (f'You have {current_score} unbanked points and {remaining_dice} dice remaining')
                    roll_or_bank = input('(r)oll again, (b)ank your points or (q)uit ')
                    if roll_or_bank == 'b':
                        print(f'You banked {test_banker.bank()} points in round {counter}')
                        print(f'Total score is {test_banker.balance} points')
                    
                    elif roll_or_bank == 'q':
                        print(f"Total score is {test_banker.balance} points")
                        print(f"Thanks for playing. You earned {test_banker.balance} points")
                        break
                    elif roll_or_bank == 'r':
                        continue



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