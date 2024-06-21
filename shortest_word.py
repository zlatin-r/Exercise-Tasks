def find_short(s):
    words = [len(w) for w in s.split()]
    return min(words)

# def find_short(s):
#     return min(len(x) for x in s.split())
