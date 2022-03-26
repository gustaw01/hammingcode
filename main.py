class HammingCode:

    number: int
    binary: list
    code: list
    coded: int

    def __init__(self, number):
        self.number = number
        self.binary = []
        self.code = ["x", "x", 0, "x", 0, 0, 0, "x", 0, 0, 0, 0]
        self.coded = 0

    def __str__(self):
        if self.binary:
            return f"{self.binary}"
        return f"{self.number}"

    def to_binary(self):
        while self.number != 0:
            self.binary.append(self.number % 2)
            self.number = int(self.number/2)
        self.binary.reverse()

    def coding(self):
        j = 0
        for i in range(len(self.code)):
            if self.code[i] != "x":
                self.code[i] = self.binary[j]
                j += 1

        def __xor(args: list):
            if args.count(1) % 2 == 0:
                return 0
            return 1

        for i in range(len(self.code)):
            if i == 0:
                self.code[i] = __xor([self.code[2], self.code[4], self.code[6], self.code[8], self.code[10]])
            if i == 1:
                self.code[i] = __xor([self.code[2], self.code[5], self.code[6], self.code[9], self.code[10]])
            if i == 3:
                self.code[i] = __xor([self.code[4], self.code[5], self.code[6], self.code[11]])
            if i == 7:
                self.code[i] = __xor([self.code[8], self.code[9], self.code[10], self.code[11]])


num = HammingCode(154)
print(num)
num.to_binary()
print(num)
print(num.code)
num.coding()
print(num.code)

print(2+8+32+216+512+1024+2048)

