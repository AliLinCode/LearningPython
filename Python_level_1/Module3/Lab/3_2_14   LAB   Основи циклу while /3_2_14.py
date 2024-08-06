#My Solutions
blocks = int(input("Enter the number of blocks: "))
i=1
height=0
while i <= blocks:
    blocks -= i
    height += 1
    i += 1
    #
# Write your code here.
#

print("The height of the pyramid:", height)


#AI Solutions
blocks = int(input("Enter the number of blocks: "))

height = 0
current_layer = 1

while blocks >= current_layer:
    blocks -= current_layer
    height += 1
    current_layer += 1

print("The height of the pyramid:", height)