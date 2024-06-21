def hashtag_generator(string):
    text = string.strip().split()
    result = '#'

    if text == '':
        return False

    for word in text:
        result += word.capitalize()

    if len(result) > 140 or result == '#':
        return False

    return result



print(hashtag_generator("Hello there thanks for trying my Kata"))
print(hashtag_generator("      The    hastag     "))
