


s = 'abcabcbb'


arr1 = []
i = 0
j = 0
max = 0

while i < len(s):

    if s[i] not in arr1:
        arr1.append(s[i])
        i += 1
        if max < i - j:
            max = i - j
    else:
        if max < i - j:
            max = i - j
        arr1.reverse()
        arr1.pop()
        j += 1
        i = j + len(arr1)

print(max)


# arr1 = [1,2,3]

# arr1.reverse()
# arr1.pop()

# print(arr1)