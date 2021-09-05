#lesson 57
'''
def piska():
    print("Hello")
    print("Bye")

piska()


def turn_left_3():
    turn_left()
    turn_left()
    turn_left()

def butterfly():
    turn_left()
    move()
    turn_left_3()
    move()
    turn_left_3()
    move()
    turn_left_3()
    move()
    turn_left_3()

butterfly()

'''

#lesson58
'''
def turn_right():
    for left in range(3):
        turn_left()

def one_circle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for circle in range(6):
    one_circle()
'''

#lesson60



def turn_right():
    for left in range(3):
        turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    jump()
#    number_of_hurdles = number_of_hurdles + 1
#    print(number_of_hurdles)

#lesson61


'''
def turn_right():
    for left in range(3):
        turn_left()

def jump():
    #    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    if front_is_clear() == True:
        move()
    elif wall_in_front() == True:
        jump()


#lesson62
def turn_right():
    for left in range(3):
        turn_left()

def jump():
    while front_is_clear() == True:
        move()

        if right_is_clear() == True:
            turn_right()
            move()
            turn_right()


while not at_goal():
    if front_is_clear() == True:
        move()
    elif wall_in_front() == True:
        turn_left()
        jump()
        
'''

#lesson63
def turn_right():
    for left in range(3):
        turn_left()

def jump():
    while front_is_clear() == True:
        move()

        if right_is_clear() == True and at_goal() != True:
            turn_right()
            move()
            turn_right()


while not at_goal():
    if front_is_clear() == True:
        move()
    elif wall_in_front() == True:
        turn_left()
        jump()
