# response: int = int(input("Pick an even number < 10: "))

# if (response % 2 != 0) or (response >= 10):
#     print ("Wrong number")
# else:
#     if (response < 10):
#         print ("Guess was less than 10.")
# if response % 2 == 0:
#     print("Guess was even.")

# x = 1 
# y = 2
# z = "x"

# if x > y:
#     print(str(x))
# else:
#     if y % 2 == 0:
#         print(str(y))
# print (z)

# i: int = 0
# s: str = ""

# while i < 4:
#     if i % 2 == 0:
#         s = s + "h"
#     else:
#         if i % 3 == 0:
#             s = s + "!"
#         else:
#             s = s + "e"
#     i = i + 1

# Stack 
# i = 0 1 2 3 4
# s = “” “h” “he” “heh” “heh!”

# Output:
# No outputs because no “print()” function

# def mimic(my_words: str) -> str:
#     """Given the string my_words, outputs the same string"""
#     return my_words

# print(mimic("Hello!")) 

# def mimic_letter(my_words: str, letter_idx: int) -> str:
#     """Outputs the character of my_words at index letter_idx"""
#     if letter_idx >= len(my_words):
#         return("Index too high")
#     return my_words[letter_idx]

# print(mimic_letter("Hello", 6))

# xs: str = "123"
# ys: str = "45"

# x_idx: int = 0
# while x_idx < len(xs):
#     y_idx: int = 0
#     while y_idx < len(ys):
#         print(f"{xs[x_idx]},{ys[y_idx]}")
#         y_idx = y_idx + 1
#     x_idx = x_idx + 1

# stack:
# xs = "123", 
# ys = "45"
# x_idx = 0, 1, 2
# y_idx = 0, 1

# output:
# (1, 4)
# (1, 5)
# (2, 4)
# (2, 5)
# (3, 4)
# (3, 5)

# def main():
#     """Main code of program"""
#     y: float = double(2.0)
#     print(halve(y))

# def halve(x: float) -> float:
#     """Returns half the value of x"""
#     print(f"halve({x})")
#     return x / 2.0

# def double(x: float) -> float:
#     """Double a value"""
#     print(f"double({x})")
#     return x * 2.0

# main()

# stack:
# globals
#     main ->
#     halve ->
#     double -> 
# main
#     RA = 16  y = 4.0
#     RV = None
# double
#     RA = 3   x = 2.0
#     RV = 4.0
# halve
#     RA = 4   x = 4.0
#     RV = 2.0


# heaps:
# fn 1-4
# fn 6-9
# fn 11-14

# output:
# double(2.0)
# halve(4.0)
# 2.0

# def f(x: int) -> int:
#     return x
#     x *= 2
#     print(x)

# y: int = f(3)
# print (y)

# x = type(9 / len( str(110)))
# print (x) 

# y = "440" + "20"
# print (y)

# print(55 % 2 ** 4)

# z = "Saturday"
# print(f'"{z[2]}{z[1]}{z[4]}"')

# print(2 + 2 / 2 ** (2 * 0))

# print("Saturday"[2] + "Saturday"[1] + "Saturday"[4])

# x: int = 10
# result: str = ""

# while x >= 0:
#     if x % 3 > 0:
#          result = result + str(x)
#     else:
#          result = str(x) + result
#     x = x - 1

# print(result)

# print("" + str(10))
# print(str(10) + "")

# from random import random
# print(type(random()))

# print(True or False)
# print(True and False)
# print(False or True)
# print(False and True)