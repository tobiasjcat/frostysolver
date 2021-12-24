#!/usr/bin/env python3

#Paul Croft
#December 23, 2021


from itertools import combinations
from operator import itemgetter
from pprint import pformat, pprint
import string

def main():

    most_rotations = {}
    total_links = {}

    for lengths in combinations(range(1,11),3):
        unique_increments = set()
        first, second, third = lengths
        rotations = 0
        spelling = "{}{}{}".format( \
            string.ascii_lowercase[rotations % first], \
            string.ascii_uppercase[rotations % second], \
            string.digits[rotations % third], \
            )
        while spelling not in unique_increments:
            unique_increments.add(spelling)
            rotations += 1
            spelling = "{}{}{}".format( \
                string.ascii_lowercase[rotations % first], \
                string.ascii_uppercase[rotations % second], \
                string.digits[rotations % third], \
                )
        signature = "{},{},{}".format(first,second,third)
        most_rotations[signature] = len(unique_increments)
        total_links[signature] = sum(lengths)


    most_rotations = sorted(most_rotations.items(), key=itemgetter(1),reverse=True)[:10]
    # total_links = sorted(most_rotations.items(), key=itemgetter(1))[:10]

    pprint(most_rotations)
    # print(total_links)


    return 0

if __name__ == '__main__':
    main()
