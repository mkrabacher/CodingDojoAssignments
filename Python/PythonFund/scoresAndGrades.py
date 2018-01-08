import random

def sAndGs():
    print 'Scores and Grades'
    for stu in range(0, 10):
        score = random.randint(60, 100)
        if score < 60:
            grade = 'F'
        elif score < 70:
            grade = 'D'
        elif score < 80:
            grade = 'C'
        elif score < 90:
            grade = 'B'
        elif score <= 100:
            grade = 'A'
        else:
            grade = 'you being a big fat cheater'
        print 'Score: {}; Your grade is {}'.format(score, grade)

sAndGs()