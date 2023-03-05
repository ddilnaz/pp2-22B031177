def count_case(string):
    upper_count = 0
    lower_count = 0
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return (upper_count, lower_count)
    
string = input(str())
upper, lower = count_case(string)
print(f"Uppercase count: {upper}")
print(f"Lowercase count: {lower}")