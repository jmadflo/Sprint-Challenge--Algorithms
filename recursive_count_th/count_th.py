'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if len(word) < 2:
        return 0

    letters = list(word)

    # take off existing last letter
    next_word = "".join(list(word)[:-1])

    # add 1 to our count_th(next_word) return value before returning otherwise just return count_th(next_word)
    if letters[-1] == 'h' and letters[-2] == 't': 
        return 1 + count_th(next_word)
    else:
        return count_th(next_word)
