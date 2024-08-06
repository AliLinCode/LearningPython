import traceback

i = 15
j = 22
log = i and j
print(log)
bit = i & j
print(bit)
logneg = not i
print(logneg)
bitneg = ~i
print(bitneg)
flag_register = 0x1234
print(flag_register)
the_mask = 8
flag_register |= the_mask
print(flag_register)

var = 4
var_right = var >> 1
var_left = var << 2
print(var, var_left, var_right)
x = 1
y = 0

z = ((x == y) and (x == y)) or not (x == y)
print(not (z))

x = 6
y = 2

a = x & y
b = x | y
c = ~x  # tricky!
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)

try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)
    в=44

except:
    print("Перевір чи всі змінні та функції в нормі")
    print("Трасування винятку:")


    traceback.print_exc()

