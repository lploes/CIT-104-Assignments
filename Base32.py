# Base-32 to Octal Converter
# Base 32 and octal don't line up digit for digit (5 bits vs 3 bits),
# so I go through binary in the middle:
#   1. Turn each base-32 digit into 5 bits using a dictionary
#   2. Add zeros on the left until the number of bits divides evenly by 3
#   3. Turn each group of 3 bits into one octal digit using a second dictionary

base32_to_bits = {
    "0": "00000", "1": "00001", "2": "00010", "3": "00011",
    "4": "00100", "5": "00101", "6": "00110", "7": "00111",
    "8": "01000", "9": "01001", "A": "01010", "B": "01011",
    "C": "01100", "D": "01101", "E": "01110", "F": "01111",
    "G": "10000", "H": "10001", "I": "10010", "J": "10011",
    "K": "10100", "L": "10101", "M": "10110", "N": "10111",
    "O": "11000", "P": "11001", "Q": "11010", "R": "11011",
    "S": "11100", "T": "11101", "U": "11110", "V": "11111"
}

bits_to_octal = {
    "000": "0", "001": "1", "010": "2", "011": "3",
    "100": "4", "101": "5", "110": "6", "111": "7"
}

base32_number = input("Enter a base-32 number: ")
base32_number = base32_number.upper()

# Step 1: build one long string of bits, 5 bits for every base-32 digit
bits = ""
for digit in base32_number:
    bits = bits + base32_to_bits[digit]

# Step 2: add zeros on the left until the length divides evenly by 3
while len(bits) % 3 != 0:
    bits = "0" + bits

# Step 3: take the bits 3 at a time and look up each octal digit
octal_number = ""
position = 0
while position < len(bits):
    group = bits[position] + bits[position + 1] + bits[position + 2]
    octal_number = octal_number + bits_to_octal[group]
    position = position + 3

# Remove extra zeros on the left (keep one 0 if the answer is zero)
octal_number = octal_number.lstrip("0")
if octal_number == "":
    octal_number = "0"

print("Octal:", octal_number)