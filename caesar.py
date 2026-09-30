# Modified Caesar Cipher
# Reads a quote from quote.txt and asks the user for an offset (1-20).
# Unlike a standard Caesar cipher, the offset increases in a repeating
# pattern of three: 1st character uses offset, 2nd uses offset+1,
# 3rd uses offset+2, then the pattern repeats.

input_file = open("quote.txt", "r")
plain_text = input_file.read()
input_file.close()

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

offset = 0
while offset < 1 or offset > 20:
    entry = input("Enter an offset between 1 and 20: ")
    if entry.isdigit():
        offset = int(entry)
    else:
        offset = 0
    if offset < 1 or offset > 20:
        print("Invalid input. Enter a number from 1 to 20.")

encrypted_text = ""
position = 0

for ch in plain_text:

    if position % 3 == 0:
        shift = offset
    elif position % 3 == 1:
        shift = offset + 1
    else:
        shift = offset + 2

    if ch in lowercase:
        old_spot = lowercase.find(ch)
        new_spot = old_spot + shift
        new_spot = new_spot % 26
        new_letter = lowercase[new_spot]
        encrypted_text = encrypted_text + new_letter
    elif ch in uppercase:
        old_spot = uppercase.find(ch)
        new_spot = old_spot + shift
        new_spot = new_spot % 26
        new_letter = uppercase[new_spot]
        encrypted_text = encrypted_text + new_letter
    else:
        encrypted_text = encrypted_text + ch

    position = position + 1

print(encrypted_text)
output_file = open("encrypted.txt", "w")
output_file.write(encrypted_text)
output_file.close()