import random


def split(numbers):
    spl, *others = numbers
    lesseql = []
    greater = []
    for x in range(len(others)):
        if others[x] <= spl:
            lesseql.append(others[x])
        else:
            greater.append(others[x])
    numbers = []
    for x in range(len(lesseql)):
        numbers.append(lesseql[x])
    numbers.append(spl)
    for x in range(len(greater)):
        numbers.append(greater[x])
        

    #################
    # Do not delete return statement
    return numbers


def main():
    numbers = [3, 2, 0, 5, 4]
    # print (id(numbers))
    numbers = split(numbers)
    # print (id(numbers))
    print(numbers)

    numbers = [random.randint(0, 20) for i in range(10)]
    print(numbers)
    numbers = split(numbers)
    print(numbers)


if __name__ == '__main__':
    main()
