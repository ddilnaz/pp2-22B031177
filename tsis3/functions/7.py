def has_33(nums):
    c = 0
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            c = 1
            break
    if c == 1:
        return True
    else:
        return False

st = input()
parts = st.split(" ")
numbers = [int(i) for i in parts]
print(has_33(numbers))
