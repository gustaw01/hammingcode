def to_binary(number):
    binary = []
    while number != 0:
        binary.append(number % 2)
        number = int(number/2)
    binary.reverse()
    return binary


def code(num: int):
    coded = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    bnum = to_binary(num)
    bnum.reverse()
    print(len(bnum))
    # kolejne potęgi 2
    k = 0
    # iterator kodowanej liczby
    j = 0
    for i in range(1, len(coded)+1):
        # sprawdzenie czy liczba nie jest k-tą potęgą 2
        if i != 2**k and j < len(bnum):
            coded[i-1] = bnum[j]
            j += 1
        else:
            k += 1
    print(bnum)
    print(coded)


