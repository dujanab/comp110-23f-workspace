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

i: int = 0
s: str = ""

while i < 4:
    if i % 2 == 0:
        s = s + "h"
    else:
        if i % 3 == 0:
            s = s + "!"
        else:
            s = s + "e"
    i = i + 1

# Stack 
# i = 0 1 2 3 4
# s = “” “h” “he” “heh” “heh!”

# Output:
# No outputs because no “print()” function
