""" Write a program that converts centimeters to yards, feet, and inches.
There are 2.54cm in an inch. You can solve this problem by doing
division, multiplication addition, and subtraction. Converting a float to an
int at the appropriate time will help in solving this problem. When you run
the program it should look exactly like this (except possibly for decimal
places in the inches):

How many centimeters do you want to convert? 127.25
This is 1 yard , 1 foot , 2.098425 inches.

In this version of it you should print “yard” when there is one yard, and
“yards” when there is more than one yard. If there are zero yards then it
should not print “yard” or “yards”. The same thing applies to “feet”. Use
an if statement to determine the label to print and if the label should be
printed at all. """

cent = float(input('How many centimeters do u wanna convert? '))
yard = int(cent/91.44)
foot = int(cent/30.48)
inch = cent/2.54
yplural = None
fplural = None

if yard > 1:
    yplural = str('yards')
else:
    yplural = str('yard')

if foot > 1:
    fplural = str('feet')
else:
    fplural = str('foot')

print('This is {0} {1}, {2} {3} and {4} inches. '.format(yard,yplural,foot,fplural,inch))