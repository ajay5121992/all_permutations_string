# Python program to print all permutations of string in lexicographical order


# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.


def permute(a, l, r):
    if l == r:
        output.append(''.join(a))
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)
            a[l], a[i] = a[i], a[l]  # backtrack
    return output


# Input
val = int(input(""))
strings=[]
for i in range(val):
    # Driver program to test the above function
    string = input("")
    strings.append(string)

# calling function on given input string
for str in strings:
    output = []
    output=permute(list(str), 0, len(str) - 1)
    output.sort()
    print(" ".join(output))