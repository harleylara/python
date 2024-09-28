x = 534
# x is just pointing to the memory address
# of the PyObject
print(hex(id(x)))

# if we change the value of the variable
# we are pointing to a different memory location
x = 999
print(hex(id(x)))
