class RomanNumeral:
    def __init__(self, integer):
        self.integer = integer

    def convert(self):
        roman_numerals = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]

        result = ""
        num = self.integer

        for value, numeral in roman_numerals:
            while num >= value:
                result += numeral
                num -= value

        return result


number = int(input("Enter the number you want to find the Roman numeral of: "))
roman_numeral = RomanNumeral(number)
print(roman_numeral.convert())  
