t = ([1, 2, 3]) # type ? tuple or list?

t = 1, [1, 2, 3]

try:
    t[1] = 5 # error
except Exception as e:
    print(e)

try:
    t[1] = [1, 3] # error
except Exception as e:
    print(e)

try:
    t[1].append([4, 5, 6]) # change the mutable list (the tuple stay the same)
    print(f"after append: {t = }")
except Exception as e:
    print(e)

t = 1, [6, 5, 4]
try:
    t[1] += [3, 2, 1]
    print(f"After += {t = }")
except Exception as e:
    print(e)
