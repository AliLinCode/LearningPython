import time

c0 = int(input("Enter digital: "))
steps = 0

if c0 <= 0:
    print("End")
else:
    while c0 != 1:
        if c0%2 == 0:
            print("if 1")
            c0 = c0 / 2
            print(c0)
            steps += 1
            time.sleep(3)

        elif c0%2 == 1:
            print("if 2")
            c0 = 3 * c0 + 1
            print(c0)
            steps += 1

print("Steps: ", steps)


