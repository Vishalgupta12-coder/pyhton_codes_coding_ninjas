def permu(li):
    permutations = [[a, b, c]
                    for a in li for b in li for c in li if a != b and b != c and c != a]
    return permutations


ans = permu(input("Enter string whose permutations you wants : "))
for i in ans:
    print(''.join(i))
