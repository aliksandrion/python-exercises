from itertools import combinations


def bananas(s) -> set:
    result = set()
    # my code is here:
    for i in combinations(range(0, len(s)), len(s) - len('banana')):  # generates all combinations with '-'
        m = list(s)
        for j in i:  # replace the letter with the '-' in the input word
            m[j] = '-'
        if [k for k in m if k != '-'] == list('banana'):  # adds to the 'result' if replacement results in the word 'banana'
            result.add(''.join(m))
    return result


# test
assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                                "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                                "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}
