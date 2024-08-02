#My solution
secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
number = int(input("Enter number:  "))
while number != secret_number:
    print("Ha ha! You're stuck in my loop!")
    number = int(input("Enter number:  "))

print("Well done, muggle! You are free now.")


#AI solution
secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

while True:
    user_input = int(input("Enter an integer number: "))
    if user_input == secret_number:
        print(user_input)
        print("Well done, muggle! You are free now.")
        break
    else:
        print("Ha ha! You're stuck in my loop!")
