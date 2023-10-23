"""Lists in memory."""

x: list[str] = ["Comp", "110"]
x[1] = "210"
y: list[str] = x
print(y)

# Stack
# Globals
# x = –> list[str] in heap
# y = -> list[str] in heap

# Heap
# list[str]
# 0 "Comp"
# 1 "110", becomes "210"

# Output
# ["Comp", "210"]

a: str = "24"
b: str = a
a += "6"
print(b)

a: list[int] = [2,4]
b: list[int] = a
a.append(6)
print(b)

# Stack
# Globals
#a = "24" –> "246" list[int] in heap
#b = "24" –> list[int] in heap

# Heap
# list[int]
# 0     2
# 1     4
# 2     6

# Output
# "24"
# [2,4,6]



# Stack                             Heap
# dup =     –>                      fn 1-6

# groceries =   –>                  list [str]
# dup RA = 9                        0   "apples"
# xs            –>                  1   "eggs"
# start_len = 2                     2   "apples"
# i = 0, becomes 1, becomes 2       3   "eggs"
# RV = none

# Output
# ["apples, "eggs", "apples", "eggs"]

def odds_list(min: int, max: int) -> list[int]:
    odds: list[int] = list()
    x: int = min
    while x <= max:
        if x % 2 == 1:
            odds.append(x)
        x += 1
    return odds

global_odds: list[int] = odds_list(2,10)
print(global_odds)

# Stack                                 Heap

# Globals:
# odds_list =         –>                fn 1-9
# global_odds =       –> list[int]

# global_odds:
# RA = 11
# min = 2
# max = 10
# odds =              –> list[int]      list[int]
# RV -                –> list[int]
# x = 2, 3, 4, 5, 6, 7, 8, 9, 10, 11    0   3
#                                       1   5
#                                       2   7
#                                       3   9

#Output
# [3, 5, 7, 9]


