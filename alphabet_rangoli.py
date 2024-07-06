def print_rangoli(size):
    alphabet = [chr(i) for i in range(97, 123)][:size]
    alphabet.reverse()
    len_alphabet = len(alphabet)
    w = size + (size - 1)
    w += (w - 1)

    for i in range(len_alphabet):
        letters_to_print = alphabet[:i + 1]
        letters_to_print = letters_to_print + letters_to_print[:-1][::-1]
        print("-".join(letters_to_print).center(w, '-'))

    for i in range(len(alphabet) - 1):
        letters_to_print = alphabet[:len(alphabet) - i - 1]
        letters_to_print = letters_to_print + letters_to_print[:-1][::-1]
        print("-".join(letters_to_print).center(w, '-'))


print_rangoli(5)
