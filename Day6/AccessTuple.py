thistuple = ("apple", "banana", "cherry")
print(thistuple[2])

# Negative Indexation
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

# Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

# Begin
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

# End
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

# Negative Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

# Verify
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes")