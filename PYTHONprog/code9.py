# Match Statement
x = int(input('Enter the value of x: '))

match x:
    case 0:
        print('x is zero')
    case 4:
        print('case is 4')
    case _ if x!=5:
        print(x, 'is not 5')
    case _:
        print(x)