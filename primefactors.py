# Python program to print the prime factor of a number so either way there is an output for number
# If the number itself is prime, print PRIME

num = int(input("Input number: "))

divisor = 2
factors = []

while num > 1:
    if num % divisor == 0:
        factors.append(divisor)
        num = num // divisor
    else:
        divisor += 1

if len(factors) == 1:
    print("PRIME")
else:
    output = ""
    for f in factors:
        output = output + str(f) + " "
    print(output)