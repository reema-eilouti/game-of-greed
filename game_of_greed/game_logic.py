from random import randint, sample
from collections import Counter 

class GameLogic():
    def __init__(self):
        pass

    
    @staticmethod
    def calculate_score(dice_roll:tuple) -> int:
        """
    Add calculate_score static method to GameLogic class.
    The input to calculate_score is a tuple of integers that represent a dice roll.
    The output from calculate_score is an integer representing the roll’s score according to rules of game.
        """
        score = 0
        counter = 0

        dice_roll_counter_dict = Counter(dice_roll)

        for i in range(1,7):
            if dice_roll_counter_dict[i] == 1:
                counter += 1
            if dice_roll_counter_dict[i] == 2:
                counter += 3
    

        if counter == 6 or counter == 9:
            # Striaght
            score = 1500
            return score

        

        for key in dice_roll_counter_dict:

            if key == 1:
                if dice_roll_counter_dict[key] == 6:
                    # HOT DICE
                    score += 4000
                elif dice_roll_counter_dict[key] == 5:
                    score += 3000
                elif dice_roll_counter_dict[key] == 4:
                    score += 2000
                elif dice_roll_counter_dict[key] == 3:
                    score += 1000
                else:
                    score += dice_roll_counter_dict[key] * 100


            if key == 2:
                if dice_roll_counter_dict[key] == 6:
                    # HOT DICE
                    score += 800
                elif dice_roll_counter_dict[key] == 5:
                    score += 600
                elif dice_roll_counter_dict[key] == 4:
                    score += 400
                elif dice_roll_counter_dict[key] == 3:
                    score += 200


            if key == 3:
                if dice_roll_counter_dict[key] == 6:
                    # HOT DICE
                    score += 1200
                elif dice_roll_counter_dict[key] == 5:
                    score += 900
                elif dice_roll_counter_dict[key] == 4:
                    score += 600
                elif dice_roll_counter_dict[key] == 3:
                    score += 300


            if key == 4:
                if dice_roll_counter_dict[key] == 6:
                    # HOT DICE
                    score += 1600
                elif dice_roll_counter_dict[key] == 5:
                    score += 1200
                elif dice_roll_counter_dict[key] == 4:
                    score += 800
                elif dice_roll_counter_dict[key] == 3:
                    score += 400


            if key == 5:
                if dice_roll_counter_dict[key] == 6:
                    # HOT DICE
                    score += 2000
                elif dice_roll_counter_dict[key] == 5:
                    score += 1500
                elif dice_roll_counter_dict[key] == 4:
                    score += 1000
                elif dice_roll_counter_dict[key] == 3:
                    score += 500  
                else:
                    score += dice_roll_counter_dict[key] * 50


            if key == 6:
                if dice_roll_counter_dict[key] == 6:
                    # HOT DICE
                    score += 2400
                elif dice_roll_counter_dict[key] == 5:
                    score += 1800
                elif dice_roll_counter_dict[key] == 4:
                    score += 1200
                elif dice_roll_counter_dict[key] == 3:
                    score += 600  




        return score

           



    @staticmethod
    def roll_dice(num_dice):
        return tuple(randint(1,6) for _ in range(0,num_dice))
        # or
        # return tuple(sample(range(1, 6 + 1), num_dice))


test = GameLogic()

print(test.calculate_score((2, 2, 3, 3, 4, 6)))