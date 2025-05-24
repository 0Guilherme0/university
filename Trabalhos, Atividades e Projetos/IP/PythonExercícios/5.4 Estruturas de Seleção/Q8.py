""" Write a program that prints a user’s grade given a percent of points
achieved in the class. The program should prompt the user to enter
his/her percent of points. It should then print a letter grade A, A−, B+, B,
B−, C+, C, C−, D+, D, D−, F.
The grading scale is given in Fig. 2 . Use exception handling to check the
input from the user to be sure it is valid. Running the program should
look like this:
Please enter your percentage achieved in the class: 92.32
You earned an A- in the class. """

score = float(input('Please enter your percentage achieved in the class: '))
gradscale  = None
if score >= 0 and score < 60:
    gradscale  = 'F'
elif score >= 60 and score < 63.33:
    gradscale  = 'D-'
elif score >= 63.33 and score < 66.67:
    gradscale  = 'D'
elif score >= 66.67 and score < 70:
    gradscale  = 'D+'
elif score >= 70 and score < 73.33:
    gradscale >= 'C-'
elif score >= 73.33 and score < 76.67:
    gradscale = 'C'
elif score >= 76.67 and score < 80:
    gradscale = 'C+'
elif score >= 80 and score < 83.33:
    gradscale = 'B-'
elif score >= 83.33 and score < 86.67:
    gradscale = 'B'
elif score >= 86.67 and score < 90:
    gradscale = 'B+'
elif score >= 90 and score < 93.33:
    gradscale = 'A-'
elif score >= 93.33 and score <= 100:
    gradscale = 'A'
elif score > 100:
    print('Invalid score')

print('You earned a(n)',gradscale,' in the class')