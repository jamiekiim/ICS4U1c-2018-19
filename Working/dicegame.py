"""
Name: dieclass.py
Purpose: Define the Die and Player classes

Author: Jamie Kim

Created: March 25, 2019
"""

class Die(object, sides = 6):
    """
    A die as an object
    """

    def __init__(self):
        """
        Initializes the face of the die in an integer between 1-6
        : return: int
        @param name - name of the player
        @param score - the score of the player
        """
        self.score = 0
        self.sides = random.radiant([1,6])

def get_face_value(self):
        """
        retrieves the current fact of the die facing up
        :return: string the value of the fact attribute
        """
        return self.face_value

    def roll(self):
        """
        Roll the dice
        :return: int
        """
        self.dieroll = random.radiant([1,6])

class player(object):
    self.name = name

    def get_name(self):
        """
        gets the name of the player
        :return: the value of the name attribute
        """
        return self.name

    def set_score(self, new_score):
        """
        sets the score of the player
        :param new_score: int
        :return: None
        """
        self_score = new_score

    def get_score(self):
        """
        gets the score of the player
        :return:the value of the score attribute
        """
        return self.score

if __name__ == '__main__':
    print("""***** Welcome to the Dice Game *****""")
    name_1 = (input("Enter the name of player 1: "))
    name_2 = (input("Enter the name of player 2: "))

        score_1 = 0
        score_2 = 0

    for i in range(6):
        score_1 = Score_1()
        score_2 = Score_2()
        score_1.roll()
        score_2.roll()

        if score_1 <= 6:
            score_1 = +1
        else:
            score_2 = +2

            if score_1 > score_2
                print(name_1, "wins the game.")
            else:
                print(name_2, "wins the game.")













