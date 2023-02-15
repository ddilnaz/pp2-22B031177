def unique_list(numbers):
    unique = []
    for item in numbers :
        if item not in unique:
            unique.append(item)
    return unique


st = input()
parts = st.split(" ")
numbers = [int(i) for i in parts]
print(unique_list(numbers))

#print(unique_list([1, 2, 3, 1, 2]))
# [1, 2, 3]
