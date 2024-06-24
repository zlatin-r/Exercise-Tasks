def scramble(s1, s2):
    letters = list(s1)
    for i in range(len(s2)):
        el = s2[i]
        if el not in letters:
            return False
        letters.remove(el)
    return True


# def scramble(s1,s2):
#     for c in set(s2):
#         if s1.count(c) < s2.count(c):
#             return False
#     return True


print(scramble('hwypyjjudlcfn', 'lndhfyfjy'))
print(scramble('rkqodlw', 'world'))
print(scramble('cedewaraaossoqqyt', 'codewars'))
print(scramble('katas', 'steak'))
