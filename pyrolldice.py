# Dice
from random import choice
import matplotlib.pyplot as plt

class Dice:
    """
    An object dice with a roll method that return a random number.
    You can create any type of dice, even with custom faces.
    You can roll your dice just once or multiple times; you can also add a bonus.

    Args:
        num   - number of dice's faces (required)
        times - number of rolls of the same dice (optional)
        bonus - a positive/negative number that modifies the dice's roll (optional)
        show  - if True show the single results of a multiple roll (default False)

    Return:
        A random number from the set defined by the dice's type

    """

    __slots__ = ['num', 'faces']

    _shapes = {4:'Tetrahedron',
              6:'Cube',
              8:'Octahedron',
             10:'Pentagonal trapezohedron',
             12:'Dodecahedron',
             20:'Icosahedron',
             100:'Zocchihedron'}

    _num_roll_test = 15000

    def __init__(self, num):
        self.num = num
        self.faces = [i for i in range(1,self.num+1)]

    def roll(self, times =1,  bonus = 0, show=False):
        rolls = [choice( self.faces) for t in range(times)]
        if show:
            print(rolls)
        try:
            out = sum(rolls) + bonus
        except TypeError:
            out = rolls
        return out

    def showstats(self):
        rolls = [self.roll() for i in range(self._num_roll_test) ]
        plt.hist(rolls)
        plt.show

    def __repr__(self):
        return "Dice({})".format(self.num)

    def __str__(self):
        try:
            show = 'Dice #{}: {}\n'.format(self.num, self._shapes[self.num])
        except KeyError:
            show = 'Dice #{}: unknown\n'.format(self.num)
        show += ' '.join([str(f) for f in self.faces])
        return show

    def __add__(self, other):
        return self.roll() + other.roll()

    @staticmethod
    def full_dice_set():
        return (Dice(i) for i in (1,4,6,8,10,12,20,100))

    @staticmethod
    def copynpaste():
        print('d1,d4, d6, d8, d10, d12, d20, d100 = rollDice.full_dice_set()')

    @classmethod
    def set_stats_rolls(cls, num):
        cls._num_roll_test = num

    @property
    def avg(self):
        return sum(range(1,self.num+1))/self.num

class customDice(Dice):
    def __init__(self, num, faces):
        super().__init__(num)
        self.faces = faces
        assert len(self.faces) == self.num, "\nThe number of faces and the entered list have a DIFFERENT LENGTH"

    def set_faces(self, new_faces):
        self.faces = new_faces[:]
