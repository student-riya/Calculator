#Taking input from user
decimal_number=int(input("Enter a decimal number:"))
#Converting to binary
binary=""
num=decimal_number
while num > 0:
    remainder=num%2
    binary = str(remainder)+ binary
    num=num//2
binary="0"
    if binary=="":
        else binary  #In case the number is 0
#Converting to octal
octal=""
num=decimal_number
while num > 0:
    remainder=num%8
    octal = str(remainder)+ octal
    num=num//8
octal="0"
    if octal=="":
        else octal  #In case the number is 0
#Converting to hexadecimal
hexadecimal=""
num=decimal_number
hex_digits="0123456789ABCDEF"
while num > 0:
    remainder=num%16
    hexadecimal = str(remainder)+ hexadecimal
    num=num//16
hexadecimal="0"
    if hexadecimal=="":
        else hexadecimal  #In case the number is 0
