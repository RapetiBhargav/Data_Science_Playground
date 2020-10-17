#Just as regular expressions put strings on steroids, the itertools module 
#puts iterators on steroids.

#HAWAII + IDAHO + IOWA + OHIO == STATES
#510199 + 98153 + 9301 + 3593 == 621246
#Puzzles like this are called cryptarithms or alphametics.

#Reference : Raymond Hettinger

import re
import itertools

def solve(puzzle):
    words = re.findall('[A-Z]+', puzzle.upper())
    unique_characters = set(''.join(words))
    assert len(unique_characters) <= 10, 'Too many letters'
    first_letters = {word[0] for word in words}
    n = len(first_letters)
    sorted_characters = ''.join(first_letters) + \
        ''.join(unique_characters - first_letters)
    characters = tuple(ord(c) for c in sorted_characters)
    digits = tuple(ord(c) for c in '0123456789')
    zero = digits[0]
    for guess in itertools.permutations(digits, len(characters)):
        if zero not in guess[:n]:
            equation = puzzle.translate(dict(zip(characters, guess)))
            if eval(equation):
                return equation

if __name__ == '__main__':
    import sys
    for puzzle in sys.argv[1:]:
        print(puzzle)
        solution = solve(puzzle)
        if solution:
            print(solution)
            
#Trying it out on some puzzles            
print(solve("HAWAII + IDAHO + IOWA + OHIO == STATES"))
print(solve("I + LOVE + YOU == DORA"))
print(solve("SEND + MORE == MONEY"))