#Write a program to print all the ASCII values and their equivalent characters using a while loop. The ASCII values vary from 0 to 255.


ascii_value = 0


while ascii_value <= 255:
    print(ascii_value,"-",chr(ascii_value))
    # Increment the ASCII value
    ascii_value += 1
