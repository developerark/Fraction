class Fraction:
    @classmethod
    def __GCD(cls, a, b):
        if (a == 0):
            return b
        return cls.__GCD(b % a, a)

    def __init__(self, numerator, denominator):
        self.__numerator = numerator
        self.__denominator = denominator
    
    # '+' operator overload
    def __add__(self, other):
        return Fraction(self.__numerator * other.__denominator + self.__denominator * other.__numerator, self.__denominator * other.__denominator) 

    # '-' operator overload
    def __sub__(self, other):
        return Fraction(self.__numerator * other.__denominator - self.__denominator * other.__numerator, self.__denominator * other.__denominator)

    # '*' operator overload
    def __mul__(self, other):
        return Fraction(self.__numerator * other.__numerator, self.__denominator * other.__denominator)

    # '/' operator overload
    def __truediv__(self, other):
        return Fraction(self.__numerator * other.__denominator, self.__denominator * other.__numerator)

    # String representation of the Fraction
    def __str__(self):
        return "{}/{}".format(self.__numerator, self.__denominator)
    
    # Reduces self
    def reduce(self):
        GCD = Fraction.__GCD(self.__numerator, self.__denominator)
        self.__numerator //= GCD
        self.__denominator //= GCD

    # Returns a new reduced Fraction
    def reduced(self):
        GCD = Fraction.__GCD(self.__numerator, self.__denominator)
        return Fraction(self.__numerator // GCD, self.__denominator // GCD)

if __name__ == "__main__":
    f1 = Fraction(2, 4)
    f2 = Fraction(2, 5)
    print(f1 + f2)
    print(f1 - f2)
    print(f1 * f2)
    print(f1 / f2)
    print(f1.reduced())
    f1.reduce()
    print(f1)
