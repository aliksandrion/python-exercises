from math import prod


def count_find_num(primesL, limit):
    # my code is here:
    base = prod(primesL)  # the smallest number after the multiplication of numbers in primesL
    list_of_numbs = [base]  # the list of multiplication results
    if base <= limit:
        for i in primesL:  # multiply 'base' by each number in primesL
            max_mult = base
            while max_mult <= limit:
                max_mult = max_mult * i
                if max_mult <= limit:
                    list_of_numbs.append(max_mult)
        for j in primesL[1:]:  # multiply numbers in 'list_of_numbs' by each number in primesL one more time
            for k in list_of_numbs:
                new_number = j * k
                if new_number not in list_of_numbs and new_number <= limit:  # add the 'new_number' if it is not on the
                    list_of_numbs.append(new_number)                         # 'list_of_numbs'

        return [len(list_of_numbs), max(list_of_numbs)]
    else:
        return []


# test
primesL = [2, 5, 7]
limit = 500
assert count_find_num(primesL, limit) == [5, 490]

primesL = [2, 3]
limit = 200
assert count_find_num(primesL, limit) == [13, 192]

primesL = [2, 5]
limit = 200
assert count_find_num(primesL, limit) == [8, 200]

primesL = [2, 3, 5]
limit = 500
assert count_find_num(primesL, limit) == [12, 480]

primesL = [2, 3, 5]
limit = 1000
assert count_find_num(primesL, limit) == [19, 960]

primesL = [2, 3, 47]
limit = 200
assert count_find_num(primesL, limit) == []
