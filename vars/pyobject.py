x = 534
# x is just pointing to the memory address
# of the PyObject
print(hex(id(x)))

# if we change the value of the variable
# we are pointing to a different memory location
x = 999
print(hex(id(x)))

# in this case both share the same address
y = x
print(f"x addr: {hex(id(x))}, value: {x = }")
print(f"y addr: {hex(id(y))}, value: {y = }")

# but if you change one
# you are creating a new PyObject
# and python update the memory location of 
# that variable
x = 6
print(f"x addr: {hex(id(x))}, value: {x = }")
print(f"y addr: {hex(id(y))}, value: {y = }")
