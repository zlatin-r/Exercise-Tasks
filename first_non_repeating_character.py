def first_non_repeating_letter(string):
    for i in range(len(string)):
        if string.lower().count(string[i].lower()) == 1:
            return string[i]
    return ''


# def first_non_repeating_letter(string):
#     singles = [i for i in string if string.lower().count(i.lower()) == 1]
#     return singles[0] if singles else ''


print(first_non_repeating_letter('sTreStSre'))
print(first_non_repeating_letter('stress'))
print(first_non_repeating_letter('sTreSS'))
