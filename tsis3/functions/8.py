def has_33(nums):
    c = 0
    for i in range(len(nums) - 2):
        if nums[i] == 0 and nums[i+1] == 0 and nums[i + 2] == 7:
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