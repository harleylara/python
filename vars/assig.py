x = [1, 2, 3]
print(f"x addr: {hex(id(x))}, value: {x = }")
x = x + [4, 5, 6] # this creates a new object and then append
print(f"x addr: {hex(id(x))}, value: {x = }")

y = [1, 2, 3]
print(f"y addr: {hex(id(y))}, value: {y = }")
y += [4, 5, 6] 
# this append the list to the current y
# call the list.__iadd__(self, other_iterable)
print(f"y addr: {hex(id(y))}, value: {y = }")
