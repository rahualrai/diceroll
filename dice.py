import random

print('Welcome. This Is a Dice Rolling Simulator!')

while True:
    try:
        n = int(input('Number Of Rolls: '))
        break
    except ValueError:
        print("     Input Must Be A Number!")

lis = []
for i in range(1, n+1):
    print('-'*27)
    print('This Is Roll No.{}'.format(str(i)))
    while True:
        try:
            l = int(input('Number Of Faces of Die: '))
            n = 1/l
            break
        except ValueError:
            print("     Input Must Be A Number!")
        except ZeroDivisionError:
            print('     Number Cannot Be Zero!')
    roll = random.randint(1, l)
    print('Your Number Is {}!'.format(roll))
    lis.append(roll)


print('-'*27)
nis = enumerate(lis)
for i, n in nis:
    print('Roll Number {} is {}'.format(str(i+1), str(n)))
print('-'*27)
