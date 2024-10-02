s1 = input()
s2 = input()


def isAnagram(str1, str2):
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False


print(sorted(s1, reverse=True), sorted(s2))
print(isAnagram(s1, s2))
