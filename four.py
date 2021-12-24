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

    for lengths in combinations(range(1,11),4):
        unique_increments = set()
        first, second, third, fourth = lengths
        rotations = 0
        spelling = "{}{}{}{}".format( \
            string.ascii_lowercase[rotations % first], \
            string.ascii_uppercase[rotations % second], \
            string.digits[rotations % third], \
            string.punctuation[rotations % fourth], \
            )
        while spelling not in unique_increments:
            unique_increments.add(spelling)
            rotations += 1
            spelling = "{}{}{}{}".format( \
                string.ascii_lowercase[rotations % first], \
                string.ascii_uppercase[rotations % second], \
                string.digits[rotations % third], \
                string.punctuation[rotations % fourth], \
                )
        signature = "{},{},{},{}".format(first,second,third,fourth)
        most_rotations[signature] = len(unique_increments)
        total_links[signature] = sum(lengths)


    most_rotations = sorted(most_rotations.items(), key=itemgetter(1),reverse=True)
    # total_links = sorted(most_rotations.items(), key=itemgetter(1))[:10]

    # pprint(most_rotations)
    # print(total_links)

    for k,v in most_rotations:
        print("{}|{}|{}".format(k,v,total_links[k]))


    return 0

if __name__ == '__main__':
    main()
