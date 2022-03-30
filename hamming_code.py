def to_binary(number):
    binary = []
    while number != 0:
        binary.append(number % 2)
        number = int(number/2)
    binary.reverse()
    return binary


def to_decimal(binary):
    binary.reverse()
    number = 0
    j = 0
    for i in binary:
        if i == 1:
            number += 2**j
        j += 1
    return number


def code(num: int):
    control_bits = []
    coded = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    bnum = to_binary(num)
    bnum.reverse()
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

    def __XOR(*args):
        ones = args.count(1)
        if ones % 2 != 0:
            return 1
        return 0

    for i in range(len(coded)):
        if i == 0:
            coded[i] = __XOR(bnum[0], bnum[1], bnum[3], bnum[4], bnum[6])
            control_bits.append(coded[i])
        elif i == 1:
            coded[i] = __XOR(bnum[0], bnum[2], bnum[3], bnum[5], bnum[6])
            control_bits.append(coded[i])
        elif i == 3:
            coded[i] = __XOR(bnum[1], bnum[2], bnum[3], bnum[7])
            control_bits.append(coded[i])
        elif i == 7:
            coded[i] = __XOR(bnum[4], bnum[5], bnum[6], bnum[7])
            control_bits.append(coded[i])

    return to_decimal(coded), control_bits


coded_number, control_bits = code(154)

print(coded_number)
print(control_bits)

