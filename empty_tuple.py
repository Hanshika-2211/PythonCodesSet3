# Write a program to remove an empty tuple from a list of tuples.
data = [(), (), ("",), ('a', 'b'), ('a', 'b', 'c'), ('d')]
print("Original list:",data)
index = len(data) - 1
while index >= 0:
    if not data[index]:  
        data.pop(index)  
    index -= 1
print("Updated list:", data)