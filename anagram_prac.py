s1 = input().replace(" ", '').lower()
s2 = input().replace(" ", '').lower()


def isAnagram1(s1, s2):
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False


print(f'{s1} is {s2}\'s anagram: {isAnagram1(s1, s2)}')

