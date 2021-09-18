from map import Map
from count import count_words, count_letters, count_duplicates

# Custom Map
m = Map()
m.put('a', 0)
m.put('b', 1)
m.put('c', 2)
m.put('d', 3)
m.put('e', 4)
m.put('f', 5)

assert m.get('a') == 0
assert m.get('b') == 1
assert m.get('c') == 2
assert m.get('d') == 3
assert m.get('e') == 4
assert m.get('f') == 5

m.delete('b')
assert m.get('b') is None
assert m.get('a') is not None
assert m.get('a') == 0

# Python Map/Dict
n = {}
n['a'] = 0 # put 
n['b'] = 1 # put 

assert n.get('a') == 0
assert n.get('b') == 1

# Test count_words()
sentence = "the quick brown fox jumps over the lazy dog and the dog does not mind it at all the fox is just a fox"
expected = {'a': 1, 'all': 1, 'and': 1, 'at': 1, 'brown': 1, 'does': 1, 'dog': 2, 'fox': 3, 'is': 1, 'it': 1, 'jumps': 1, 'just': 1, 'lazy': 1, 'mind': 1, 'not': 1, 'over': 1, 'quick': 1, 'the': 4}
assert count_words(sentence) == expected
print("PASS count_words()")

# Test count_letters
word = "the quick brown fox jumps over the lazy dog and the dog does not mind it at all the fox is just a fox"
expected = {' ': 23, 'a': 5, 'b': 1, 'c': 1, 'd': 5, 'e': 6, 'f': 3, 'g': 2, 'h': 4, 'i': 4, 'j': 2, 'k': 1, 'l': 3, 'm': 2, 'n': 4, 'o': 9, 'p': 1, 'q': 1, 'r': 2, 's': 4, 't': 8, 'u': 3, 'v': 1, 'w': 1, 'x': 3, 'y': 1, 'z': 1}
assert count_letters(word) == expected
print("PASS count_letters()")

# Test count_duplicates()
word = "geeksforgeeeks"
expected = {'e': 5, 'g': 2, 'k': 2, 's': 2}
assert count_duplicates(word) == expected
print("PASS count_duplicates()")
