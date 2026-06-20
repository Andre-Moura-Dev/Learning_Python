x = ("apple", "banana", "cherry")
y = list(x) # Convert Tuple to List
y[1] = "Kiwi"
x = tuple(y) # Transform List in Tuple

print(x)

# Add Itens
thisTuple = ("apple", "banana", "cherry")
y = list(thisTuple) # Convert Tuple to List
y.append("orange")
thisTuple = tuple(y) # Transform List to Tuple

# Add Tuple in Other
thisTuple = ("apple", "banana", "cherry")
y = ("orange",)
thisTuple += y

print(thisTuple)