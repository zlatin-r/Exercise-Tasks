string = input()
position, character = input().split(' ')


def mutate_string(string, position, character):

    return string[:int(position)] + character + string[int(position) + 1:]


print(mutate_string(string, position, character))
