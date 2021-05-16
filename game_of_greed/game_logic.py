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
    def roll_dice(num_dice:int)->tuple:
        """   
    Add roll_dice static method to GameLogic class.
    The input to roll_dice is an integer between 1 and 6.
    The output of roll_dice is a tuple with random values between 1 and 6.
    The length of tuple must match the argument given to roll_dice method.
        """
        return tuple(randint(1,6) for _ in range(0,num_dice))


class Banker:
    def __init__(self):
        self.shelved = 0
        self.balance = 0
    def shelf(self,points:int):
        """        
    Input to shelf is the amount of points (integer) to add to shelf.
    shelf should temporarily store unbanked points.
        """
        self.shelved += points

    def bank(self)->int:
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


test = GameLogic()

print(test.roll_dice(5))