# step 1
beatles = []
print("Step 1:", beatles)
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
# step 2
print("Step 2:", beatles)

for i in range(2):
    i=str(input("Add new member to list: "))
    beatles.append(i)
# step 3
print("Step 3:", beatles)

del beatles[4]
del beatles[3]
# step 4
print("Step 4:", beatles)

# step 5
beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))