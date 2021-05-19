from random import randint, sample
from collections import Counter

from _pytest.outcomes import skip

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

        dice_roll_dict = Counter(dice_roll)

        results = []
        counter = 0
        
        for i in range(1, 7):
            if dice_roll_dict[i] == 1:
                counter += 1
            if dice_roll_dict[i] == 2:
                counter += 3

        if counter == 6 or counter == 9:
            # Striaght or 3 pairs
            return dice_roll

        for key in dice_roll_dict:
            if key == 1 or key == 5:
                for i in range(dice_roll_dict[key]):
                    results.append(key)

            elif dice_roll_dict[key] >= 3:
                for i in range(dice_roll_dict[key]):
                    results.append(key)
        
        return tuple(results)
                



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



