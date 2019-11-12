# pyrolldice
Create and roll dice.
You can create a dice object with the desired number of faces.
You can even customize your faces: so instead of numbers you can use wathever string you need.
You can roll your dice just once or multiple times; you can also add a bonus.
For example if you need to roll the dice just once, just call the .roll() method without arguments;
if you need to roll your dice 3 times, call the .roll() method with the argument 3; in order to add a bonus, add a second argument +1
E.G. d6 = Dice(6)
- roll once
d6.roll()
- roll 3 times
d6.roll(3)
- roll 3 times and add a bonus
d6.roll(3,+1)

