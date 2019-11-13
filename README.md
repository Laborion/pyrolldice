# pyrolldice
Create and roll your dice.
You can create a dice object with the desired number of faces.
You can even customize your faces: so instead of numbers you can use wathever string you need, using customDice subclass.
It has is own add method, so you can directly add up two dices.

You can roll your dice just once or multiple times; you can also add a bonus.
For example if you need to roll the dice just once, just call the .roll() method without arguments;
if you need to roll your dice 3 times, call the .roll() method with the argument 3; in order to add a bonus +1, add a second argument +1.
Type .roll(bonus= +1) in order to add just the bonus.   

E.G. d6 = Dice(6)
- roll once: d6.roll()
- roll 3 times: d6.roll(3)
- roll 3 times and add a bonus: d6.roll(3,+1)

### todo list
1. documentation
