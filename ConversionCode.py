# -------------------------Number to Word Conversion--------------------------------------#
# ----------------------------------------------------------------------------------------#
# Function to convert single digit or two digit number into words
def convertToDigitCash(n, suffix):
    # if n is zero
    if n == 0:
        return ""

    # split n if it is more than 19
    if n > 19:
        return Twenties[n // 10] + Ones[n % 10] + suffix
    else:
        return Ones[n] + suffix


def convertToDigitPhone(n):
    if n == 0:
        return ""
    # split n if it is more than 19
    if n > 19:
        return Twenties[n // 10] + Ones[n % 10]
    else:
        return Ones[n]


def num2Word(num, symbol):
    n = int(num)
    result = ""
    if (symbol != '+'):  # For Cash
        # add digits at ten millions & hundred millions place
        result = convertToDigitCash((n // 1000000000) % 100, "Billion ")

        # add digits at ten millions & hundred millions place
        result += convertToDigitCash((n // 10000000) % 100, "Crore ")

        # add digits at hundred thousands & one millions place
        result += convertToDigitCash(((n // 100000) % 100), "Lakh ")

        # add digits at thousands & tens thousands place
        result += convertToDigitCash(((n // 1000) % 100), "Thousand ")

        # add digit at hundreds place
        result += convertToDigitCash(((n // 100) % 10), "Hundred ")

        if n > 100 and n % 100:
            result += "and "
    else:  # For Phone number

        result = "Plus "
        result += convertToDigitPhone((n // 100000000000) % 100)
        # add digits at ten millions & hundred millions place
        result += convertToDigitPhone((n // 1000000000) % 100)

        # add digits at ten millions & hundred millions place
        result += convertToDigitPhone((n // 10000000) % 100)

        # add digits at hundred thousands & one millions place
        result += convertToDigitPhone(((n // 100000) % 100))

        # add digits at thousands & tens thousands place
        result += convertToDigitPhone(((n // 1000) % 100))

        # add digit at hundreds place
        result += convertToDigitPhone(((n // 100) % 10))

        if n > 100 and n % 100:
            result += "and "

    # add digits at ones & tens place
    result += convertToDigitCash((n % 100), "")

    # adding currency type

    if symbol == '' or symbol == '+' or "None":
        result += ""
    else:
        result += " " + str(Symbol.get(symbol))
    return result


# -------------------------Word to Number Conversion--------------------------------------#
# ----------------------------------------------------------------------------------------#

def word2Num(num):
    result = ""
    ones = {'zero': 0,
            'one': 1, 'eleven': 11,
            'two': 2, 'twelve': 12,
            'three': 3, 'thirteen': 13,
            'four': 4, 'fourteen': 14,
            'five': 5, 'fifteen': 15,
            'six': 6, 'sixteen': 16,
            'seven': 7, 'seventeen': 17,
            'eight': 8, 'eighteen': 18,
            'nine': 9, 'nineteen': 19}

    # a mapping of digits to their names when they appear in the 'tens'
    # place within a number group
    tens = {'ten': 10,
            'twenty': 20,
            'thirty': 30,
            'forty': 40,
            'fifty': 50,
            'sixty': 60,
            'seventy': 70,
            'eighty': 80,
            'ninety': 90}

    # an ordered list of the names assigned to number groups
    groups = {'thousand': 1000,
              'million': 1000000,
              'billion': 1000000000,
              'trillion': 1000000000000}

    Symbol2Word = {"Dollar": '$',
                   "pence": 'p',
                   "pounds": '£',
                   "plus": '+'}

    # initializing string
    test_str = num
    # checking word from list in Dictionary and obtaining Value
    for word in test_str:
        if word in ones:
            result += str(ones.get(word))
        if word in tens:
            result += str(tens.get(word))
        if "-" in word:
            half = word.split('-')
            num1 = tens.get(half[0])
            num2 = ones.get(half[1])
            data = num1 + num2
            result += str(data)
        if word in Symbol2Word:
            result += Symbol2Word.get(word)

    return result


# --------------------------------------------------------------------------------------------#


def ReadFile():
    with open(r"C:\Users\User\Downloads\TestCase.txt", "r+") as file_in:  # loading File Data from file
        for line in file_in:
            line = line.strip('\n')
            line = line.strip('Â')
            lines.append(line)


def WriteFile(Result):
    with open(r"C:\Users\User\Downloads\Result.txt", "a+") as f:
        f.writelines(Result + '\n')
        f.closed



# -------------------------------------------------------------------------------#
Ones = ["", "One ", "Two ", "Three ", "Four ", "Five ", "Six ",
        "Seven ", "Eight ", "Nine ", "Ten ", "Eleven ", "Twelve ",
        "Thirteen ", "Fourteen ", "Fifteen ", "Sixteen ",
        "Seventeen ", "Eighteen ", "Nineteen "]

Twenties = ["", "", "Twenty ", "Thirty ", "Forty ", "Fifty ",
            "Sixty ", "Seventy ", "Eighty ", "Ninety "]
Symbol = {'$': "Dollar",
          'p': "pence ",
          '£': "pound",
          '+': "plus"}

word = []
lines = []
ReadFile()

for line in lines:

    if line.isnumeric() or line[0] in Symbol:
        symbol = line[0]
        line = line[1:]  # obtaining and removing Cash symbol from line
        result = num2Word(line, symbol)
        WriteFile(result)  # writing in file

    else:
        line = line.lower()

        if "and" in line:    # Splitting String in Word by word
            word = line.split(' ')
            result = word2Num(word)
            WriteFile(result) # writing in file

        if "," in line:  # Splitting String in Word by word
            word = line.split(',')
            result = word2Num(word)
            WriteFile(result) # writing in file
