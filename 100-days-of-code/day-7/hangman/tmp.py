import random
import stages

def draw_hangman(life):
    match life:
        case 1:
            print(stages.stages[0])
        case 2:
            print(stages.stages[1])
        case 3:
            print(stages.stages[2])
        case 4:
            print(stages.stages[3])
        case 5:
            print(stages.stages[4])
        case 6:
            print(stages.stages[5])
        case 7:
            print(stages.stages[6])

life = 7
for i in range(7):
    draw_hangman(i)
