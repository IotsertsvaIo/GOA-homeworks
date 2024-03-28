def print_nums(num1, num2) :
    print(num1 + num2)
    print(num1 - num2)
    print(num1 * num2)
    print(num1 / num2)

print_nums(78, 34)



def print_rectangle(number1, number2) :
        print(number1 * number2) 

print_rectangle(13, 2)


def print_rectangle_perimeter(num1, num2, num3, num4) :
    print(num1 + num2 * 2)

print_rectangle_perimeter(7, 24 ,7 ,24)




def summation(listn) :
    num = 0
    for i in listn:
        num += num
        print(summation)

summation([2, 4, 7])



def max_founder(listn) :
    if listn[0] > listn[1] and listn[0] > listn[2]:
        print("max number is: " + str(listn[0]))
    elif listn[1] > listn[0] and listn[1] > listn[2]:
        print("max number is: " + str(listn[1]))
    else:
         print("max number is: " + str(listn[2]))


max_founder(4, 78 , -90)




def min_founder(listn) :
    if listn[0] < listn[1] and listn[0] < listn[2]:
        print("min number is: " + str(listn[0]))
    elif listn[1] < listn[0] and listn[1] < listn[2]:
        print("min number is: " + str(listn[1]))
    else:
         print("min number is: " + str(listn[2]))


min_founder(4, 78 , -90)


    
